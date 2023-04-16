from unittest import TestCase

from app import root


class AppTests(TestCase):
    def test_root(self):
        self.assertEqual(root(), {'message': 'Hello, world!'})
