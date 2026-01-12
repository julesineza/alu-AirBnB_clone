#!/usr/bin/python3
"""
Unit tests for BaseModel class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import time


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def test_instance_creation(self):
        """Test that a new instance is created properly"""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_unique_id(self):
        """Test that each instance has a unique id"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_str_representation(self):
        """Test __str__ method"""
        model = BaseModel()
        string = str(model)
        self.assertIn("[BaseModel]", string)
        self.assertIn(model.id, string)

    def test_save_method(self):
        """Test that save method updates updated_at"""
        model = BaseModel()
        old_updated_at = model.updated_at
        time.sleep(0.01)
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)
        self.assertGreater(model.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Test to_dict method"""
        model = BaseModel()
        model.name = "Test"
        model.number = 42
        model_dict = model.to_dict()
        
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertEqual(model_dict['name'], 'Test')
        self.assertEqual(model_dict['number'], 42)

    def test_to_dict_datetime_format(self):
        """Test that datetime is properly formatted in to_dict"""
        model = BaseModel()
        model_dict = model.to_dict()
        created_at = datetime.strptime(model_dict['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
        self.assertIsInstance(created_at, datetime)

    def test_kwargs_initialization(self):
        """Test initialization with kwargs"""
        model = BaseModel()
        model.name = "Test"
        model.number = 42
        model_dict = model.to_dict()
        
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, model.id)
        self.assertEqual(new_model.created_at, model.created_at)
        self.assertEqual(new_model.updated_at, model.updated_at)
        self.assertEqual(new_model.name, model.name)
        self.assertEqual(new_model.number, model.number)
        self.assertIsNot(new_model, model)

    def test_kwargs_datetime_conversion(self):
        """Test that datetime strings are converted to datetime objects"""
        model = BaseModel()
        model_dict = model.to_dict()
        new_model = BaseModel(**model_dict)
        
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)

    def test_kwargs_ignores_class(self):
        """Test that __class__ key in kwargs is ignored"""
        model_dict = {
            'id': 'test-id',
            'created_at': '2023-01-01T00:00:00.000000',
            'updated_at': '2023-01-01T00:00:00.000000',
            '__class__': 'SomeOtherClass'
        }
        model = BaseModel(**model_dict)
        self.assertEqual(model.__class__.__name__, 'BaseModel')


if __name__ == '__main__':
    unittest.main()