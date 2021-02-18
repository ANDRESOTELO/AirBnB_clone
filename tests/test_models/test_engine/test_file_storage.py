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
from models.user import User
import os


class TestFileStorage(unittest.TestCase):
    """
    Define TestFileStorage class
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

    def test_storage(self):
        """
        Test that checks if storage is instance of FileStorage
        """
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

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
        mymodel = BaseModel()
        all_obj = storage.all()
        key = "{}.{}".format(mymodel.__class__.__name__, mymodel.id)
        self.assertEqual(all_obj[key], mymodel)

    def test_new(self):
        """
        Testing the new method
        """
        my_model = BaseModel()
        my_model.save()
        all_objs = storage.all()
        obj_key = my_model.__class__.__name__ + '.' + my_model.id
        self.assertEqual(all_objs[obj_key], my_model)
        self.assertEqual(obj_key in all_objs, True)
        obj = {obj_key: my_model}
        self.assertEqual(obj, all_objs)

    def test_User_ins(self):
        """
        Testing the User instance
        """
        my_model = User()
        my_model.save()
        all_objs = storage.all()
        obj_key = my_model.__class__.__name__ + '.' + my_model.id
        self.assertEqual(all_objs[obj_key], my_model)
        self.assertEqual(obj_key in all_objs, True)
        obj = {obj_key: my_model}
        self.assertEqual(obj, all_objs)

    def test_file_json(self):
        """
        Test for check file.json
        """
        my_model = BaseModel()
        my_model.save()
        here = os.path.exists('file.json')
        self.assertEqual(here, True)

    def test_save_method(self):
        """
        Test that checks save method
        """
        filename = "file.json"
        my_model = BaseModel()
        key = "{}.{}".format(my_model.__class__.__name__, my_model.id)
        storage.new(my_model)
        storage.save()
        self.assertTrue(os.path.exists(filename))
        with open(filename) as f:
            obj = json.load(f)
            self.assertEqual(my_model.id, obj[key]["id"])
            self.assertEqual(my_model.__class__.__name__,
                             obj[key]["__class__"])
        FileStorage._FileStorage__objects = {}
        storage.reload()
        all_obj = storage.all()
        self.assertEqual(my_model.id, all_obj[key].id)
        self.assertEqual(my_model.__class__, all_obj[key].__class__)
        self.assertEqual(my_model.created_at, all_obj[key].created_at)
        self.assertEqual(my_model.updated_at, all_obj[key].updated_at)

    def test_file_empty(self):
        """
        Test for file.json not empty
        """
        my_model = BaseModel()
        my_model.save()
        file_path = 'file.json'
        file_size = os.stat(file_path).st_size
        self.assertNotEqual(file_size, 0)

    def test_file_json(self):
        """
        Test fon info inside file.json
        """
        my_model = BaseModel()
        my_model.save()
        json_object = storage.all()

    def tearDown(self):
        """
        Method to reset test and remove file.json
        """
        FileStorage._FileStorage__objects = {}
        try:
            delete("file.json")
        except:
            pass

    def test_kwargs(self):
        """
        Test to check reload function
        """
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertIsNot(my_model, my_new_model)
