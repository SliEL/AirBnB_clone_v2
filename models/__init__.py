#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv


switch = getenv("HBNB_TYPE_STORAGE")

if switch == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
