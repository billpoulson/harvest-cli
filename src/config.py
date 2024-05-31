# Define configuration file path
import json
import os

CONFIG_FILE = os.path.abspath(".\.harvest.json")


def load_config():
    """Load configuration from file if it exists."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}


def save_config(config):
    """Save configuration to file."""
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)
