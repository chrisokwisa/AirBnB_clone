#!/usr/bin/python3
"""This module defines the BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """This module represents the class user

    Attributes:
    email (str) = email of the user
    password (str) = Password of the user
    first_name (str)= first name of the user
    last_name (str) = last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
