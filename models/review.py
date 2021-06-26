#!/usr/bin/python3

""" Module that contains an empty class """

from models.base_model import BaseModel


class Review(BaseModel):
    """ Class called review """

    place_id = ""
    user_id = ""
    text = ""
