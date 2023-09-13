#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.create_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        The update_at attribute with the current datetime is updated.
        """
        self.update_at = datetime.now()

    def to_dict(self):
        """
        A dictionary representation of the instance is returned.
        """
        instance_dict = self.__dict__.copy()
        instance_dict['create_at'] = self.create_at.isoformat()
        instance_dict['update_at'] = self.update_at.isoformat()
        instance_dict['__class__'] = self.__class__.__name__  
        return instance_dict
