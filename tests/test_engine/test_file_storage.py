#!/usr/bin/python3
"""
Unit tests for FileStorage class
"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        # Clear any existing file
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Clean up test environment"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all_method(self):
        """Test that all() returns the __objects dictionary"""
        result = self.storage.all()
        self.assertIsInstance(result, dict)

    def test_new_method(self):
        """Test that new() adds object to __objects"""
        model = BaseModel()
        self.storage.new(model)
        key = "BaseModel.{}".format(model.id)
        self.assertIn(key, self.storage.all())

    def test_save_method(self):
        """Test that save() creates a JSON file"""
        model = BaseModel()
        model.name = "Test"
        self.storage.new(model)
        self.storage.save()
        
        self.assertTrue(os.path.exists("file.json"))
        
        with open("file.json", 'r') as f:
            data = json.load(f)
            key = "BaseModel.{}".format(model.id)
            self.assertIn(key, data)

    def test_reload_method(self):
        """Test that reload() loads objects from JSON file"""
        model = BaseModel()
        model.name = "Test"
        self.storage.new(model)
        self.storage.save()
        
        # Create new storage instance
        new_storage = FileStorage()
        new_storage.reload()
        
        key = "BaseModel.{}".format(model.id)
        self.assertIn(key, new_storage.all())
        reloaded_model = new_storage.all()[key]
        self.assertEqual(reloaded_model.id, model.id)
        self.assertEqual(reloaded_model.name, model.name)

    def test_reload_no_file(self):
        """Test that reload() doesn't raise error if file doesn't exist"""
        try:
            new_storage = FileStorage()
            new_storage.reload()
        except Exception as e:
            self.fail("reload() raised exception: {}".format(e))


if __name__ == '__main__':
    unittest.main()