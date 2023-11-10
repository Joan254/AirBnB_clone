#!/usr/bin/python3
"""
   Defining a filestorage class that serializes
   instances to a json file and deserialises
   json file to instances
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage:
    """
        The file storage engine class, that is;
        A class that serialize and deserialise intances to a JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w") as file:
            json.dump(
                    {k: v.to_dict() for k, v in FileStorage.__objects.items()},
                    file)

    def reload(self):
        """Deserializes the JSON file to __objects if it exists"""
        class_dict = {'BaseModel': BaseModel, 'User': User,
                      'Amenity': Amenity, 'City': City, 'State': State,
                      'Place': Place, 'Review': Review}

        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r') as file:
            deserialized = None

            try:
                deserialized = json.load(file)
            except json.JSONDecodeError:
                pass

            if deserialized is None:
                return

            if not isinstance(deserialized, dict):
                return

            FileStorage.__objects = {
                k: class_dict[k.split('.')[0]](**v)
                for k, v in deserialized.items()}
