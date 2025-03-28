[![codecov](https://codecov.io/gh/mihamieat/gpac-api/graph/badge.svg?token=5UM8L15FL1)](https://codecov.io/gh/mihamieat/gpac-api)
![CI](https://github.com/mihamieat/gpac-api/actions/workflows/ci.yml/badge.svg)
[![StackShare](http://img.shields.io/badge/tech-stack-0690fa.svg?style=flat)](https://stackshare.io/mihamieat/gpac)
# Gpac API
## Overview
GpacAPI is a service for interacting with the GPAC application.

See the [API documentation](http://preprod.api.gpac.mihamina-dev.cloud/docs) for details.
⚠️ Link currently not in HTTPS.

## Features

- 📡 **FastAPI-based**: Built using FastAPI for high-performance API responses.
- 📊 **Database connectivity**: Uses MongoDB as the primary database.
- 🛠️ **CI/CD integration**: Automated testing, linting, and deployment workflows.
- 🐳 **Docker support**: Easily deployable using Docker containers.
- 📌 **Pre-commit hooks**: Ensures clean and standardized code.

## Environment variables
The following environment variables are required for running the API:
| **Variable Name**              | **Description**                                                                                         |
|-------------------------|----------------------------------------------------------------|
| `DATABASE_CLIENT`               | The name or identifier for the database client being used for the connection.                           |
| `DATABASE_CONNECTION_STRING`    | The full MongoDB connection string used to connect to the database, including credentials, server address, etc. |
| `FRONTEND_ORIGIN`               | The origin (URL) of the frontend application, the location where the frontend is hosted.      |

## Installation
It is recommended to run the server in a separate environment.

1. Clone the repository:

```sh
   git clone https://github.com/mihamieat/gpac-api.git
   cd gpac-api
```

2. Install dependencies
```sh
pip install -r requirements.txt
```
## Running the server
### In production
```sh
fastapi run src/gpac_api/app/main.py --port 80
```
### In development
```sh
fastapi dev src/gpac_api/app/main.py --reload
```
## Docker
Make sure to have Docker installed.

To run the server in a docker container.

Create a Docker image.
```sh
docker build -t gpac_api_image .
```
Run the server container.
```sh
docker run -d --name gpac_api_container -p 80:80 gpac_api_image
```
## CI/CD environment variables
Here is the list for CI/CD environment variables to be created in GitHub Action Secret variables.
| **Variable Name**            | **Description**                                                                 |
|----------------------|------------------------------------------|
| `CODECOV_TOKEN`              | The authentication token for uploading code coverage reports to Codecov.       |
| `DATABASE_CONNECTION_STRING` | The full connection string used to connect to the database in the CI/CD pipeline. |
| `DOCKERHUB_TOKEN`            | The access token for authenticating with DockerHub to push/pull images.        |
| `FRONTEND_ORIGIN`            | The origin (URL) of the frontend application, typically used for CORS settings. |
| `GH_PAT`                     | The GitHub Personal Access Token (PAT) used for authenticating GitHub actions or API requests. |
| `REMOTE_HOST`                | The hostname or IP address of the remote server used for deployment.           |
| `REMOTE_USER`                | The username for accessing the remote server.                                  |
| `SSH_PRIVATE_KEY`            | The private SSH key used for secure authentication with remote servers.        |
| `SSH_PUBLIC_KEY`             | The corresponding public SSH key for authentication and access control.        |

## Contributing
### pre-commit
Pre-commit is a tool that helps developers automatically run checks and formatting on their code before they commit changes to a version control system like Git.
#### Install
```sh
python -m ensurepip
curl -sSL https://bootstrap.pypa.io/get-pip.py | python -
python -m pip install --user pre-commit
pre-commit install
```
#### Unit Test
Unit test is an essential tool for the pre-commit action. It could also be launched alone.

Again, make sure to have Docker installed as well as [Docker Compose](https://docs.docker.com/compose/install/)

Make sure that the shell script is executable for the current user
```sh
chmod u+x ./unittest.sh
```
You can now run
```sh
./unittest.sh
```

## 📬 Contact

If you have any questions or need further assistance, feel free to open an issue or reach out! 🚀
