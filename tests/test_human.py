import unittest
from app.database import session
from app.models import Human

class HumanTestCase(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_user_exists(self) -> None:
        self.assertEqual(1, 1)