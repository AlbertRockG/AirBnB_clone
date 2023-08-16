#!/usr/bin/python3
"""
Test class for review class
"""
import sys
import unittest
import inspect
import io
import pep8
from datetime import datetime
from contextlib import redirect_stdout
from models.review import Review


class TestReview(unittest.TestCase):
    """
    class for testing Review class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Review, inspect.isfunction)

    def test_pep8_conformance_Review(self):
        """
        Test that review.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_Review(self):
        """
        Test that test_review.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Review.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Review.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def setUp(self):
        self.R = Review()

    def tearDown(self):
        self.R = None

    def test_type(self):
        """test method for type testing of review
        """
        self.assertIsInstance(self.R, Review)
        self.assertEqual(type(self.R), Review)
        self.assertEqual(issubclass(self.R.__class__, Review), True)
        self.assertEqual(isinstance(self.R, Review), True)

    def test_place_id_type(self):
        """tests the place_id class attribute type of Review
        """
        self.assertEqual(type(Review.place_id), str)

    def test_user_id_type(self):
        """tests the user_id class attribute type of Review
        """
        self.assertEqual(type(Review.user_id), str)

    def test_text_type(self):
        """tests the text class attribute type of Review
        """
        self.assertEqual(type(Review.text), str)
