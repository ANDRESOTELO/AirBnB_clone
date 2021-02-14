#!/usr/bin/python3
"""
FileStorage serializes instances to a JSON file and deserializes JSON file to instances
"""

import json
import models

class FileStorage:
    """
    This class serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    __file_path = ""
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
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """
        Public instance method that serializes __objects to the JSON file
        """
        FileStorage.__file_path = "file.json"
        json_string = json.dumps(FileStorage.__objects)
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json_string)

    def reload(self):
        """
        Public instance method deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                read_file = f.read()
                FileStorage.__objects = json.loads(read_file)
        except:
            pass
