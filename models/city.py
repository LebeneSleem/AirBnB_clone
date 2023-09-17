#!/usr/bin/python3
"""A class City that inherits from the BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Manages the city attributes"""
    state_id = ""
    name = ""
