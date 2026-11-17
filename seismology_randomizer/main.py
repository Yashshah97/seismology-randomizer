"""
Main entry point for the Seismology Monte Carlo Engine.

Provides a command-line interface to run Monte Carlo experiments and generate
confidence intervals.
"""

import argparse
from statistics import mean, stdev
from typing import List, Tuple

def calculate_ci(data: List[float], confidence_level: float = 0.95) -> Tuple[float, float]:
    """
    Calculate the confidence interval for a given dataset.

    Args:
        data (List[float]): The dataset to calculate the CI from.
        confidence_level (float): The desired confidence level (default: 0.95).

    Returns:
        Tuple[float, float]: A tuple containing the lower and upper bounds of the CI.
    """
    n = len(data)
    mean_val = mean(data)
    std_dev = stdev(data)

    z_score = _get_z_score(confidence_level)
    margin_of_error = (z_score * std_dev) / (n ** 0.5)

    lower_bound = mean_val - margin_of_error
    upper_bound = mean_val + margin_of_error

    return lower_bound, upper_bound


def _get_z_score(confidence_level: float) -> float:
    """
    Get the z-score corresponding to a given confidence level.

    Args:
        confidence_level (float): The desired confidence level.

    Returns:
        float: The z-score.
    """
    # Approximate z-scores for common confidence levels
    if confidence_level == 0.95:
        return 1.96
    elif confidence_level == 0.99:
        return 2.576

    raise ValueError("Unsupported confidence level")


def main() -> None:
    parser = argparse.ArgumentParser(description="Seismology Monte Carlo Engine")
    parser.add_argument("--num-simulations", type=int, default=1000)
    parser.add_argument("--confidence-level", type=float, default=0.95)

    args = parser.parse_args()

    num_simulations = args.num_simulations
    confidence_level = args.confidence_level

    data = [1.23, 2.45, 3.67, 4.89, 5.01]  # Replace with actual simulation data

    ci = calculate_ci(data, confidence_level)
    print(f"Confidence Interval (95%): {ci[0]} - {ci[1]}")


if __name__ == "__main__":
    main()
