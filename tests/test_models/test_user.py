#!/usr/bin/python3
"""Defines unittests for models/user.py."""

import unittest
from models.user import User
import models


class TestUser_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_string(self):
        self.assertEqual(str, type(User().id))


if __name__ == "__main__":
    unittest.main()
