import numpy as np

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    def factorial (n):
        return np.prod(np.arange(1, n + 1))
    
    pmf = np.exp(-lam) * (lam ** k) / factorial(k)
    cmf = pmf
    for i in range(0, k):
        cmf += np.exp(-lam) * (lam ** i) / factorial(i)
    return(pmf, cmf)
    pass