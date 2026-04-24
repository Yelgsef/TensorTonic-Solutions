import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    x = np.array(x)
    n = x.size
    mean = np.mean(x)
    
    std = (np.sum((x - mean)**2) / (n - 1))**0.5
    t_stat = (mean - mu0) / (std / (n**0.5))
    return t_stat

    pass