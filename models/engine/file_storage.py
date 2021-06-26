#!/usr/bin/python3

""" Module for the class FileStorage to save files in a json format """

import json


class FileStorage:
    """ Class for json serialization and deseralization of other classes """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return the __object dictionary """
        return FileStorage.__objects

    def new(self, obj):
        """ sets a new object into the __objects attribute """
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serialize the __objects into a json file """
        save_to = {}
        for key, value in FileStorage.__objects.items():
            save_to[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as my_file:
            json.dump(save_to, my_file)

    def reload(self):
        """ Deserializes JSON file and store them into __objects """
        try:
            with open(FileStorage.__file_path) as read_f:
                from models.base_model import BaseModel
                from models.user import User
                from models.city import City
                from models.amenity import Amenity
                from models.place import Place
                from models.review import Review
                from models.state import State

                json_var = json.load(read_f)
                for key, value in json_var.item():
                    class_var = value["__clas__"]
                    object_var = eval(class_var + "(**value)")
                    FileStorage.__objects[key] = object_var
        except FileNotFoundError:
            pass
