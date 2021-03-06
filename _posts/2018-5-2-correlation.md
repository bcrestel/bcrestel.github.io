---
layout: post
title: Correlation, covariance, and standard deviation
tags: correlation statistics covariance
---

I want to illustrate how correlation and covariance relates to the standard
deviation of the random variables they involve.

Let's introduce two random variables $X_i$, $i=1,2$, and the centered random
variables $Y_i = X_i - \mathbb{E}[X_i]$. Then we have 
$$\mathbb{E}[Y_i] = 0$$, $$Var[Y_i] = Var(X_i)$$, $$Cov(Y_1, Y_2) =
Cov(X_1,X_2)$$.
We then introduce two new random variables, $\tilde{X}_i$, with the same
expectation as $X_i$, but with a re-scaled standard deviation,

$$ \begin{align}
\tilde{X}_i & = \mathbb{E}[X_i] + a_i Y_i \notag \\
 & = \mathbb{E}[X_i] + a_i (X_i - \mathbb{E}[X_i]) 
\end{align} $$

with $a_i \in \mathbb{R}$. We can immediately verify that
$\mathbb{E}[\tilde{X}_i] = \mathbb{E}[X_i]$ and $Var[\tilde{X}_i] = a_i^2
Var[X_i]$.

Then, the covariance of $\tilde{X}_1$ and $\tilde{X}_2$ gives

$$ \begin{align}
Cov(\tilde{X}_1,\tilde{X}_2) & =
\mathbb{E}[(\tilde{X}_1-\mathbb{E}[\tilde{X}_1])(\tilde{X}_2-\mathbb{E}[\tilde{X}_2])]
\notag
\\ 
& = a_1a_2 \mathbb{E}[Y_1 Y_2] \notag \\
& = a_1a_2 Cov(X_1,X_2)
\end{align} $$

Whereas the correlation between $\tilde{X}_1$ and $\tilde{X}_2$ is given by

$$ \begin{align}
corr(\tilde{X}_1,\tilde{X}_2) & =
\frac{Cov(\tilde{X}_1,\tilde{X}_2)}{\sqrt{Var[\tilde{X}_1] Var[\tilde{X}_2]}}
\notag \\
& = \frac{Cov({X}_1,{X}_2)}{\sqrt{Var[{X}_1] Var[{X}_2]}} \notag \\
& = 
corr({X}_1,{X}_2)
\end{align} $$

In words, the covariance scales with the standard deviation of each random
variable, whereas the correlation is oblivious to the standard deviations. 




