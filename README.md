# Python starter

This is an example starter python project that can be used to kickstart various types of python projects.

- [Types of project](#types-of-project)
- [What's included](#whats-included)
- [What's not included](#whats-not-included)
- [Usage](#usage)

## Types of project

The main branch is for a simple Python app and can be used as the starting point for other types of applications.

There are also branches for:

- FastAPI (`fastapi`)
- FastAPI with Postgres (`fastapi-pg`)

## What's included

- `.tool-versions` file with the version of Python that was last used with this starter project
- `.vscode` VS Code settings to make it easier to work with the project
- `bin` scripts to assist with initializing the application and such
- `src/dev_requirements.txt` dependencies used during development and testing
- `src/requirements.txt` runtime dependencies
- `src/app` the FastAPI application
  - `src/app/api` the FastAPI routers
  - `src/app/models` the database model schemas
  - `src/app/queries` the persistence layer
  - `src/app/db.py` the database setup
- `src/test` the PyTest tests
- `docker-compose.yml` config for the postgres container

## What's not included

I used to run my Python apps on Docker using Docker Compose, but I always ended up down a rabbit hole trying to get formatting and linting to work in the way that I wanted. I still use Docker Compose if I want to run things like Postgres, but I expose the ports locally instead. This allows me to have a simpler dev environment and save containerizing for deployed environments.

## Usage

1. Clone this repo, delete the `.git` folder and then start a new git history.
2. Run the init script `./bin/init` to set up the virtual environment etc.

```shell
git clone git@github.com:urfolomeus/python-starter -b fastapi-pg my-project
cd my-project
rm -rf .git
git init
git add .
git commit -m "Initial commit"
./bin/init
```

## Environment

The `./bin/init` script will create a `.envrc` file as a copy of the included `.envrc-example` file. This can be applied using a tool like [direnv](https://direnv.net/), or in any other way that you choose to apply environment variables. You may need to adjust some of the values before applying.

## Running the application

### Spinning up the database

We use Docker Compose to create a simple Postgres server. We should adjust the environment variables in the `docker-compose.yml` file to the values that we'd like to use for our database user, password and name. Any changes made to these environment variables should be reflected in the `DATABASE_URL` environment variable in our `.envrc` file.

```shell
docker compose up
```

### Starting the application

Ensure that we are in the virtual environment and then run the uvicorn server.

```shell
source .venv/bin/activate # activate.fish if in a fish shell
uvicorn app.main:app --reload
```

## Tests

Tests can be run manually with `pytest` or `pytest <path/to/file>`. Alternatively, we can use Pytest Watch to run the tests automatically when a file is changed with `ptw`.

Note that the database container needs to be running for the tests to work. See [Spinning up the database](#spinning-up-the-database).