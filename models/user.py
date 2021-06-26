#!/usr/bin/python3

""" Module that contains an empty class """

from models.base_model import BaseModel


class User(BaseModel):
    """ Class called user """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
