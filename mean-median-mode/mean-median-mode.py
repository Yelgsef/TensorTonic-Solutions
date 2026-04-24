import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = np.array(x)
    mean = np.mean(x)
    med = np.median(x)
    freq = Counter(x)
    mode = freq.most_common(1)[0][0]
    
    return (mean, med, mode)
    pass