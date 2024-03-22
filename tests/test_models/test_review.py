#!/usr/bin/python3
"""
Defines the TestReviewDocs class and related tests.
"""

from datetime import datetime
import inspect
import models
from models import review
from models.base_model import BaseModel
import pep8
import unittest
Review = review.Review

class TestReviewDocs(unittest.TestCase):
    """Verifies the documentation integrity and style of the Review class."""
    @classmethod
    def setUpClass(cls):
        """Sets up the test environment."""
        cls.review_f = inspect.getmembers(Review, inspect.isfunction)

    def test_pep8_conformance_review(self):
        """Checks if models/review.py conforms to PEP8 standards."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style errors (and warnings) detected in models/review.py.")

    def test_pep8_conformance_test_review(self):
        """Checks if tests/test_models/test_review.py complies with PEP8 standards."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style errors (and warnings) detected in tests/test_models/test_review.py.")

    def test_review_module_docstring(self):
        """Ensures review.py has a valid module docstring."""
        self.assertIsNot(review.__doc__, None,
                         "A docstring is missing for review.py.")
        self.assertTrue(len(review.__doc__) >= 1,
                        "A docstring is missing for review.py.")

    def test_review_class_docstring(self):
        """Ensures the Review class has a valid docstring."""
        self.assertIsNot(Review.__doc__, None,
                         "A docstring is missing for the Review class.")
        self.assertTrue(len(Review.__doc__) >= 1,
                        "A docstring is missing for the Review class.")

    def test_review_func_docstrings(self):
        """Verifies the presence of docstrings in Review methods."""
        for func in self.review_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

class TestReview(unittest.TestCase):
    """Tests the functionality of the Review class."""
    def test_is_subclass(self):
        """Checks if Review is a subclass of BaseModel."""
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_place_id_attr(self):
        """Checks if Review has the 'place_id' attribute, and it's initialized properly."""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        if models.storage_t == 'db':
            self.assertEqual(review.place_id, None)
        else:
            self.assertEqual(review.place_id, "")

    def test_user_id_attr(self):
        """Checks if Review has the 'user_id' attribute, and it's initialized properly."""
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        if models.storage_t == 'db':
            self.assertEqual(review.user_id, None)
        else:
            self.assertEqual(review.user_id, "")

    def test_text_attr(self):
        """Checks if Review has the 'text' attribute, and it's initialized properly."""
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        if models.storage_t == 'db':
            self.assertEqual(review.text, None)
        else:
            self.assertEqual(review.text, "")

    def test_to_dict_creates_dict(self):
        """Checks if the to_dict method creates a dictionary with the proper attributes."""
        r = Review()
        new_d = r.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in r.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """Checks if the values in the dictionary returned from to_dict are correct."""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        r = Review()
        new_d = r.to_dict()
        self.assertEqual(new_d["__class__"], "Review")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], r.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], r.updated_at.strftime(t_format))

    def test_str(self):
        """Checks if the str method has the correct output."""
        review = Review()
        string = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(string, str(review))
