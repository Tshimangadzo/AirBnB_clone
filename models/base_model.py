#!/usr/bin/python3
""" baseModel class documentation"""

import uuid
from datetime import datetime

class BaseModel:

    def __init__(self):
        """ init documentation"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()


    def __str__(self) -> str:
        """str documentation"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance"""
        intsance_info = self.__dict__
        intsance_info["__class__"] = self.__class__.__name__
        return intsance_info
