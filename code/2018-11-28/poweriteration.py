"""
Compute power iteration for dominant eigenvalues
and for k largest eigenvalues
"""

import numpy as np

def power_iteration(A, eps=1e-10):
    """
    Inputs:
        A = matrix (symmetric)
        eps = precision
    Outputs:
        v = eigenvector for dominant eigenvalue
    """
    m, n = A.shape
    v = np.random.randn(n).reshape((-1,1))
    v = v / np.linalg.norm(v)
    for kk in range(1000):
        v_old = v.copy()
        v = A.dot(v)
        v = v / np.linalg.norm(v)
        diff = np.linalg.norm(v-v_old)
        if diff < eps:
            return v


def power_iteration_k(A, k, eps=1e-10):
    """
    Inputs:
        A = matrix (symmetric)
        k = nb of eigenvectors to compute
        eps = precision
    Outputs:
        v = matrix of the k dominant eigenvectors
    """
    m, n = A.shape
    v = np.random.randn(n*k).reshape((-1,k))
    v,_ = np.linalg.qr(v)
    for kk in range(1000):
        v_old = v.copy()
        v = A.dot(v)
        v,_ = np.linalg.qr(v)
        diff = np.max(np.sqrt(np.sum((v-v_old)**2, axis=0)))
        if diff < eps:
            return v    


def Rayleigh_quotient(A, v):
    return (v.T).dot(A.dot(v)) / (v.T).dot(v)


if __name__ == "__main__":
    R = np.random.randn(25).reshape((5,5))
    A = R.dot(R.T)
    l,X = np.linalg.eig(A)
    l1 = power_iteration(A)
    print(l1), print(Rayleigh_quotient(A,l1))
    print(X[:,0].reshape((-1,1))), print(l[0])
    
    lk = power_iteration_k(A,3)
    print(lk)
    print(X[:,:3])
    
