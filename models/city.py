#!/usr/bin/python3
"""Module defines the BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Represents the class city

    Attributes:
    state_id (str): It will be the state id
    name (str): empty string
    """
    state_id = ""
    name = ""
