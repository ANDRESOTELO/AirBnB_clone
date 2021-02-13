#!/usr/bin/python3
"""
This is the base model module that defines all common attributes
and methods for the other classes
"""

from uuid import uuid4
from datetime import datetime


class BaseModel():
    """
    BaseModel class defines all common atributes/methods for other
    classes.
    """

    def __init__(self, id=None, created_at=None, updated_at=None):
        """
        Class constructor that have inits class attributes
        """

        # uuid4 create random UUID
        self.id = str(uuid4())
        # datetime.now() assign the actual date/time values
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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
