#!/usr/bin/python3
"""
Unittest for BaseModel class
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import time


class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class"""

    def test_id_is_string(self):
        """Test that id is a string"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_unique_id(self):
        """Test that two BaseModel instances have unique ids"""
        m1 = BaseModel()
        m2 = BaseModel()
        self.assertNotEqual(m1.id, m2.id)

    def test_datetime_attributes(self):
        """Test that created_at and updated_at are datetime objects"""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """Test that save() updates updated_at"""
        model = BaseModel()
        old_updated_at = model.updated_at
        time.sleep(0.001)  # ensure timestamp changes
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)
        self.assertGreater(model.updated_at, old_updated_at)

    def test_to_dict_returns_dict(self):
        """Test that to_dict() returns a dictionary with correct keys and types"""
        model = BaseModel()
        model.name = "Test"
        model.my_number = 42
        d = model.to_dict()

        self.assertIsInstance(d, dict)
        self.assertIn("id", d)
        self.assertIn("created_at", d)
        self.assertIn("updated_at", d)
        self.assertIn("__class__", d)
        self.assertEqual(d["__class__"], "BaseModel")

        # Check types of dictionary values
        self.assertIsInstance(d["id"], str)
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)
        self.assertIsInstance(d["name"], str)
        self.assertIsInstance(d["my_number"], int)

    def test_str_method(self):
        """Test that __str__ method returns expected string format"""
        model = BaseModel()
        string = str(model)
        self.assertIn("[BaseModel]", string)
        self.assertIn(model.id, string)
        self.assertIn("created_at", string)
        self.assertIn("updated_at", string)


if __name__ == "__main__":
    unittest.main()
