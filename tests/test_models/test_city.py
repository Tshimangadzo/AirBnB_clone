#!/usr/bin/python3
"""Defines unittests for models/city.py."""

import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_str_repr(self):
        today_date = datetime.today()
        today_date_repr = repr(today_date)
        city_ = City()
        city_.id = "some_id"
        city_.created_at = today_date
        city_.updated_at = today_date
        city_str = city_.__str__()
        self.assertIn("[City] (some_id)", city_str)
        self.assertIn("'id': 'some_id'", city_str)
        self.assertIn("'created_at': " + today_date_repr, city_str)
        self.assertIn("'updated_at': " + today_date_repr, city_str)

    def test_state_id_is_public_class_attribute(self):
        city = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(city))
        self.assertNotIn("state_id", city.__dict__)

    def test_name_is_public_class_attribute(self):
        city = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(city))
        self.assertNotIn("name", city.__dict__)

    def test_two_cities_unique_ids(self):
        city_1 = City()
        city_2 = City()
        self.assertNotEqual(city_1.id, city_2.id)

    def test_two_cities_different_created_at(self):
        city_1 = City()
        sleep(0.05)
        city_2 = City()
        self.assertLess(city_1.created_at, city_2.created_at)

    def test_two_cities_different_updated_at(self):
        city_1 = City()
        sleep(0.05)
        city_2 = City()
        self.assertLess(city_1.updated_at, city_2.updated_at)

    def test_args_unused(self):
        city = City(None)
        self.assertNotIn(None, city.__dict__.values())

    def test_instantiation_with_kwargs(self):
        today_date = datetime.today()
        today_date_iso = today_date.isoformat()
        city = City(id="some_id", created_at=today_date_iso,
                    updated_at=today_date_iso)
        self.assertEqual(city.id, "some_id")
        self.assertEqual(city.created_at, today_date)
        self.assertEqual(city.updated_at, today_date)

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))


if __name__ == "__main__":
    unittest.main()
