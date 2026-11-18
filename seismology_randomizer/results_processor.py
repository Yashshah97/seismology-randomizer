import math
import statistics
from typing import List, Dict

class ResultsProcessor:
    """
    Processes results from Monte Carlo experiments.
    """

    def __init__(self, data: List[Dict]):
        """
        Initializes the processor with the given data.

        :param data: A list of dictionaries containing experiment results.
        """
        self.data = data

    def calculate_mean(self) -> float:
        """
        Calculates the mean of the experiment results.

        :return: The mean value.
        """
        return statistics.mean([result['value'] for result in self.data])

    def calculate_confidence_interval(self, confidence_level: float = 0.95) -> (float, float):
        """
        Calculates a confidence interval around the mean.

        :param confidence_level: The desired confidence level (default is 95%).
        :return: A tuple containing the lower and upper bounds of the interval.
        """
        n = len(self.data)
        std_dev = statistics.stdev([result['value'] for result in self.data])
        margin_of_error = math.sqrt((n - 1) * std_dev ** 2 / (n * (n - 2)))
        lower_bound = self.calculate_mean() - (margin_of_error * math.sqrt(n))
        upper_bound = self.calculate_mean() + (margin_of_error * math.sqrt(n))
        return lower_bound, upper_bound

    def plot_results(self):
        """
        Plots the experiment results using matplotlib.
        """
        import matplotlib.pyplot as plt
        values = [result['value'] for result in self.data]
        plt.hist(values, bins=10)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('Experiment Results')
        plt.show()

# Example usage:
data = [
    {'value': 1.2},
    {'value': 3.4},
    {'value': 5.6},
    # ...
]
processor = ResultsProcessor(data)
mean_value = processor.calculate_mean()
lower, upper = processor.calculate_confidence_interval()
print(f'Mean value: {mean_value}')
print(f'95% CI: [{lower}, {upper}]')
