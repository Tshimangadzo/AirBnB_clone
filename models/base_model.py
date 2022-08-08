#!/usr/bin/python3
""" baseModel class module"""

import uuid
import models
from datetime import datetime

class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """ initializing our class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                     value = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                self.__setattr__(key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            

    def __str__(self) -> str:
        """string representation of the class"""

        return "[{}] ({}) {}".format(self.__class__.__name__,self.id,self.__dict__)
    
    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()
        

    def to_dict(self):
        """ dictionery representation of the object"""
        instance_info = self.__dict__.copy()
        instance_info["__class__"] = self.__class__.__name__
        instance_info["created_at"] = self.created_at.isoformat()
        instance_info["updated_at"] = self.updated_at.isoformat()
        return instance_info
    
base = BaseModel()
print(base)