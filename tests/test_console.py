#!/usr/bin/python3
"""
Defines the TestConsoleDocs class.
"""

import console
import inspect
import pep8
import unittest
HBNBCommand = console.HBNBCommand

class TestConsoleDocs(unittest.TestCase):
    """Verifies the documentation integrity of the console module."""
    def test_pep8_conformance_console(self):
        """Checks if console.py adheres to PEP8 standards."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style errors (and warnings) detected in console.py.")

    def test_pep8_conformance_test_console(self):
        """Checks if tests/test_console.py complies with PEP8 standards."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style errors (and warnings) detected in tests/test_console.py.")

    def test_console_module_docstring(self):
        """Ensures console.py has a valid module docstring."""
        self.assertIsNot(console.__doc__, None,
                         "A docstring is missing for console.py.")
        self.assertTrue(len(console.__doc__) >= 1,
                        "A docstring is missing for console.py.")

    def test_HBNBCommand_class_docstring(self):
        """Verifies the presence of a docstring for the HBNBCommand class."""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "A docstring is missing for the HBNBCommand class.")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "A docstring is missing for the HBNBCommand class.")
