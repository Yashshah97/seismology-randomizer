import math
from typing import Callable, List, Tuple

def monte_carlo_experiment(
    num_trials: int,
    func: Callable[[float], float],
    confidence_interval: float = 0.95,
) -> Tuple[float, float]:
    """
    Run a Monte Carlo experiment.

    Args:
        num_trials (int): Number of trials.
        func (Callable[[float], float]): Function to run for each trial.
        confidence_interval (float): Confidence interval (default is 0.95).

    Returns:
        Tuple[float, float]: Mean and standard deviation of results.
    """
    if num_trials <= 1:
        raise ValueError("Number of trials must be greater than 1")

    results = [func(0) for _ in range(num_trials)]
    mean = sum(results) / num_trials
    std_dev = math.sqrt(sum((x - mean) ** 2 for x in results) / (num_trials - 1))
    ci_lower = mean - (std_dev * (math.sqrt(1 / num_trials) * math.erfinv(math.sqrt(confidence_interval))))
    ci_upper = mean + (std_dev * (math.sqrt(1 / num_trials) * math.erfinv(math.sqrt(1 - confidence_interval))))

    return mean, std_dev, ci_lower, ci_upper


def run_monte_carlo_experiment(
    func: Callable[[float], float],
    num_trials: int,
    confidence_interval: float = 0.95,
) -> List[Tuple[float, float]]:
    """
    Run multiple Monte Carlo experiments.

    Args:
        func (Callable[[float], float]): Function to run for each trial.
        num_trials (int): Number of trials.
        confidence_interval (float): Confidence interval (default is 0.95).

    Returns:
        List[Tuple[float, float]]: Mean and standard deviation of results for each experiment.
    """
    return [
        monte_carlo_experiment(num_trials, func, confidence_interval)
        for _ in range(10)  # Run 10 experiments
    ]
