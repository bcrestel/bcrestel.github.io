---
layout: post
title: Under determined least squares
tags: leastsquares pseudoinverse underdetermined
---

I somehow always forget these things. So I'll mark it down here once and for
all.

When looking for parameter $\beta$ in a linear system
\\[ y = X . \beta + e \\]
where $y \in \mathbb{R}^{n \times 1}, X \in \mathbb{R}^{n \times  m}, \beta \in
\mathbb{R}^{m \times 1}$, and noise $e \sim \mathcal{N}(0, \sigma^2)$, it is
formulated as the following linear least squares problem
\\[ \hat{\beta} = \arg \min_\beta || X . \beta - y ||_2^2 \\]

### When $X$ is full rank
When $X$ is full rank, then we can just solve the normal equation, by solving
the first-order optimality condition of the least-squares problem, 
\\[ X^T . (X . \hat{\beta} - y) = 0 \\]
which gives the solution
\\[ \hat{\beta} = (X^T.X)^{-1} . X^T.y \\]
This requires $X$ to be full rank so that $X^T.X$ is invertible.

### When $X$ is rank deficient
If $X$ doesn't have full rank, then we don't have a unique answer $\hat{\beta}$.
Instead we have an entire linear space of solution. That is given any solution
$\hat{\beta}$, then any non-trivial vector $x$ in the null space of $X$, $\hat{\beta} + x$
will still be a solution; the fact that such a non-trivial $x$ exists is due to
the fact that $X$ is rank deficient.
All of this matters if you care about $\hat{\beta}$, as it doesn't have a unique
value anymore. 

But if all you care about is transforming a given $X$ into a $y$, then that's no
problem. All you need is to fine a (any) solution $\hat{\beta}$. To do this, we
typically rely on the
[pseudo-inverse](https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse#Linear_least-squares).
Let's see why. When $X$ is rank-deficient, we can still write its singular value
decomposition, $X = U.\Sigma.V^\star$, where $U \in \mathbb{R}^{n \times n},
\Sigma \in \mathbb{R}^{n \times m}, V\in\mathbb{R}^{m \times m}$. 
$U, V$ are unitary matrices.
$\Sigma$
is a diagonal matrix that contains the singular values (typically written in
decreasing order). Since $X$ is rank-deficient, some of these singular values
are zero. Let's assume $rank(X) = r$. Then the reduced SVD is obtained by
keeping the first $r$ columns of $U$ and $V$, and keeping only the first $r$
singular values of $\Sigma$. We write this as $X = U_r . \Sigma_r . V_r^\star$,
where $U_r \in \mathbb{R}^{n\times r}, V_r \in \mathbb{R}^{m \times r}$ and
$\Sigma \in \mathbb{R}^{r \times r}$. Replacing this reduced SVD into the
least-squares formulation, we can left multiply by a unitary matrix $U^\star$.
Due to the orthogonality of the columns of $U$, we get
\\[ \arg \min_\beta || \Sigma_r . V_r^\star . \beta - U_r^\star . y ||^2 + 
|| - U_{n-r}^\star . y ||^2 \\]
Since the second term does not depend on $\beta$, it won't impact the value of
$\beta$ such that we can remove it. Also, we can left-multiply by
$\Sigma_r^{-1}$ which is invertible since all singular values in $\Sigma_r$ are
non-zero. We get
\\[ \arg \min_\beta || V_r^\star . \beta - \Sigma_r^{-1} . U_r^\star . y ||^2 \\]
And we're done. Well, almost. Now we see where the non-unicity lies. The term
$V_r^\star . \beta$ is uniquely defined by this equation. And the least-squares
equation will be minimum (actually zero) when
\\[ V_r^\star . \beta = \Sigma_r^{-1} . U_r^\star . y \\]
However, $\beta$ is not uniquely defined. Indeed, let's assume we know a
solution $\hat{\beta}$ to the equation above. Then adding any vector of the form
$v = V_{m-r} . z$, we still get a solution. 
We can do though is to look for a special solution, and typically we look for
the solution with the minimum norm. First, we can easily verify that
\\[ \hat{\beta} = V_r . \Sigma_r^{-1} . U_r^\star . y \\]
is a solution to the minimization problem above, as it will lead to a zero norm.
Now this is the unique solution in the subspace described by the $V_r$. But any
other solution of the form $\hat{\beta} + V_{m-r} . z$ will have a larger norm,
since $V_r$ and $V_{m-r}$ are orthogonal to each other.
So we found the minimum norm solution. It is often written in terms of the
[pseudo-inverse](https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse#Singular_value_decomposition_(SVD)) of $X$, i.e., $\hat{\beta} = X^+ . y$, where $X^+ = V . \Sigma^+
. U^\star$, where $\Sigma^+$ is a diagonal matrix with all singluar values
inverted, except when they were zero in which case they are left unchanged. We
can easily verify that the reduced form of the pseudo-inverse is indeed $V_r .
\Sigma_r^{-1} . U_r^\star$.
