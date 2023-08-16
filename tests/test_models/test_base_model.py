#!/usr/bin/python3

"""
Test class for base model class
"""
import sys
import unittest
import inspect
import io
import pep8
from datetime import datetime
import uuid
from contextlib import redirect_stdout
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    class for testing BaseModel class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(BaseModel, inspect.isfunction)

    def setUp(self):
        """Set up method for object BM of BAseModel"""
        self.BM = BaseModel()

    def tearDown(self):
        """Set tmp object"""
        self.BM = None

    def test_pep8_conformance_BaseModel(self):
        """
        Test that base_model.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_BaseModel(self):
        """
        Test that test_base_model.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/\
                                        test_base_model.py'])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_type(self):
        """test method for type testing of BaseModel
        """
        self.assertIsInstance(self.BM, BaseModel)
        self.assertEqual(type(self.BM), BaseModel)
