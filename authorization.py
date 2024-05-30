import json
import multiprocessing
import os
import threading
import webbrowser

import click
import requests
from flask import Flask, after_this_request, request

REDIRECT_URI = "http://localhost:5000/callback"
AUTH_FILE = os.path.expanduser("~\.harvest_cli_config.json")

app = Flask(__name__)
data = {}


def start_local_authorization_server():
    """Start a local server to handle OAuth2 callback."""
    from authorization import app

    app.run(port=5000)


@app.route("/callback")
def callback():
    """Handle OAuth2 callback."""
    code = request.args.get("code")
    auth = load_auth()

    # Exchange authorization code for access token
    response = requests.post(
        "https://id.getharvest.com/api/v2/oauth2/token",
        data={
            "code": code,
            "client_id": auth["clientId"],
            "client_secret": auth["clientSecret"],
            "redirect_uri": REDIRECT_URI,
            "grant_type": "authorization_code",
        },
        headers={"User-Agent": "Harvest CLI"},
    )

    if response.status_code in [200, 201]:
        tokens = response.json()
        auth["access_token"] = tokens["access_token"]
        auth["refresh_token"] = tokens["refresh_token"]
        save_auth(auth)

        print(
            "Authentication successful. waiting for authorization server to exit gracefully.."
        )

        @after_this_request
        def shutdown_server(response):
            threading.Timer(
                2.0, shutdown
            ).start()  # Wait for 5 seconds before shutting down
            return response

        return (
            "Authentication successful. You can close this tab and return to the CLI."
        )
    else:
        return "Authentication failed.", response.status_code


def get_headers():
    """Get headers with authorization token."""
    auth = load_auth()
    return {
        "Authorization": f"Bearer {auth['access_token']}",
        "User-Agent": "Harvest CLI",
    }


def load_auth():
    """Load authentication details from file if it exists."""
    if os.path.exists(AUTH_FILE):
        with open(AUTH_FILE, "r") as f:
            return json.load(f)
    return {}


def save_auth(config):
    """Save authentication details to file."""
    with open(AUTH_FILE, "w") as f:
        json.dump(config, f)


def shutdown():
    """Shutdown the Flask server."""
    os._exit(0)


def authorize_cli():
    """Authorize the CLI to access Harvest API."""
    client_id = try_get_client_and_secret()
    # Step 1: Authenticate
    flask_process = multiprocessing.Process(target=start_local_authorization_server)
    flask_process.start()

    auth_url = f"https://id.getharvest.com/oauth2/authorize?client_id={client_id}&response_type=code&redirect_uri={REDIRECT_URI}"
    webbrowser.open(auth_url)
    click.echo("Opening browser for authentication...")
    # This will block the process until the flask_process stops.
    flask_process.join()


def try_get_client_and_secret():
    """Try to get client id and secret from file or prompt user to enter them."""
    auth = load_auth()
    if not auth.get("clientId") or not auth.get("clientSecret"):
        clientId = click.prompt("Please enter client id", type=str)
        clientSecret = click.prompt("Please enter client secret", type=str)

        auth["clientId"] = clientId
        auth["clientSecret"] = clientSecret
        save_auth(auth)
        return clientId
    else:
        return auth["clientId"]


if __name__ == "__main__":
    app.run()
