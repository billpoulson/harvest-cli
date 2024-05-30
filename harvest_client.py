import click
import inquirer
import requests

from authorization import get_headers
from config import load_config


def get_linked_task_assignments(project_id):
    """Get all linked task assignments for a project."""
    headers = get_headers()
    response2 = requests.get(
        "https://api.harvestapp.com/v2/task_assignments",
        headers=headers,
    )
    data2 = response2.json()
    task_assignments = [
        assignment
        for assignment in data2["task_assignments"]
        if assignment["project"]["id"] == project_id
    ]

    return [assignment["task"] for assignment in task_assignments]


def prompt_for_task_type(project_id):
    """Prompt user to select a task type for the project."""
    tasks = get_linked_task_assignments(project_id)
    project_choices = [(project["name"], project["id"]) for project in tasks]

    questions = [
        inquirer.List(
            "task_id",
            message="Please select the project",
            choices=project_choices,
        )
    ]
    answers = inquirer.prompt(questions)
    return answers["task_id"]


def get_projects():
    """Fetch all projects from Harvest."""
    headers = get_headers()
    response = requests.get("https://api.harvestapp.com/v2/projects", headers=headers)
    if response.status_code == 200:
        return response.json()["projects"]
    else:
        click.echo(f"Failed to fetch projects. Status code: {response.status_code}")
        return []


def prompt_select_project():
    """Prompt user to select a project."""
    projects = get_projects()
    if not projects:
        click.echo("No projects found. Exiting.")
        return

    project_choices = [(project["name"], project["id"]) for project in projects]

    questions = [
        inquirer.List(
            "project_id",
            message="Please select the project",
            choices=project_choices,
        )
    ]
    answers = inquirer.prompt(questions)
    selected_project_id = answers["project_id"]

    # Find the selected project name
    selected_project_name = next(
        project["name"] for project in projects if project["id"] == selected_project_id
    )

    click.echo(f"Project '{selected_project_name}' selected.")

    # Return selected project name and ID
    return selected_project_name, selected_project_id


def submit_time_entry(post_data):
    """Submit time entry to Harvest."""
    config = load_config()
    headers = get_headers()
    response = requests.post(
        "https://api.harvestapp.com/v2/time_entries", headers=headers, json=post_data
    )
    if response.status_code in [200, 201]:
        click.echo(f"Time tracked successfully. ({config['project_name']})")
    else:
        click.echo(f"Failed to track time. Status code: {response.status_code}")
