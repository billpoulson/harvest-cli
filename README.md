# Harvest CLI

Harvest CLI is a command-line interface tool designed to interact with the
Harvest API, providing functionalities to manage and automate various tasks
related to time tracking and invoicing.

## Features

- Authorization with the Harvest API.
- Configuration management for API keys and user settings.
- Command-line operations to interact with Harvest data.
- Utility functions for common operations.

## Project Structure

```ini {"id":"01HZ5PT3FXW7ACR50AJ754CWPC"}
harvest-cli-main/
│
├── .gitignore
├── README.md
├── authorization.py
├── cli.py
├── config.py
├── harvest_client.py
├── setup.py
├── util.py
└── .vscode/
    └── launch.json
```

- `.gitignore`: Specifies files and directories to be ignored by Git.
- `README.md`: Provides information about the project.
- `authorization.py`: Handles authorization with the Harvest API.
- `cli.py`: Contains the main command-line interface logic.
- `config.py`: Manages configuration settings.
- `harvest_client.py`: Implements the client for interacting with the Harvest
   API.
- `setup.py`: Script for setting up the project.
- `util.py`: Contains utility functions used throughout the project.
- `.vscode/launch.json`: Configuration file for VSCode debugging.

## Getting Started

### Prerequisites

- Python 3.7+
- An active Harvest account with API access.

### Installation

1. Clone the repository:

```bash {"id":"01HZ5PT3FXW7ACR50AJ8G2JEWN"}
git clone https://github.com/yourusername/harvest-cli.git
cd harvest-cli
```

2. Install the required dependencies:

```bash {"id":"01HZ5PT3FXW7ACR50AJC904BH2"}
pip install .
```

### Configuration

Create a configuration file to store your Harvest API key and other settings.
You can use the `config.py` module to manage your configurations.

### Usage

The main entry point for using the CLI is the `cli.py` file. You can run it
directly from the command line:

```bash {"id":"01HZ5PT3FXW7ACR50AJEBC9FW0"}
harvest init
harvest track
```

```bash {"id":"01HZ5PZV5V6FE884WRP322B0HD"}

```

#### Available Commands

- `init`: Set up authorization with the Harvest API and select a project for the active repo.
- `track`: Track time against the project.

```bash {"id":"01HZ5Q40YG0GYFG83QV94EY06J"}

```

## Testing

### Dependencies

```bash {"id":"01HZ6FAF2QTJ4KZMV79RK70VBG"}
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
poetry --version
pip install pytest-watch

```

```bash {"id":"01HZ6FHPBJSGEPA2MN8W49JFTB"}
[System.Environment]::SetEnvironmentVariable("Path", $env:Path + $env:APPDATA\Python\Scripts", [System.EnvironmentVariableTarget]::User)

```

```bash {"id":"01HZ6F95V5NNWADQCEGSN9ASH1"}
ptw
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file
for details.

## Contact

For questions or suggestions, please open an issue on GitHub or contact the
project maintainer.
