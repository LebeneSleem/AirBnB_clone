#!/usr/bin/python3
# This is a base model for the Air BnB project
import uuid
from datetime import datetime


class BaseModel:
    """Class for the Base Model"""
    def __init__(self):
        """public instance id to have a unique id for each base model"""
        self.id = str(uuid.uuid4())
        self.create_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        """Public instance method"""
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
