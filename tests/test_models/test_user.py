#!/usr/bin/python3
"""
    Test User
"""
import unittest
from models.user import User


class TestUser(unittest, TestCase):
    """ Test """

    def test_User(self):
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
