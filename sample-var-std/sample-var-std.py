import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x = np.array(x)
    n = x.size
    var = np.sum((x - np.mean(x))**2) / (n - 1)
    return (var, var**0.5)
    pass