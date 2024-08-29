#!/bin/sh

docker-compose -f docker-compose.test.yaml down
docker-compose -f docker-compose.test.yaml up -d
poetry run pytest --cov=src --cov-report=xml
docker-compose -f docker-compose.test.yaml down
coverage html
