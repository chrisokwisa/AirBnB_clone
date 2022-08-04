#!/usr/bin/python3
"""This module defines the BaseModel"""


from models.base_model import BaseModel


class Place(BaseModel):
    """Represents the class amenity

    Attributes:
    city_id (str): It will be the city id
    user_id (str): It will be the user id
    name (str): name of the place
    description (str): description of the place
    number_rooms (int): number of the rooms
    number_bathrooms (int): number of bathrooms
    max_guest (int): integer
    price_by_night: integer
    latitude (f): float
    longitude: float
    amenity_ids (list): []
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
