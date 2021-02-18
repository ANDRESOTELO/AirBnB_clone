#!/usr/bin/python3
"""
Unittest for file_storage module
"""

import unittest
import inspect
from models import user
from models.base_model import BaseModel
import os
from datetime import datetime
from models.engine.file_storage import FileStorage
import pep8
User = user.User


class TestUser(unittest.TestCase):
    """
    Define TestUser class
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
        Test that checks pep8 implementation in test_user file
        """
        path = "tests/test_models/test_user.py"
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
        my_model = User()
        self.assertIsInstance(my_model, BaseModel)

    def test_has_attrs(self):
        """
        Test that checks if object has attributes
        """
        my_model = User()
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertTrue(hasattr(my_model, "created_at"))

    def test_email(self):
        """
        Test that checks if has attribute
        """
        my_model = User()
        self.assertTrue(hasattr(my_model, "email"))
        self.assertEqual(my_model.email, "")

    def test_password(self):
        """
        Test that checks if has attribute
        """
        my_model = User()
        self.assertTrue(hasattr(my_model, "password"))
        self.assertEqual(my_model.password, "")

    def test_firs_name(self):
        """
        Test that checks if has attribute
        """
        my_model = User()
        self.assertTrue(hasattr(my_model, "first_name"))
        self.assertEqual(my_model.first_name, "")

    def test_last_name(self):
        """
        Test that checks if has attribute
        """
        my_model = User()
        self.assertTrue(hasattr(my_model, "last_name"))
        self.assertEqual(my_model.last_name, "")

    def test_str_method(self):
        """
        Test str method
        """
        my_model = User()
        str_format = "[{}] ({}) {}".format(my_model.__class__.__name__,
                                           my_model.id, my_model.__dict__)
        self.assertEqual(str_format, str(my_model))

    def test_to_dict(self):
        """
        Test that checks if dict model to json is created
        """
        my_model = User()
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
