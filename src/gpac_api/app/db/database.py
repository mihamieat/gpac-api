# -*- coding: utf-8 -*-
"""Database module"""

from motor.motor_asyncio import AsyncIOMotorClient


DATABASE_USER = "rmiham"
DATABASE_PASSWORD = "NAdKy4ljB52FhRvw"
DATABASE_DOMAIN = "atlasprime.8ldgp.mongodb.net"
DATABASE_APP_NAME = "AtlasPrime"
DATABASE_URL = f"mongodb+srv://{DATABASE_USER}:{DATABASE_PASSWORD}\
@{DATABASE_DOMAIN}/?retryWrites=true&w=majority&appName={DATABASE_APP_NAME}"
DATABASE_CLIENT = "gpac_db_test"

client = AsyncIOMotorClient(DATABASE_URL)
db = client[DATABASE_CLIENT]


def get_database():
    """
    Retrieves the current database instance.

    Args:
        None

    Returns:
        object: The current database instance.
    """
    return db
