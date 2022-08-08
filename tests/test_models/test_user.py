import imp
import unittest
from models.user import User
import models

class TestUser_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""
    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

if __name__ == "__main__":
    unittest.main()
