#!/usr/bin/python3
"""
Defines the TestUserDocs class and related tests.
"""

from datetime import datetime
import inspect
import models
from models import user
from models.base_model import BaseModel
import pep8
import unittest
User = user.User

class TestUserDocs(unittest.TestCase):
    """Verifies the documentation integrity and style of the User class."""
    @classmethod
    def setUpClass(cls):
        """Sets up the test environment."""
        cls.user_f = inspect.getmembers(User, inspect.isfunction)

    def test_pep8_conformance_user(self):
        """Checks if models/user.py conforms to PEP8 standards."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style errors (and warnings) detected in models/user.py.")

    def test_pep8_conformance_test_user(self):
        """Checks if tests/test_models/test_user.py complies with PEP8 standards."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style errors (and warnings) detected in tests/test_models/test_user.py.")

    def test_user_module_docstring(self):
        """Ensures user.py has a valid module docstring."""
        self.assertIsNot(user.__doc__, None,
                         "A docstring is missing for user.py.")
        self.assertTrue(len(user.__doc__) >= 1,
                        "A docstring is missing for user.py.")

    def test_user_class_docstring(self):
        """Ensures the User class has a valid docstring."""
        self.assertIsNot(User.__doc__, None,
                         "A docstring is missing for the User class.")
        self.assertTrue(len(User.__doc__) >= 1,
                        "A docstring is missing for the User class.")

    def test_user_func_docstrings(self):
        """Verifies the presence of docstrings in User methods."""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

class TestUser(unittest.TestCase):
    """Tests the functionality of the User class."""
    def test_is_subclass(self):
        """Checks if User is a subclass of BaseModel."""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_email_attr(self):
        """Checks if User has the 'email' attribute, and it's initialized properly."""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        if models.storage_t == 'db':
            self.assertEqual(user.email, None)
        else:
            self.assertEqual(user.email, "")

    def test_password_attr(self):
        """Checks if User has the 'password' attribute, and it's initialized properly."""
        user = User()
        self.assertTrue(hasattr(user, "password"))
        if models.storage_t == 'db':
            self.assertEqual(user.password, None)
        else:
            self.assertEqual(user.password, "")

    def test_first_name_attr(self):
        """Checks if User has the 'first_name' attribute, and it's initialized properly."""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        if models.storage_t == 'db':
            self.assertEqual(user.first_name, None)
        else:
            self.assertEqual(user.first_name, "")

    def test_last_name_attr(self):
        """Checks if User has the 'last_name' attribute, and it's initialized properly."""
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        if models.storage_t == 'db':
            self.assertEqual(user.last_name, None)
        else:
            self.assertEqual(user.last_name, "")

    def test_to_dict_creates_dict(self):
        """Checks if the to_dict method creates a dictionary with the proper attributes."""
        u = User()
        new_d = u.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in u.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """Checks if the values in the dictionary returned from to_dict are correct."""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = User()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "User")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """Checks if the str method has the correct output."""
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))
