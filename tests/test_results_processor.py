import unittest
from seismology_randomizer import results_processor

class TestResultsProcessor(unittest.TestCase):

    def test_calculate_mean(self):
        data = [{'value': 1}, {'value': 2}, {'value': 3}]
        processor = results_processor.ResultsProcessor(data)
        self.assertEqual(processor.calculate_mean(), 2)

    def test_calculate_confidence_interval(self):
        data = [{'value': 1}, {'value': 2}, {'value': 3}]
        processor = results_processor.ResultsProcessor(data)
        lower, upper = processor.calculate_confidence_interval()
        self.assertGreaterEqual(lower, 1.25)
        self.assertLessEqual(upper, 2.75)

    def test_plot_results(self):
        # This method is not easily testable due to its side effects
        pass

if __name__ == '__main__':
    unittest.main()
