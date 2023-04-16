from unittest import TestCase

from app import index


class AppTests(TestCase):
    def test_index(self):
        self.assertEqual(index(), {'message': 'Hello, world!'})
