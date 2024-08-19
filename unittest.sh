#!/bin/sh

docker-compose -f docker-compose.test.yaml up -d
pytest --cov=src tests/
docker-compose -f docker-compose.test.yaml down
coverage html
