# -*- coding: utf-8 -*-
"""Database module"""
import os

from dotenv import load_dotenv, dotenv_values
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient

load_dotenv()

if os.environ.get("TESTING").lower() not in ("true", "1", "yes"):
    config = dotenv_values()
    DATABASE_USER = config.get("DATABASE_USER")
    DATABASE_PASSWORD = config.get("DATABASE_PASSWORD")
    DATABASE_DOMAIN = config.get("DATABASE_DOMAIN")
    DATABASE_APP_NAME = config.get("DATABASE_APP_NAME")
    DATABASE_URL = f"mongodb+srv://{DATABASE_USER}:{DATABASE_PASSWORD}\
@{DATABASE_DOMAIN}/?retryWrites=true&w=majority&appName={DATABASE_APP_NAME}"
    DATABASE_CLIENT = config.get("DATABASE_CLIENT")

    client = AsyncIOMotorClient(DATABASE_URL)
    db = client[DATABASE_CLIENT]
else:
    client = MongoClient("mongodb://tester:tester$@localhost:27017")
    db = client["testdb"]
