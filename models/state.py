#!/usr/bin/python3
"""This module defines the BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """Represents the class state

    Attributes:
    name(str): The name of the state
    """
    name = ""
