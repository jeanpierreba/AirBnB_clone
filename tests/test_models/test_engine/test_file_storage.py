#!/usr/bin/python3
"""
    Test file storage
"""

import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest, TestCase):
    """ Test """

    def test_storage(self):
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
