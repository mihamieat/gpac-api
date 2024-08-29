[![codecov](https://codecov.io/gh/mihamieat/gpac-api/graph/badge.svg?token=5UM8L15FL1)](https://codecov.io/gh/mihamieat/gpac-api)
# Gpac API documentation
## Overview
> GpacAPI is a service for interacting with the GPAC application.

See the API documentation for details.
## Installation
It is recommended to run the server in a separate environment.
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
To run the server in a docker container.

Create a Docker image.
```sh
docker build -t gpac_api_image .
```
Run the server container.
```sh
docker run -d --name gpac_api_container -p 80:80 gpac_api_image
```
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
