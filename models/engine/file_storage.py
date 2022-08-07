#!/usr/bin/python3
"""file storage module"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:

    """class that serializes instances to a JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""

        return type(self).__objects

    def new(self, obj):
        """sets object in objects"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """serialize objects to json files"""

        temp = {}
        for k, v in type(self).__objects.items():
            temp[k] = v.to_dict()
        with open(type(self).__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(temp) + "\n")

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist"""
        clslist = {'BaseModel': BaseModel, 'State': State, 'City': City,
                   'Amenity': Amenity, 'Place': Place, 'Review': Review,
                   'User': User}
        try:
            with open(type(self).__file_path, 'r', encoding='utf-8') as f:
                temp = json.load(f)
                for k, v in temp.items():
                    self.new(clslist[v['__class__']](**v))
        except FileNotFoundError:
            pass
