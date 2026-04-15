import numpy as np
from scipy.stats import norm


def z_test(sample, mu0, sigma=None, alternative='two-sided'):
    """
    Perform a large sample Z-test.

    Parameters
    ----------
    sample : array-like
        Sample observations
    mu0 : float
        Population mean under H0
    sigma : float (optional)
        Population standard deviation. If None, sample std is used.
    alternative : str
        'two-sided', 'greater', or 'less'

    Returns
    -------
    z_stat : float
        Z test statistic
    p_value : float
        Corresponding p-value
    """

    sample = np.array(sample)
    n = len(sample)
    x_bar = np.mean(sample)

    if sigma is None:
        sigma = np.std(sample, ddof=1)

    standard_error = sigma / np.sqrt(n)

    z_stat = (x_bar - mu0) / standard_error

    if alternative == 'two-sided':
        p_value = 2 * (1 - norm.cdf(abs(z_stat)))
    elif alternative == 'greater':
        p_value = 1 - norm.cdf(z_stat)
    elif alternative == 'less':
        p_value = norm.cdf(z_stat)
    else:
        raise ValueError(
            "alternative must be 'two-sided', 'greater', or 'less'")

    return z_stat, p_value


# Example usage
sample_data = [52, 48, 50, 47, 49, 51, 53, 46, 52, 50,
               49, 48, 47, 51, 52, 50, 49, 48, 47, 51,
               53, 54, 50, 49, 48, 47, 52, 51, 50, 49]

mu0 = 50

z_stat, p_val = z_test(sample_data, mu0)

print("Z statistic:", z_stat)
print("p-value:", p_val)
