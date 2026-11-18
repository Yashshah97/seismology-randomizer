"""
Module for loading and preprocessing earthquake waveform data.

This module provides a class `DataLoader` to load and preprocess earthquake waveform data.
"""

import random
from typing import List, Tuple

class DataLoader:
    """
    Class to load and preprocess earthquake waveform data.

    Attributes:
        data (List[Tuple[float]]): Loaded data as a list of tuples containing time and amplitude values.
        num_samples (int): Number of samples in the loaded data.
    """

    def __init__(self, filename: str):
        """
        Initializes the DataLoader with a filename to load from.

        Args:
            filename (str): Path to the file containing earthquake waveform data.
        """
        self.filename = filename
        self.data = []

    def load_data(self) -> None:
        """
        Loads the earthquake waveform data from the specified file.

        The file is expected to contain time and amplitude values, one pair per line,
        separated by a space. The data is stored as a list of tuples in the `data` attribute.
        """
        with open(self.filename, 'r') as f:
            for line in f:
                time, amplitude = map(float, line.split())
                self.data.append((time, amplitude))

    def preprocess_data(self) -> None:
        """
        Preprocesses the loaded data by randomly sampling a specified number of points.
        """
        num_samples = random.randint(1000, 2000)
        self.data = random.sample(self.data, num_samples)

def load_and_preprocess(filename: str, num_samples: int) -> List[Tuple[float]]:
    """
    Loads and preprocesses earthquake waveform data.

    Args:
        filename (str): Path to the file containing earthquake waveform data.
        num_samples (int): Number of samples to keep after preprocessing.

    Returns:
        List[Tuple[float]]: Preprocessed data as a list of tuples containing time and amplitude values.
    """
    loader = DataLoader(filename)
    loader.load_data()
    loader.preprocess_data()
    return loader.data

# Example usage
filename = 'data.txt'
num_samples = 1500
preprocessed_data = load_and_preprocess(filename, num_samples)
print(preprocessed_data[:5])  # Print the first five samples of preprocessed data
