#!/usr/bin/python3
"""
Unittest for BaseModel class
"""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel"""

    def test_id(self):
        """Test that id exists and is a string"""
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))
        self.assertIsInstance(model.id, str)

    def test_created_at(self):
        """Test that created_at exists and is datetime"""
        model = BaseModel()
        self.assertTrue(hasattr(model, "created_at"))
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at(self):
        """Test that updated_at exists and is datetime"""
        model = BaseModel()
        self.assertTrue(hasattr(model, "updated_at"))
        self.assertIsInstance(model.updated_at, datetime)

    def test_save(self):
        """Test that save updates updated_at"""
        model = BaseModel()
        old_updated_at = model.updated_at
        time.sleep(0.001)
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)
        self.assertIsInstance(model.updated_at, datetime)

    def test_to_dict(self):
        """Test to_dict returns correct dictionary"""
        model = BaseModel()
        model.name = "Test"
        model.number = 10
        d = model.to_dict()

        self.assertIsInstance(d, dict)
        self.assertIn("__class__", d)
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertIn("id", d)
        self.assertIn("created_at", d)
        self.assertIn("updated_at", d)

        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)
        self.assertIsInstance(d["id"], str)

    def test_str(self):
        """Test __str__ output format"""
        model = BaseModel()
        string = str(model)

        self.assertIn("[BaseModel]", string)
        self.assertIn(model.id, string)
        self.assertIn(str(model.__dict__), string)


if __name__ == "__main__":
    unittest.main()
