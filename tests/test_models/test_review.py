#!/usr/bin/python3
"""Defines unittests for models/review.py."""

import unittest
import models
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())
    
    def test_id_is_public_string(self):
        self.assertEqual(str, type(Review().id))

if __name__ == "__main__":
    unittest.main()
