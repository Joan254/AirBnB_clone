#!/usr/bin/python3
import uuid
from datetime import datetime
import models
"""Defining a base class for the whole project"""


class BaseModel():
    """This it the base that defines all common atributes for other clases"""
    def __init__(self, *args, **kwargs):
        """Initializing an object with these instance attribute
           Args:
               self.id (int) : The unique id of the instance
               current_time : Generates the time
               self.created_time: Time created
               self.updated_time: The upated time
        """
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if "created_at" == key or "updated_at" == key:
                    self.__dict__[key] = datetime.strptime(value, date_format)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            current_time = datetime.now()
            self.created_at = current_time
            self.updated_at = current_time
            models.storage.new(self)

    def save(self):
        """A public instance method to update the update_at
        with the current time.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """Custom string representation:
        should print [<class name>] (<self.id>) <self.__dict__>
        """
        clsName = self.__class__.__name__
        return "[{}] ({}) {}".format(clsName, self.id, self.__dict__)
