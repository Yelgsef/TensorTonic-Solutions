import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.array(x)
    upper = np.exp(x - np.max(x, axis= x.ndim - 1, keepdims=True))
    lower = np.sum(upper, axis= x.ndim - 1, keepdims=True)
    return upper / lower
    pass