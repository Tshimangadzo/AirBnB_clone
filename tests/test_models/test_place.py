#!/usr/bin/python3
"""Defines unittests for models/place.py."""

from datetime import datetime
import unittest
import models
from models.place import Place
from time import sleep


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_string(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        place = Place()
        self.assertEqual(str, type(place.city_id))
        self.assertIn("city_id", dir(place))
        self.assertNotIn("city_id", place.__dict__)

    def test_user_id_is_public_class_attribute(self):
        place = Place()
        self.assertEqual(str, type(place.user_id))
        self.assertIn("user_id", dir(place))
        self.assertNotIn("user_id", place.__dict__)

    def test_name_is_public_class_attribute(self):
        place_ = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(place_))
        self.assertNotIn("name", place_.__dict__)

    def test_description_is_public_class_attribute(self):
        place = Place()
        self.assertEqual(str, type(place.description))
        self.assertIn("description", dir(place))
        self.assertNotIn("description", place.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        place = Place()
        self.assertEqual(int, type(place.number_rooms))
        self.assertIn("number_rooms", dir(place))
        self.assertNotIn("number_rooms", place.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        place = Place()
        self.assertEqual(int, type(place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(place))
        self.assertNotIn("number_bathrooms", place.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        place = Place()
        self.assertEqual(int, type(place.max_guest))
        self.assertIn("max_guest", dir(place))
        self.assertNotIn("max_guest", place.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        place = Place()
        self.assertEqual(int, type(place.price_by_night))
        self.assertIn("price_by_night", dir(place))
        self.assertNotIn("price_by_night", place.__dict__)

    def test_latitude_is_public_class_attribute(self):
        place = Place()
        self.assertEqual(float, type(place.latitude))
        self.assertIn("latitude", dir(place))
        self.assertNotIn("latitude", place.__dict__)

    def test_longitude_is_public_class_attribute(self):
        place = Place()
        self.assertEqual(float, type(place.longitude))
        self.assertIn("longitude", dir(place))
        self.assertNotIn("longitude", place.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        place = Place()
        self.assertEqual(list, type(place.amenity_ids))
        self.assertIn("amenity_ids", dir(place))
        self.assertNotIn("amenity_ids", place.__dict__)

 
    def test_city_id_is_public_class_attribute(self):
        place_ = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(place_))
        self.assertNotIn("name", place_.__dict__)

    def test_two_places_unique_ids(self):
        place_1 = Place()
        place_2 = Place()
        self.assertNotEqual(place_1.id, place_2.id)

    def test_two_places_different_created_at(self):
        place_1 = Place()
        sleep(0.05)
        place_2 = Place()
        self.assertLess(place_1.created_at, place_2.created_at)

    def test_two_places_different_updated_at(self):
        place_1 = Place()
        sleep(0.05)
        place_2 = Place()
        self.assertLess(place_1.updated_at, place_2.updated_at)

    def test_str_repr(self):
        today_date = datetime.today()
        today_date_repr = repr(today_date)
        place_ = Place()
        place_.id = "some_id"
        place_.created_at = today_date
        place_.updated_at = today_date
        place_str = place_.__str__()
        self.assertIn("[Place] (some_id)", place_str)
        self.assertIn("'id': 'some_id'", place_str)
        self.assertIn("'created_at': " + today_date_repr, place_str)
        self.assertIn("'updated_at': " + today_date_repr, place_str)

    def test_instantiation_with_kwargs(self):
        today_date = datetime.today()
        today_date_iso = today_date.isoformat()
        place = Place(id="some_id", created_at=today_date_iso,
                      updated_at=today_date_iso)
        self.assertEqual(place.id, "some_id")
        self.assertEqual(place.created_at, today_date)
        self.assertEqual(place.updated_at, today_date)

if __name__ == "__main__":
    unittest.main()
