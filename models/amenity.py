#!/usr/bin/python3
"""
Module to create a new class
"""

import models
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class Amenity that inherits from BaseModel
    """
    name = ""
