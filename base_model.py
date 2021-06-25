#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
#from models.base_model import BaseModel

class BaseModel:

    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key in kwargs.keys():
                if key == "created_at":
                    self.created_at = datetime.strptime(
                        kwargs[key], time_format)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(
                        kwargs[key], time_format)
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return str("[{}] ({}) {}".format(
            type(self).__name__, self.id, str(self.__dict__)))

    def save(self):
        self.updated_at = datetime.datetime.now

    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
