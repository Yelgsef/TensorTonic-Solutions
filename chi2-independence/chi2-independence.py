import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here
    C = np.array(C)
    row = np.sum(C, axis=1)
    col = np.sum(C, axis=0)
    N = np.sum(C)
    E = np.outer(row, col) / N
    chi2 = np.sum((C - E)**2 / E)
    return (chi2, E)
    pass