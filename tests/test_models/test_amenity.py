#!/usr/bin/python3
"""Defines unittests for models/amenity.py."""

from datetime import datetime
from time import sleep
import unittest
import models
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_string(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        amenity = Amenity()
        self.assertEqual(str, type(amenity.name))
        self.assertIn("name", dir(amenity))
        self.assertNotIn("name", amenity.__dict__)
 
    def test_city_id_is_public_class_attribute(self):
        amenity = Amenity()
        self.assertEqual(str, type(amenity.name))
        self.assertIn("name", dir(amenity))
        self.assertNotIn("name", amenity.__dict__)

    def test_two_amenities_unique_ids(self):
        amenity_1 = Amenity()
        amenity_2 = Amenity()
        self.assertNotEqual(amenity_1.id, amenity_2.id)

    def test_two_amenities_different_created_at(self):
        amenity_1 = Amenity()
        sleep(0.05)
        amenity_2 = Amenity()
        self.assertLess(amenity_1.created_at, amenity_2.created_at)

    def test_two_amenities_different_updated_at(self):
        amenity_1 = Amenity()
        sleep(0.05)
        amenity_2 = Amenity()
        self.assertLess(amenity_1.updated_at, amenity_2.updated_at)

    def test_str_repr(self):
        today_date = datetime.today()
        today_date_repr = repr(today_date)
        amenity_ = Amenity()
        amenity_.id = "some_id"
        amenity_.created_at = today_date
        amenity_.updated_at = today_date
        amenity_str = amenity_.__str__()
        self.assertIn("[Amenity] (some_id)", amenity_str)
        self.assertIn("'id': 'some_id'", amenity_str)
        self.assertIn("'created_at': " + today_date_repr, amenity_str)
        self.assertIn("'updated_at': " + today_date_repr, amenity_str)

    def test_instantiation_with_kwargs(self):
        today_date = datetime.today()
        today_date_iso = today_date.isoformat()
        amenity = Amenity(id="some_id", created_at=today_date_iso,
                      updated_at=today_date_iso)
        self.assertEqual(amenity.id, "some_id")
        self.assertEqual(amenity.created_at, today_date)
        self.assertEqual(amenity.updated_at, today_date)


if __name__ == "__main__":
    unittest.main()
