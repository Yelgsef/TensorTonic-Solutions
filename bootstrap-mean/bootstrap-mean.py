import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Returns: (boot_means, lower, upper)
    """
    # Write code here
    x = np.array(x)
    n = x.size
    temp = np.zeros(n)
    boot_means = np.zeros(n_bootstrap)
    
    for a in range(n_bootstrap):
        for i in range(n):
            temp[i] = x[rng.integers(0, n)]
        boot_means[a] = np.mean(temp)

    lower = np.quantile(boot_means, (1 - ci) / 2)
    upper = np.quantile(boot_means, 1 - (1 - ci) / 2)
    return (boot_means, lower, upper)
    pass
