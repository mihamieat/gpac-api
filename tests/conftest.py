# -*- coding: utf-8 -*-
"""Test the main module."""

import os
from src.gpac_api.app.db.database import get_database

os.environ["TESTING"] = "1"
db = get_database()

# notifs
notif_collection = db["notif"]
