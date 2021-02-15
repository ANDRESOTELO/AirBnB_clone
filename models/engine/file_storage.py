#!/usr/bin/python3
"""
FileStorage serializes instances to a JSON file and deserializes JSON file to instances
"""

import json
import models
from models.base_model import BaseModel

class FileStorage:
    """
    This class serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Public instance method that returns the dictionary __objects
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        Public instance method that sets in __objects the obj with the
        key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__ , obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Public instance method that serializes __objects to the JSON file
        """
        filename = FileStorage.__file_path
        dictionary = {}
        for key, value in FileStorage.__objects.items():
            val = value.to_dict()
            dictionary[key] = val
        with open(filename, 'w') as json_file:
            json.dump(dictionary, json_file)

    def reload(self):
        """
        Public instance method deserializes the JSON file to __objects
        """
        filename = FileStorage.__file_path
        try:
            with open(filename, 'r') as f:
                read_file = json.load(f)
                for key, value in read_file.items():
                    FileStorage.__objects[key] = eval(value["__class__"])(**value)
        except Exception:
            pass
