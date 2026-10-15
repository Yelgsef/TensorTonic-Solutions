import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """
    # Write code here
    w = np.zeros(X.shape[1])
    b = 0
    m = X.shape[1]
    n = X.shape[0]
    for _ in range(steps):
        z = X @ w + b
        y_pred = _sigmoid(z)
        w = w - lr * (1 / n) * np.sum(X.T * (y_pred - y.T), axis=1)
        b = b - lr * (1 / n)  * np.sum((y_pred - y.T))
    return (w, b)
    pass