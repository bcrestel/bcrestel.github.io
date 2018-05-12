---
layout: post
title: Sample mean, sample variance
tags: statistics 
---

Let $X_1,\ldots,X_n$ be a random sample from a population with mean $\mu$ and
variance $\sigma^2 < \infty$. Any function of this
random sample is called a statistic, and the probability distribution of a statistic is
called the sampling distribution of that statistic.
In this note, we look at two important statistics.

#### Sample mean
The sample mean is defined as \\[ \bar{X} = \frac1n \sum_{i=1}^n X_i \\]
The sample mean is an unbiased estimator of the mean of the distribution, i.e.,
\\[ \mathbb{E}[\bar{X}] = \frac1n \sum_{i=1}^n \mathbb{E}[X_i] = \mu\\]
And the variance of the sample mean is
$$\begin{align} 
Var[\bar{X}] & = \mathbb{E}[\left( \frac1n \sum_{i=1}^n (X_i-\mu) \right)^2 ]
\notag \\
& = \frac{1}{n^2} \left( \sum_{i=1}^n \mathbb{E}[ (X_i-\mu)^2] + \sum_{i j}
\mathbb{E}[(X_i-\mu)(X_j-\mu)] \right) \notag \\
Var[\bar{X}] & = \frac{\sigma^2}n
\end{align} $$

#### Sample variance
The sample variance is defined as \\[ (S_n^2=) S^2 = \frac1{n-1} \sum_{i=1}^n (X_i -
\bar{X})^2 \\]
The sample variance is an unbiased estimator of the variance of the distribution
the samples are taken from, i.e.,
$$ \begin{align}
\mathbb{E}[S^2] & = \frac1{n-1} \sum_{i=1}^n \left( \mathbb{E}[X_i^2] - \frac2n
\sum_{j=1}^n \mathbb{E}[X_i X_j] + \mathbb{E}[\bar{X}^2] \right) \notag\\
& = \frac1{n-1} \sum_{i=1}^n \left( \mu^2 + \sigma^2 - \frac2n (\sigma^2 + n
\mu^2 ) + \frac1{n^2} (n(\mu^2+\sigma^2) + (n^2-n)\mu^2) \right) \notag\\
\mathbb{E}[S^2] & = \sigma^2
\end{align} $$
However, because of [Jensen's
inequality](https://en.wikipedia.org/wiki/Jensen%27s_inequality#Measure-theoretic_and_probabilistic_form),
$$\sqrt{S^2}$$ is a biased estimator of the standard deviation of the distribution
we sampled from. Indeed, square root being strictly concave over its domain, we
have that $$\mathbb{E}[\sqrt{S^2}] < \sqrt{\mathbb{E}[S^2]} = \sigma$$ (unless
$\sigma=0$).

On the other hand, because square root is a continuous function over
$\mathbb{R}^+$, if $S^2$ is a consistent estimator (converges in probability),
$\sqrt{S^2}$ is also a consistent estimator (i.e., the bias disappears as the
number of samples grow). Using Chebychev's inequality, we see that
\\[ \mathbb{P}[|S_n^2 - \sigma^2| \geq \varepsilon] \leq
\frac{Var[S_n^2]}{\varepsilon^2}, \notag \\]
that is $S^2_n$ is consistent if $Var[S_n^2]$ goes to zero as the number of
samples increase.

Without a proof, one can show that with $\theta$ the fourth moment of the
underlying distribution, we have
\\[ Var[S^2] = \frac1n (\theta - \frac{n-3}{n-1} \sigma^4) \\]
