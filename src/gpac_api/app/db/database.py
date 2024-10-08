# -*- coding: utf-8 -*-
"""Database module"""
from dotenv import load_dotenv, dotenv_values
from pymongo import MongoClient

from src.gpac_api.app.utils.logger import logger
from src.gpac_api.app.utils.envcheck import is_testing_env

load_dotenv()

if not is_testing_env():
    logger.warning("No test environment in use")
    config = dotenv_values()
    DATABASE_USER = config.get("DATABASE_USER")
    DATABASE_PASSWORD = config.get("DATABASE_PASSWORD")
    DATABASE_DOMAIN = config.get("DATABASE_DOMAIN")
    DATABASE_APP_NAME = config.get("DATABASE_APP_NAME")
    DATABASE_URL = f"mongodb+srv://{DATABASE_USER}:{DATABASE_PASSWORD}\
@{DATABASE_DOMAIN}/?retryWrites=true&w=majority&appName={DATABASE_APP_NAME}"
    DATABASE_CLIENT = config.get("DATABASE_CLIENT")

    client = MongoClient(DATABASE_URL)
    db = client[DATABASE_CLIENT]
else:
    # Test environment uses unauthenticated connection for simplicity
    client = MongoClient("mongodb://localhost:27017")
    db = client["testdb"]
    logger.warning("test environment in use")
