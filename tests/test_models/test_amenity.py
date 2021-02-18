#!/usr/bin/python3
"""
Unittest for amenity module
"""

import unittest
import inspect
from models import amenity
from models.base_model import BaseModel
import os
from datetime import datetime
from models.engine.file_storage import FileStorage
import pep8
Amenity = amenity.Amenity


class TestAmenity(unittest.TestCase):
    """
    Define TestAmenity state
    """
    def setUp(self):
        """
        Method to init test and remove file.json
        """
        FileStorage._FileStorage__objects = {}
        try:
            delete("file.json")
        except:
            pass

    def test_pep8(self):
        """
        Test that checks pep8 implementation in test_amenity file
        """
        path = "tests/test_models/test_amenity.py"
        style = pep8.StyleGuide(quiet=True)
        check = style.check_files([path])
        self.assertEqual(check.total_errors, 0,
                         "PEP8 style errors: {:d}".format(check.total_errors))

    def test_doc_string(self):
        """
        Test docstring
        """
        self.assertIsNotNone(FileStorage.__doc__)

    def test_subclass(self):
        """
        Test that checks if is subclass of BaseModel
        """
        my_model = Amenity()
        self.assertIsInstance(my_model, BaseModel)

    def test_has_attrs(self):
        """
        Test that checks if object has attributes
        """
        my_model = Amenity()
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertTrue(hasattr(my_model, "created_at"))

    def test_name(self):
        """
        Test that checks if has attribute
        """
        my_model = Amenity()
        self.assertTrue(hasattr(my_model, "name"))
        self.assertEqual(my_model.name, "")

    def test_str_method(self):
        """
        Test str method
        """
        my_model = Amenity()
        str_format = "[{}] ({}) {}".format(my_model.__class__.__name__,
                                           my_model.id, my_model.__dict__)
        self.assertEqual(str_format, str(my_model))

    def test_to_dict(self):
        """
        Test that checks if dict model to json is created
        """
        my_model = Amenity()
        my_model_json = my_model.to_dict()
        self.assertEqual("__class__" in my_model_json, True)

    def tearDown(self):
        """
        Method to reset test and remove file.json
        """
        FileStorage._FileStorage__objects = {}
        try:
            delete("file.json")
        except:
            pass
