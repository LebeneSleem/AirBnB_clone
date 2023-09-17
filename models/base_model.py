#!/usr/bin/python3
"""This is the base model for the project"""

import uuid
from datetime import datetime


class BaseModel:
    """
    Base class for other models.

    Attributes:
        id (str): A unique identifier for each instance.
        created_at (datetime): The date and time when the instance is created.
        updated_at (datetime): The date and time when the instance
        is last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes an instance of BaseModel.

        Args:
            *args: List of arguments (not used in this implementation).
            **kwargs: Dictionary of key-value arguments.
            If provided, the instance
                attributes are populated from kwargs. Otherwise, new attributes
                are generated.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value,
                            '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: A formatted string containing the class name, id,
            and attribute dictionary.
        """

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute with the current date and time.
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the instance to a dictionary representation.

        Returns:
            dict: A dictionary containing the instance's attributes.
        """

        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict
