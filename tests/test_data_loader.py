import unittest
from seismology_randomizer import data_loader

class TestDataLoader(unittest.TestCase):
    def test_load_data(self):
        filename = 'data.txt'
        loader = data_loader.DataLoader(filename)
        loader.load_data()
        self.assertGreater(len(loader.data), 0)

    def test_preprocess_data(self):
        filename = 'data.txt'
        num_samples = 1500
        loader = data_loader.DataLoader(filename)
        loader.load_data()
        loader.preprocess_data()
        self.assertEqual(len(loader.data), num_samples)

    def test_load_and_preprocess(self):
        filename = 'data.txt'
        num_samples = 1500
        preprocessed_data = data_loader.load_and_preprocess(filename, num_samples)
        self.assertEqual(len(preprocessed_data), num_samples)

if __name__ == '__main__':
    unittest.main()
