#!/usr/bin/python3
"""
This is the base model module that defines all common attributes
and methods for the other classes
"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel class defines all common atributes/methods for other
    classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Class constructor that have inits class attributes
        """

        # if kwargs is not empty assign key like attribute name
        # and each value like a value of this attribute name
        if kwargs:
            for key in kwargs:
                if key == "created_at" or key == "updated_at":
                    obj_format = "%Y-%m-%dT%H:%M:%S.%f"
                    # strptime creates a datetime object from a string
                    # kwargs[key] will be an object and will be set in the key
                    kwargs[key] = datetime.strptime(kwargs[key], obj_format)
                    # setattr sets the value of the specified attribute
                    setattr(self, key, kwargs[key])
                if key != "__class__":
                    setattr(self, key, kwargs[key])
        # if kwargs is empty create instance like a new instance
        # with new id and new created and updated variables
        else:
            # uuid4 create random UUID
            self.id = str(uuid4())
            # datetime.now() assign the actual date/time values
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Method that override the __str__ method and
        returns specific text format
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Method that updates the public instance attribute updated_at with the
        current datetime
        """
        
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
        return (self.updated_at)

    def to_dict(self):
        """
        Method that returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        # __dict__ contains all the attributes defined for the object itself
        # first create a copy of __dict__ and then modify values of the keys
        # isoformat() change the datatime format
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["created_at"] = self.created_at.isoformat()
        return dictionary
