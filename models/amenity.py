#!/usr/bin/python3
"""
Amemity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class inherits from BaseModel.

    Attribute:
        name (str): Public class attribute for Amenity's name.
    """
    name = ''
