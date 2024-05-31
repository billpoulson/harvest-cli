import datetime

import click

from authorization import authorize_cli
from config import (
    load_config,
    save_config,
)
from harvest_client import (
    prompt_for_task_type,
    prompt_select_project,
    submit_time_entry,
)
from util import parse_hours


@click.group()
def cli():
    """A simple CLI tool to interact with Harvest API"""
    pass


@click.command()
def track():
    """Track time against the selected project."""
    config = load_config()

    if "project_id" not in config:
        click.echo("No project selected. Please select a project first.")
        return

    project_id = config["project_id"]
    task_id = prompt_for_task_type(project_id)
    hours = click.prompt("Please enter hours (in H:MM format)", type=str)
    notes = click.prompt("Please enter any notes", type=str)

    # Parse hours input
    try:
        parsed_hours = parse_hours(hours)
    except ValueError as e:
        click.echo(str(e))
        return

    post_data = {
        "project_id": project_id,
        "task_id": task_id,
        "hours": parsed_hours,
        "notes": notes,
        "spent_date": datetime.date.today().isoformat(),
    }

    submit_time_entry(post_data)


@click.command()
def init():
    """Initialize the CLI by authenticating and selecting a project."""

    authorize_cli()

    selected_project_name, selected_project_id = prompt_select_project()

    config = load_config()
    config["project_name"] = selected_project_name
    config["project_id"] = selected_project_id
    save_config(config)


cli.add_command(track)
cli.add_command(init)

if __name__ == "__main__":
    cli()
