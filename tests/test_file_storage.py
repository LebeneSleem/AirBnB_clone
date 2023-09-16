#!/usr/bin/python3

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage(models={})

    def tearDown(self):
        del self.storage

    def test_all_method(self):
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_method(self):
        base_model = BaseModel()
        self.storage.new(base_model)
        obj_key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.assertIn(obj_key, self.storage.all())

    def test_save_and_reload(self):
        base_model = BaseModel()
        self.storage.new(base_model)
        obj_key = "{}.{}".format(base_model.__class__.__name__, base_model.id)

        # Save data to a temporary file
        self.storage.save()

        # Create a new storage instance and reload data
        new_storage = FileStorage(models={})
        new_storage.reload()

        # Check if the object is reloaded correctly
        self.assertIn(obj_key, new_storage.all())

if __name__ == '__main__':
    unittest.main()

