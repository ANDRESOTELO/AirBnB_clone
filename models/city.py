#!/usr/bin/python3
"""
Module to create a new class
"""

import models
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class City that inherits from BaseModel
    """
    state_id = ""
    name = ""
