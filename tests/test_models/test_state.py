#!/usr/bin/python3
"""Defines unittests for models/state.py."""

import models
from models.state import State
import unittest


class TestState_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_public_string(self):
        self.assertEqual(str, type(State().id))

if __name__ == "__main__":
    unittest.main()
