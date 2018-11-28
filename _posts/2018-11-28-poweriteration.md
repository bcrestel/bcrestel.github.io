---
layout: post
title: Power iteration for the $k$ dominant eigenvectors
tags: NLA eigenvalue poweriteration iterative QR
---

First of a disclaimer: This post is not an extensive review of state of the art
techniques to compute eigenvalues or eigenvectors of a matrix. I'm just
summarizing a simple result on the power iteration. This being said, I think
it's fair that I try to motivate the use of power iteration, given how much bad
press this algorithm gets.

The [power iteration](https://en.wikipedia.org/wiki/Power_iteration) 
is a simple way to compute the dominant eigenvector of a
diagonalizable matrix $A$. It is generally slow to converge. What are the
alternatives. Typically, you could use an eigenvalue-revealing factorizations,
then get the eigenvectors with the
[Rayleigh quotient 
iteration](https://en.wikipedia.org/wiki/Rayleigh_quotient_iteration).
You could even stop the factorization early and refine the eigenvalue and
compute the eigenvector at the same time with the Rayleigh quotient iteration,
which converges at a cubic rate(!).
However, the eigenvalue-revealing factorizations (that I am aware of) all
require access to the entries of the matrix. And one of the steps in the
Rayleigh quotient iteration is an 
[inverse iteration](https://en.wikipedia.org/wiki/Inverse_iteration), 
which involves solving a linear system with the matrix $A$.
All of this to say that in some situations, e.g., if the matrix $A$ is not
assembled and you can only compute a matvec, and/or if the matrix $A$ is very
large and sparse such that the matvec is cheap but the inversion costly, you may
want to rely on the power iteration.

The algorithm is pretty simple. You sample a random vector $v$, then repeat the
following steps
* multiply by $A$, i.e., $v = A.v$
* normalize $v$, i.e., $v = v / \| v\|$

Then $v$ will converge to the dominant eigenvector. Why? Since $A$ is
diagonalizable, its eigenvectors form a basis. Let's call these eigenvectors
$q_i$ and the corresponding eigenvalues $\lambda_i$. Then we can write any
random vector as $$ v = \sum_i (v^T.q_i) q_i $$. And then

$$ A^n. v = \sum_i \lambda_i^n (v^T.q_i) q_i $$

After sufficiently many iterations, $A^n . v$ will point toward the dominant
eigenvector. To avoid blowing everything, we normalize $v$ after each step.

Now the next question is: how to apply power iteration to compute the first $k$
eigenvectors? No problem, we can do that. Let's think about the second dominant
eigenvector. It will be the dominant eigenvector if we look in the hyperplane
defined by the dominant eigenvector, that is $q_1^\perp$. One idea would be to
first compute $q_1$ using the power iteration, then repeat the same procedure
but projecting $v$ onto $q_1^\perp$ at each step. That would be:
* multiply by $A$, i.e., $v = A.v$
* project onto $q_1^\perp$, i.e., $v = v - (v^T.q_1)q_1$
* normalize $v$, i.e., $v = v / \| v\|$

This algorithm would converge to $q_2$. After doing so, we could repeat the same
procedure but project onto $(q_1,q_2)^\perp$. And so on, so forth. Now, we can
actually do all the steps at the same time. Instead of sampling a single vector,
sample a matrix $V$ with as many columns as you want eigenvectors. Then after
each left-multiplication by $A$, instead of projecting then normalizing, simply
do a [QR decomposition](https://en.wikipedia.org/wiki/QR_decomposition)
of $V$ and keep the $Q$ matrix. 
* left-multiply by $A$, i.e., $V = A.V$
* project and normalize with a QR decomposition, i.e., $V=Q$ where $Q,R = QR(V)$

That matrix will converge
toward the first $k$ dominant eigenvectors. Here is the code in Python
```python
import numpy as np
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
```
