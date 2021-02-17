#!/usr/bin/python3
"""
Unittest for base_model.py module
"""

from os import remove as delete
import models
from models.base_model import BaseModel
import unittest
import pep8
import inspect
from models.base_model import BaseModel, __doc__
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Define TestBaseModel class
    """
    def setUp(self):
        """
        Method to init test and remove file.json
        """
        try:
            delete("file.json")
        except:
            pass

    def test_pep8_BaseModel(self):
        """
        Test that checks pep8 implementation
        """
        style = pep8.StyleGuide(quiet=True)
        check = style.check_files(['models/base_model.py'])
        self.assertEqual(check.total_errors, 0,
                         "PEP8 style errors: {:d}".format(check.total_errors))

    def test_pep8_test_BaseModel(self):
        """
        Test that checks pep8 implementation in test_base file
        """
        style = pep8.StyleGuide(quiet=True)
        check = style.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(check.total_errors, 0,
                         "PEP8 style errors: {:d}".format(check.total_errors))

    def test_doc_string(self):
        """
        Test docstring
        """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_create_instance(self):
        """
        Test that checks correct creation of instance
        checking correct id instance and specific id too.
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel,
                              "Object isn´t an instance of class")

    def test_model_json(self):
        """
        Test that checks if method to_dict creates a dictionary
        """
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.save()
        my_model_json = my_model.to_dict()
        self.assertTrue(type(my_model_json), "<class 'dict'>")

    def test_save_method(self):
        """
        Test that save method updates the updated_at variable
        """
        my_model = BaseModel()
        up1 = my_model.updated_at
        my_model.name = "Holberton"
        my_model.save()
        up2 = my_model.updated_at
        self.assertNotEqual(up1, up2)

    def test_uuid(self):
        """
        Test that checks if two instances have different id
        """
        my_model = BaseModel()
        my_model_id = my_model.id
        my_new_model = BaseModel()
        my_new_model_id = my_new_model.id
        self.assertNotEqual(my_model_id, my_new_model_id)

    def test_attributes(self):
        """
        Test that checks correct set value
        """
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.number = 89
        self.assertEqual(my_model.name, "Holberton")
        self.assertEqual(my_model.number, 89)

    def test_str(self):
        """
        Test that __str__ have correct output
        """
        my_model = BaseModel()
        str_format = "[BaseModel] ({}) {}".format(my_model.id,
                                                  my_model.__dict__)
        self.assertEqual(str_format, str(my_model))

    def test_instance(self):
        """
        Test correct instance
        """
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.number = 89
        self.assertEqual(my_model.__class__.__name__, "BaseModel")
        self.assertEqual(type(my_model), BaseModel)
        self.assertEqual(my_model.name, "Holberton")
        self.assertEqual(my_model.number, 89)

    def test_check_datetime(self):
        """
        doce
        """
        my_model = BaseModel()
        datetime_class = "<class 'datetime.datetime'>"
        self.assertTrue(type(my_model.created_at), datetime_class)
        self.assertTrue(type(my_model.updated_at), datetime_class)
        self.assertTrue(type(my_model.id), "<class 'str'>")


if __name__ == "__main__":
    """
    Entry point
    """
    unittest.main()
