"""Smoke tests for tests_test_engine."""
import unittest

from seismology_randomizer import tests_test_engine


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(tests_test_engine, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(tests_test_engine) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
