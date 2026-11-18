import unittest
from seismology_randomizer import tests_test_engine

class TestTestEngine(unittest.TestCase):

    def test_import(self):
        self.assertIsNotNone(tests_test_engine)

    def test_module_has_tests(self):
        self.assertTrue(hasattr(tests_test_engine, 'test_run'))
        self.assertTrue(hasattr(tests_test_engine, 'test_run_with_confidence_intervals'))
        self.assertTrue(hasattr(tests_test_engine, 'test_run_invalid_input'))

if __name__ == '__main__':
    unittest.main()
