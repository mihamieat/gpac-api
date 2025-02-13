[![codecov](https://codecov.io/gh/mihamieat/gpac-api/graph/badge.svg?token=5UM8L15FL1)](https://codecov.io/gh/mihamieat/gpac-api)
![CI](https://github.com/mihamieat/gpac-api/actions/workflows/ci.yml/badge.svg)
[![StackShare](http://img.shields.io/badge/tech-stack-0690fa.svg?style=flat)](https://stackshare.io/mihamieat/gpac)
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
