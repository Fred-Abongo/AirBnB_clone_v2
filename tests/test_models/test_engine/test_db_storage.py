#!/usr/bin/python3
"""
Houses the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
import os
import pep8
import unittest
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
DBStorage = db_storage.DBStorage


class TestDBStorageDocs(unittest.TestCase):
    """Tests to verify the documentation and style of the DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Initial setup for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Validates conformity of models/engine/db_storage.py with PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Encountered code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Checks conformity of tests/test_models/test_engine/
        test_db_storage.py with PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Encountered code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Ensures existence of docstring for db_storage.py module"""
        self.assertIsNot(db_storage.__doc__, None,
                         "Missing docstring for db_storage.py")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "Docstring for db_storage.py should not be empty")

    def test_db_storage_class_docstring(self):
        """Ensures existence of docstring for the DBStorage class"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "Missing docstring for DBStorage class")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "Docstring for DBStorage class should not be empty")

    def test_dbs_func_docstrings(self):
        """Checks presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            with self.subTest(function=func):
                self.assertIsNot(func[1].__doc__, None,
                                 "{:s} method lacks a docstring".format(func[0]))
                self.assertTrue(len(func[1].__doc__) >= 1,
                                "{:s} method docstring should not be empty".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "Not testing db storage")
    def test_all_returns_dict(self):
        """Verifies that all returns a dictionary"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "Not testing db storage")
    def test_all_no_class(self):
        """Checks if all returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "Not testing db storage")
    def test_new(self):
        """Validates that new adds an object to the database"""

    @unittest.skipIf(models.storage_t != 'db', "Not testing db storage")
    def test_save(self):
        """Confirms that save correctly saves objects to file.json"""
