#!/usr/bin/python3
from models.base_model import BaseModel

"""review module"""


class Review(BaseModel):
    """review class"""
    
    place_id = ""
    user_id = ""
    text = ""