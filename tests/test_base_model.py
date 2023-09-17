#!/usr/bin/python3
"""Unittest module for BaseModel."""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        """
        Test if the BaseModel is correctly initialized with id,
        created_at, and updated_at attributes.
        """
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_id_generation(self):
        """
        Test if each BaseModel instance generates a unique ID.
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_created_at_and_updated_at(self):
        """
        Test if created_at and updated_at are correctly
        initialized as datetime objects
        and if they have the same value upon initialization.
        """
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_save_updates_updated_at(self):
        """
        Test if the save method updates the updated_at attribute.
        """
        obj = BaseModel()
        original_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(original_updated_at, obj.updated_at)

    def test_to_dict(self):
        """
        Test if the to_dict method correctly converts
        the BaseModel instance to a dictionary.
        """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_str_representation(self):
        """
        Test if the string representation of the BaseModel
        instance is correctly formatted.
        """
        obj = BaseModel()
        obj_str = str(obj)
        self.assertIsInstance(obj_str, str)
        self.assertIn('[BaseModel]', obj_str)
        self.assertIn(obj.id, obj_str)


if __name__ == '__main__':
    unittest.main()
