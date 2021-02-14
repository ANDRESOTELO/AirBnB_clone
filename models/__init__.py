#!/usr/bin/python3
"""
Create a unique FileStorage instance for your application
"""

import models
from . import engine
from . import base_model

storage = engine.file_storage.FileStorage()
storage.reload()
