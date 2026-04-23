import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    x = np.array(x)
    pmf = np.where(x == 0, 1 - p, p)
    mean = p 
    var = p * (1 - p)
    return (pmf, mean, var)
    pass