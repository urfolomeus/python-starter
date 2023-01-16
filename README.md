# Python starter

This is an example starter python project that can be used to kickstart various types of python projects.

- [Types of project](#types-of-project)
- [What's included](#whats-included)
- [What's not included](#whats-not-included)
- [Usage](#usage)

## Types of project

The main branch is for a simple Python app and can be used as the starting point for other types of applications.

There are also branches for:

- FastAPI with Postgres (`fastapi-pg`)
- others TBC

## What's included

- `.tool-versions` file with the version of Python that was last used with this starter project
- `src/dev_requirements.txt` dependencies used during development and testing
- `src/requirements.txt` runtime dependencies
- `src/app/main.py` the Python entry point

## What's not included

I used to run my Python apps on Docker using Docker Compose, but I always ended up down a rabbit hole trying to get formatting and linting to work in the way that I wanted. I still use Docker Compose if I want to run things like Postgres, but I expose the ports locally and treat the containers like any other remote server. This allows me to have a simpler dev environment and save containerizing for deployed environments.

## Usage

1. Clone this repo, delete the `.git` folder and then start a new git history with `git init`.
2. Run the init script `./bin/init` to set up the venv etc
3. Run code inside of the venv `source .venv/bin/activate` (or `activate.fish` if in a fish shell)

## Tests

Tests can be run manually with `pytest` or `pytest path/to/file`. Alternatively, we can use Pytest Watch to run the tests automatically when a file is changed with `ptw`.
