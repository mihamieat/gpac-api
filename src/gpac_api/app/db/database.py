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

    DATABASE_USER = os.getenv("DATABASE_USER", config.get("DATABASE_USER"))
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", config.get("DATABASE_PASSWORD"))
    DATABASE_DOMAIN = os.getenv("DATABASE_DOMAIN", config.get("DATABASE_DOMAIN"))
    DATABASE_APP_NAME = os.getenv("DATABASE_APP_NAME", config.get("DATABASE_APP_NAME"))
    DATABASE_CLIENT = os.getenv("DATABASE_CLIENT", config.get("DATABASE_CLIENT"))

    if (
        not DATABASE_USER
        or not DATABASE_PASSWORD
        or not DATABASE_DOMAIN
        or not DATABASE_APP_NAME
        or not DATABASE_CLIENT
    ):
        logger.error("Required environment variables for database are missing")
        raise EnvironmentError("Missing required environment variables")

    DATABASE_URL = (
        f"mongodb+srv://{DATABASE_USER}:{DATABASE_PASSWORD}"
        f"@{DATABASE_DOMAIN}/?retryWrites=true&w=majority&appName={DATABASE_APP_NAME}"
    )

    client = MongoClient(DATABASE_URL)
    db = client[DATABASE_CLIENT]
else:
    # Test environment uses unauthenticated connection for simplicity
    client = MongoClient("mongodb://localhost:27017")
    db = client["testdb"]
    logger.warning("test environment in use")
