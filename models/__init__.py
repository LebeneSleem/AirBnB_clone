#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

# The models dictionary are passed when creating the FileStorage
storage = FileStorage(models)
storage.reload()

# A dictionary is created containing the class references needed
models = {'BaseModel': BaseModel}
