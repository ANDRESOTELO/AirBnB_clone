#!/usr/bin/python3
"""
Unittest for file_storage module
"""

from os import remove as delete
import models
import json
import uuid
from models import storage
from models.base_model import BaseModel
import unittest
import pep8
import inspect
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Define TestFileStorage class
    """
    def setUp(self):
        """
        Method to init test and remove file.json
        """
        try:
            delete("file.json")
        except:
            pass

    def test_pep8_FileStorage(self):
        """
        Test that checks pep8 implementation
        """
        style = pep8.StyleGuide(quiet=True)
        check = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(check.total_errors, 0,
                         "PEP8 style errors: {:d}".format(check.total_errors))

    def test_pep8_test_FileStorage(self):
        """
        Test that checks pep8 implementation in test_base file
        """
        path = "tests/test_models/test_engine/test_file_storage.py"
        style = pep8.StyleGuide(quiet=True)
        check = style.check_files([path])
        self.assertEqual(check.total_errors, 0,
                         "PEP8 style errors: {:d}".format(check.total_errors))

    def test_doc_string(self):
        """
        Test docstring
        """
        self.assertIsNotNone(FileStorage.__doc__)

    def test_all_method(self):
        """
        Test if storage all method works
        """
        all_objs = storage.all()
        self.assertEqual(all_objs, {})
        self.assertTrue(type(all_objs), "<class 'dict'>")

    def test_reload_method(self):
        """
        Test reload method
        """
        all_objs = storage.all()
        storage.reload()
        self.assertEqual(FileStorage._FileStorage__objects, {})

    def test_storage_instance(self):
        """
        Test instance creation
        """
        my_model = BaseModel()
        all_objs = storage.all()
        key = "{}.{}".format(my_model.__class__.__name__, my_model.id)
        for obj_id, obj_value in all_objs.items():
            self.assertEqual(obj_id, key)
            self.assertEqual(obj_value, my_model)

    def tearDown(self):
        """
        Method to reset test and remove file.json
        """
        try:
            delete("file.json")
        except:
            pass
