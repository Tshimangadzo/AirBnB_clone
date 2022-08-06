#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        first_base_model = BaseModel()
        second_base_model = BaseModel()
        self.assertNotEqual(first_base_model.id, second_base_model.id)

    def test_two_models_different_created_at(self):
        first_base_model = BaseModel()
        sleep(0.05)
        second_base_model = BaseModel()
        self.assertLess(first_base_model.created_at,
                        second_base_model.created_at)

    def test_two_models_different_updated_at(self):
        first_base_model = BaseModel()
        sleep(0.05)
        second_base_model = BaseModel()
        self.assertLess(first_base_model.updated_at,
                        second_base_model.updated_at)

    def test_str_repr(self):
        today_date = datetime.today()
        date_repr = repr(today_date)
        base_model = BaseModel()
        base_model.id = "some_id"
        base_model.updated_at = date_repr
        base_model.created_at = date_repr
        base_model_str = base_model.__str__()
        print(date_repr)
        self.assertIn("[BaseModel] (some_id)", base_model_str)
        self.assertIn("'id': 'some_id'", base_model_str)
        self.assertIn("'created_at': " + f"'{date_repr}'", base_model_str)
        self.assertIn("'updated_at': " +  f"'{date_repr}'", base_model_str)


if __name__ == "__main__":
    unittest.main()
