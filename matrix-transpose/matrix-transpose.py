import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    cur = np.array(A)
    m, n = cur.shape
    ans = np.zeros((n, m))
    for i in range(m):
        for j in range(n):
            ans[j][i] = cur[i][j]
    
    return ans
    pass
