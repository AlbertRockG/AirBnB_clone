#!/usr/bin/python3
"""
Class to test filestorage class
"""
import sys
import unittest
import inspect
import io
import pep8
from datetime import datetime
from contextlib import redirect_stdout
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User


class TestFileStorage(unittest.TestCase):
    """
    class for testing FileStorage class' methods
    """
    temp_file = ""

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pep8_conformance_FileStorage(self):
        """
        Test that file_storage.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/file_storage.py'])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_FileStorage(self):
        """
        Test that test_file_storage.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/\
                                        test_file_storage.py'])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(FileStorage.__doc__) >= 1)
