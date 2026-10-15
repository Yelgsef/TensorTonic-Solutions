import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if not seqs and not max_len:
        return np.empty((0, 0), dtype=int)
    if not max_len: 
        max_len = max(len(arr) for arr in seqs) or 0
    N = len(seqs)

    ans = np.full((N, max_len), pad_value)
    for i in range(N):
        for j in range(min(len(seqs[i]), max_len)):
            ans[i][j] = seqs[i][j]
    return ans