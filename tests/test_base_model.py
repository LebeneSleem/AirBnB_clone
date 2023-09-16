#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        del self.base_model

    def test_instance_creation(self):
        self.assertIsInstance(self.base_model, BaseModel)

    def test_id_generation(self):
        self.assertIsNotNone(self.base_model.id)

    def test_created_at_type(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_type(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_to_dict_method(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

if __name__ == '__main__':
    unittest.main()
