# -*- coding: utf-8 -*-
"""Database module"""
import os
from dotenv import load_dotenv, dotenv_values
from pymongo import MongoClient

from src.gpac_api.app.utils.logger import logger
from src.gpac_api.app.utils.envcheck import is_testing_env

load_dotenv()

if not is_testing_env():
    logger.warning("No test environment in use")

    config = dotenv_values()

    DATABASE_CONNECTION_STRING = os.getenv(
        "DATABASE_CONNECTION_STRING", config.get("DATABASE_CONNECTION_STRING")
    )
    DATABASE_CLIENT = os.getenv("DATABASE_CLIENT", config.get("DATABASE_CLIENT"))

    if not DATABASE_CONNECTION_STRING or not DATABASE_CLIENT:
        logger.error("Required environment variables for database are missing")
        raise EnvironmentError("Missing required environment variables")

    client = MongoClient(DATABASE_CONNECTION_STRING)
    db = client[DATABASE_CLIENT]
else:
    # Test environment uses unauthenticated connection for simplicity
    client = MongoClient("mongodb://localhost:27017")
    db = client["testdb"]
    logger.warning("test environment in use")
    for collection_name in db.list_collection_names():
        db[collection_name].drop()
