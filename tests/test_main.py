import unittest
from seismology_randomizer import main

class TestMainModule(unittest.TestCase):
    def test_calculate_ci(self):
        data = [1, 2, 3]
        ci = main.calculate_ci(data)
        self.assertIsInstance(ci, tuple)
        self.assertEqual(len(ci), 2)

    def test_get_z_score(self):
        confidence_level = 0.95
        z_score = main._get_z_score(confidence_level)
        self.assertAlmostEqual(z_score, 1.96)

    def test_main_args(self):
        parser = main.ArgumentParser()
        args = parser.parse_args(["--num-simulations", "100"])
        self.assertEqual(args.num_simulations, 100)

if __name__ == "__main__":
    unittest.main()
