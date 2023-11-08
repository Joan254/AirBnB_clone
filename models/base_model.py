#!/usr/bin/python3
import uuid
from datetime import datetime
"""Defining a base class for the whole project"""


class BaseModel():
    """This it the base that defines all common atributes for other clases"""
    def __init__(self):
        """Initializing an object with these instance attribute
           Args:
               self.id (int) : The unique id of the instance
               current_time : Generates the time 
               self.created_time: Time created
               self.updated_time: The upated time
        """
        self.id = str(uuid.uuid4())

        current_time = datetime.now()
        self.created_at = current_time
        self.updated_at = current_time

    def save(self):
        """A public instance method to update the update_at with thecurrent time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """Custom string representation: should print [<class name>] (<self.id>) <self.__dict__>"""
        return f"[BaseModel] ({self.id}) {self.__dict__}"
