import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    if not y: 
        return 0.0
    y = np.array(y)

    value, count = np.unique(y, return_counts=True)
    total = sum(count)
    p = np.array(count / total)
    return -sum(p * np.log2(p))
    pass