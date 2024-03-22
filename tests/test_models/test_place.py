#!/usr/bin/python3
"""
Contains classes for testing documentations in TestPlaceDocs
"""

from datetime import datetime
import inspect
import models
from models import place
from models.base_model import BaseModel
import pep8
import unittest
Place = place.Place


class TestPlaceDocs(unittest.TestCase):
    """Validates documentation and style of the Place class"""
    @classmethod
    def setUpClass(cls):
        """Initializes doc tests"""
        cls.place_f = inspect.getmembers(Place, inspect.isfunction)

    def test_pep8_conformance_place(self):
        """Verifies PEP8 conformity in models/place.py."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style errors and warnings found.")

    def test_pep8_conformance_test_place(self):
        """Confirms PEP8 conformity in tests/test_models/test_place.py."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style errors and warnings found.")

    def test_place_module_docstring(self):
        """Validates docstring presence in place.py module."""
        self.assertIsNot(place.__doc__, None,
                         "A docstring is required for place.py")
        self.assertTrue(len(place.__doc__) >= 1,
                        "A docstring is required for place.py")

    def test_place_class_docstring(self):
        """Checks if the Place class has a docstring."""
        self.assertIsNot(Place.__doc__, None,
                         "Place class requires a docstring")
        self.assertTrue(len(Place.__doc__) >= 1,
                        "Place class requires a docstring")

    def test_place_func_docstrings(self):
        """Ensures all methods in Place have docstrings."""
        for func in self.place_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method must have a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method must have a docstring".format(func[0]))


class TestPlace(unittest.TestCase):
    """Tests for the Place class"""
    def test_is_subclass(self):
        """Checks if Place is a subclass of BaseModel"""
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_city_id_attr(self):
        """Confirms Place has a city_id attribute, which is an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        if models.storage_t == 'db':
            self.assertEqual(place.city_id, None)
        else:
            self.assertEqual(place.city_id, "")

    def test_user_id_attr(self):
        """Verifies Place has a user_id attribute, which is an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        if models.storage_t == 'db':
            self.assertEqual(place.user_id, None)
        else:
            self.assertEqual(place.user_id, "")

    def test_name_attr(self):
        """Ensures Place has a name attribute, which is an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        if models.storage_t == 'db':
            self.assertEqual(place.name, None)
        else:
            self.assertEqual(place.name, "")

    def test_description_attr(self):
        """Validates Place has a description attribute, which is an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        if models.storage_t == 'db':
            self.assertEqual(place.description, None)
        else:
            self.assertEqual(place.description, "")

    def test_number_rooms_attr(self):
        """Checks Place has a number_rooms attribute, which is an integer == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        if models.storage_t == 'db':
            self.assertEqual(place.number_rooms, None)
        else:
            self.assertEqual(type(place.number_rooms), int)
            self.assertEqual(place.number_rooms, 0)

    def test_number_bathrooms_attr(self):
        """Confirms Place has a number_bathrooms attribute, which is an integer == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        if models.storage_t == 'db':
            self.assertEqual(place.number_bathrooms, None)
        else:
            self.assertEqual(type(place.number_bathrooms), int)
            self.assertEqual(place.number_bathrooms, 0)

    def test_max_guest_attr(self):
        """Ensures Place has a max_guest attribute, which is an integer == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        if models.storage_t == 'db':
            self.assertEqual(place.max_guest, None)
        else:
            self.assertEqual(type(place.max_guest), int)
            self.assertEqual(place.max_guest, 0)

    def test_price_by_night_attr(self):
        """Validates Place has a price_by_night attribute, which is an integer == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        if models.storage_t == 'db':
            self.assertEqual(place.price_by_night, None)
        else:
            self.assertEqual(type(place.price_by_night), int)
            self.assertEqual(place.price_by_night, 0)

    def test_latitude_attr(self):
        """Checks Place has a latitude attribute, which is a float == 0.0"""
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        if models.storage_t == 'db':
            self.assertEqual(place.latitude, None)
        else:
            self.assertEqual(type(place.latitude), float)
            self.assertEqual(place.latitude, 0.0)

    def test_longitude_attr(self):
        """Ensures Place has a longitude attribute, which is a float == 0.0"""
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        if models.storage_t == 'db':
            self.assertEqual(place.longitude, None)
        else:
            self.assertEqual(type(place.longitude), float)
            self.assertEqual(place.longitude, 0.0)

    @unittest.skipIf(models.storage_t == 'db', "Not testing File Storage")
    def test_amenity_ids_attr(self):
        """Validates Place has an amenity_ids attribute, which is an empty list"""
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(type(place.amenity_ids), list)
        self.assertEqual(len(place.amenity_ids), 0)

    def test_to_dict_creates_dict(self):
        """Ensures to_dict method creates a dictionary with appropriate attributes"""
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in p.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

   def test_str(self):
        """Validates the output of the str method"""
        place = Place()
        string = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(string, str(place))

