#!/usr/bin/python3
"""This module creates a Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class that manages review"""

    place_id = ""
    user_id = ""
    text = ""
