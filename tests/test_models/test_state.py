#!/usr/bin/python3
"""
Test class for state class
"""
import sys
import unittest
import inspect
import io
import pep8
from datetime import datetime
from contextlib import redirect_stdout
from models.state import State


class TestState(unittest.TestCase):
    """
    class for testing State class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(State, inspect.isfunction)

    def test_pep8_conformance_State(self):
        """
        Test that state.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_state(self):
        """
        Test that test_state.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(State.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(State.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def setUp(self):
        """set up method for State class
        """
        self.S = State()

    def tearDown(self):
        """initialized method for State class
        """
        self.S = None

    def test_type(self):
        """test method for type testing of state
        """
        self.assertIsInstance(self.S, State)
        self.assertEqual(type(self.S), State)
        self.assertEqual(issubclass(self.S.__class__, State), True)
        self.assertEqual(isinstance(self.S, State), True)

    def test_name_type(self):
        """tests the type of state attribute
        """
        self.assertEqual(type(State.name), str)
