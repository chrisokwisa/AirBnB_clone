#!/usr/bin/python3
"""Defines the BaseModel module"""

from models.base_models import BaseModel


class Review(BaseModel):
    """Represents the class review

    Attributes:
    place_id (str): the place_id
    user_id (str): the user id
    text (str): empty string
    """
    place_id = ""
    user_id = ""
    text = ""
