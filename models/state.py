#!/usr/bin/python3
"""
Module to create a new class
"""

import models
from models.base_model import BaseModel

class State(BaseModel):
    """ 
    Class State that inherits from BaseModel
    """
    name = ""
