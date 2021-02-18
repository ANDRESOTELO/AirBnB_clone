#!/usr/bin/python3
"""
Unittest for Place module
"""

import unittest
import inspect
from models import place
from models.base_model import BaseModel
import os
from datetime import datetime
from models.engine.file_storage import FileStorage
import pep8
Place = place.Place


class TestPlace(unittest.TestCase):
    """
    Define TestPlace class
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
        Test that checks pep8 implementation in test_place file
        """
        path = "tests/test_models/test_place.py"
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
        my_model = Place()
        self.assertIsInstance(my_model, BaseModel)

    def test_has_attrs(self):
        """
        Test that checks if object has attributes
        """
        my_model = Place()
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertTrue(hasattr(my_model, "created_at"))

    def test_city_id(self):
        """
        Test that checks if has attribute
        """
        my_model = Place()
        self.assertTrue(hasattr(my_model, "city_id"))
        self.assertEqual(my_model.city_id, "")

    def test_user_id(self):
        """
        Test that checks if has attribute
        """
        my_model = Place()
        self.assertTrue(hasattr(my_model, "user_id"))
        self.assertEqual(my_model.user_id, "")

    def test_name(self):
        """
        Test that checks if has attribute
        """
        my_model = Place()
        self.assertTrue(hasattr(my_model, "name"))
        self.assertEqual(my_model.name, "")

    def test_description(self):
        """
        Test that checks if has attribute
        """
        my_model = Place()
        self.assertTrue(hasattr(my_model, "description"))
        self.assertEqual(my_model.description, "")

    def test_number_rooms(self):
        """
        Test that checks if has attribute
        """
        my_model = Place()
        self.assertTrue(hasattr(my_model, "number_rooms"))
        self.assertEqual(my_model.number_rooms, 0)
        self.assertEqual(type(my_model.number_rooms), int)

    def test_number_bathrooms(self):
        """
        Test that checks if has attribute
        """
        my_model = Place()
        self.assertTrue(hasattr(my_model, "number_bathrooms"))
        self.assertEqual(my_model.number_bathrooms, 0)
        self.assertEqual(type(my_model.number_bathrooms), int)

    def test_max_guest(self):
        """
        Test that checks if has attribute
        """
        my_model = Place()
        self.assertTrue(hasattr(my_model, "max_guest"))
        self.assertEqual(my_model.max_guest, 0)
        self.assertEqual(type(my_model.max_guest), int)

    def test_price_by_night(self):
        """
        Test that checks if has attribute
        """
        my_model = Place()
        self.assertTrue(hasattr(my_model, "price_by_night"))
        self.assertEqual(my_model.price_by_night, 0)
        self.assertEqual(type(my_model.price_by_night), int)

    def test_latitude(self):
        """
        Test that checks if has attribute
        """
        my_model = Place()
        self.assertTrue(hasattr(my_model, "latitude"))
        self.assertEqual(my_model.latitude, 0.0)
        self.assertEqual(type(my_model.latitude), float)

    def test_longitude(self):
        """
        Test that checks if has attribute
        """
        my_model = Place()
        self.assertTrue(hasattr(my_model, "longitude"))
        self.assertEqual(my_model.longitude, 0.0)
        self.assertEqual(type(my_model.longitude), float)

    def test_amenity_ids(self):
        """
        Test that checks if has attribute
        """
        my_model = Place()
        self.assertTrue(hasattr(my_model, "amenity_ids"))
        self.assertEqual(my_model.amenity_ids, [])

    def test_str_method(self):
        """
        Test str method
        """
        my_model = Place()
        str_format = "[{}] ({}) {}".format(my_model.__class__.__name__,
                                           my_model.id, my_model.__dict__)
        self.assertEqual(str_format, str(my_model))

    def test_to_dict(self):
        """
        Test that checks if dict model to json is created
        """
        my_model = Place()
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
