#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from .base_model import BaseModel

# A dictionary is created containing the class references needed
models = {'BaseModel': BaseModel}

# The models dictionary are passed when creating the FileStorage instance
storage = FileStorage()
storage.reload()
