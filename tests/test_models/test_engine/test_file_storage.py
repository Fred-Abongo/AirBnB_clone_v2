#!/usr/bin/python3
"""
Contains the TestFileStorageDocs classes
"""

from datetime import datetime
import inspect
import models
from models.engine import file_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
FileStorage = file_storage.FileStorage
classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class TestFileStorageDocs(unittest.TestCase):
    """Verify the documentation and style of FileStorage class"""
    @classmethod
    def setUpClass(cls):
        """Establishes the groundwork for documentation tests"""
        cls.fs_f = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pep8_conformance_file_storage(self):
        """Validate models/engine/file_storage.py against PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Detected code style errors and warnings.")

    def test_pep8_conformance_test_file_storage(self):
        """Check tests/test_models/test_engine/test_file_storage.py PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Detected code style errors and warnings.")

    def test_file_storage_module_docstring(self):
        """Ensure file_storage.py has a module docstring"""
        self.assertIsNot(file_storage.__doc__, None,
                         "file_storage.py requires a docstring")
        self.assertTrue(len(file_storage.__doc__) >= 1,
                        "file_storage.py requires a docstring")

    def test_file_storage_class_docstring(self):
        """Examine the FileStorage class for a docstring"""
        self.assertIsNot(FileStorage.__doc__, None,
                         "FileStorage class must have a docstring")
        self.assertTrue(len(FileStorage.__doc__) >= 1,
                        "FileStorage class must have a docstring")

    def test_fs_func_docstrings(self):
        """Verify presence of docstrings in FileStorage methods"""
        for func in self.fs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method must have a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method must have a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Evaluate the FileStorage class"""
    @unittest.skipIf(models.storage_t == 'db', "Not testing file storage")
    def test_all_returns_dict(self):
        """Confirm all returns the FileStorage.__objects attribute"""
        storage = FileStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, storage._FileStorage__objects)

    @unittest.skipIf(models.storage_t == 'db', "Not testing file storage")
    def test_new(self):
        """Validate that new adds an object to the FileStorage.__objects attribute"""
        storage = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, storage._FileStorage__objects)
        FileStorage._FileStorage__objects = save

    @unittest.skipIf(models.storage_t == 'db', "Not testing file storage")
    def test_save(self):
        """Verify that save correctly saves objects to file.json"""
        storage = FileStorage()
        new_dict = {}
        for key, value in classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            new_dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))
