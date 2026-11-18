import unittest
from seismology_randomizer import engine
import math
import random

class TestEngine(unittest.TestCase):
    def test_monte_carlo_experiment(self):
        func = lambda x: x**2
        mean, std_dev, ci_lower, ci_upper = engine.monte_carlo_experiment(1000, func)
        self.assertGreater(mean, 0)
        self.assertLess(std_dev, math.sqrt(sum(x**4 for x in range(-10, 11)) / 1000))

    def test_run_monte_carlo_experiment(self):
        func = lambda x: x**2
        results = engine.run_monte_carlo_experiment(func, 1000)
        self.assertEqual(len(results), 10)

if __name__ == '__main__':
    unittest.main()
