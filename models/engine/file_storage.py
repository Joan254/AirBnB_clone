#!/usr/bin/python3
"""
   Defining a filestorage class that serializes
   instances to a json file and deserialises 
   json file to instances
"""


import json
import os
from models.base_model import BaseModel

class_dict = {
        "BaseModel": BaseModel
        }


class FileStorage:
    """
        The file storage engine class, that is;
        A class that serialize and deserialise intances to a JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects"""
        return type(self).__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary."""
        if obj.id in type(self).__objects:
            print("exists")
            return
        key = "{}.{}".format(obj.__class__.__name__,obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = []
        for obj in type(self).__objects.values():
            new_dict.append(obj.to_dict())
        with open(type(self).__file_path, "w", encoding='UTF-8') as file:
            json.dump(new_dict,file)

    def reload(self):
        """Deserializes the JSON file to __objects if it exists"""
        if os.path.exists(type(self).__file_path) is True:
            return
            try:
                with open(type(self).__file_path, "r") as file:
                    new_obj = json.load(file)
                    for key, val in new_obj.items():
                        obj = self.class_dict[val['__class__']](**val)
                        type(self).__objects[key] = obj
            except Exception:
                pass
