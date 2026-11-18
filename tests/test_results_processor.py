"""Smoke tests for results_processor."""
import unittest

from seismology_randomizer import results_processor


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(results_processor, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(results_processor) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
