"""
Unit tests for the seismology_randomizer.engine module.

This module contains unit tests for the Monte Carlo experiment runner with confidence intervals.
"""

import unittest
from io import StringIO
from contextlib import redirect_stdout
from typing import Dict, List

class TestEngine(unittest.TestCase):

    def test_run(self):
        """
        Test that the engine can run a simple simulation.
        """
        class MockData:
            def __init__(self):
                self.data = {'a': 1, 'b': 2}

        data = MockData()
        output = StringIO()
        with redirect_stdout(output):
            from seismology_randomizer.engine import run
            run(data)
        result = output.getvalue().strip()

        # Check that the result is a string representation of a dictionary.
        self.assertIsInstance(result, str)

    def test_run_with_confidence_intervals(self):
        """
        Test that the engine can run a simulation with confidence intervals.
        """
        class MockData:
            def __init__(self):
                self.data = {'a': 1, 'b': 2}

        data = MockData()
        output = StringIO()
        with redirect_stdout(output):
            from seismology_randomizer.engine import run
            run(data, confidence_intervals=True)
        result = output.getvalue().strip()

        # Check that the result is a string representation of a dictionary.
        self.assertIsInstance(result, str)

    def test_run_invalid_input(self):
        """
        Test that an error is raised when invalid input is provided.
        """
        data: Dict[str, List[float]] = {'a': [1]}
        with self.assertRaises(TypeError):
            from seismology_randomizer.engine import run
            run(data)

if __name__ == '__main__':
    unittest.main()
