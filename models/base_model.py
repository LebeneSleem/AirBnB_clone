#!/usr/bin/python3
# This is an updated base model for the Air BnB project
import uuid
from datetime import datetime


class BaseModel:
    """Class for the Base Model"""

    def __init__(self, *args, **kwargs):
        """Constructor method for BaseModel."""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'update_at'):
                        # Convert string representation to datetime
                        setattr(self, key, datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
            # Ensure 'id' attribute is set or generate a new one
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.update_at = self.created_at
        # Add a call to 'new' method on 'storage' for new instances
        if not kwargs:
            storage.new(self)

    def __str__(self):
        """Public instance method."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        The update_at attribute with the current datetime is updated.
        """
        self.update_at = datetime.now()
        # Call 'save' method of 'storage'
        storage.save()

    def to_dict(self):
        """
        A dictionary representation of the instance is returned.
        """
        instance_dict = self.__dict__.copy()
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['update_at'] = self.update_at.isoformat()
        instance_dict['__class__'] = self.__class__.__name__
        return instance_dict
