---
layout: post
title: Statistical Hypothesis Tests
tags: statistics datascience
---

The goal of the post is to summarize a few important statistical hypothesis tests that come
back often in practice.

## t-tests
The first class of tests we are going to look at are
[t-tests](https://en.wikipedia.org/wiki/Student%27s_t-test), i.e., tests that
involve a statistic following a [Student's t
distribution](https://en.wikipedia.org/wiki/Student%27s_t-distribution).

#### One sample t-test
The simplest t-test, a [one sample
t-test](https://en.wikipedia.org/wiki/Student%27s_t-test#One-sample_t-test),
can be used to check whether the **sample mean** is equal to a certain value
when all samples
$$\{ X_i \}_i$$ 
are drawn from distributions that have
the same mean $\mu$ and variance $\sigma^2$.  This is a variation of a z-test when the
variance of the population is unknown and needs to be estimated from the
population. Indeed, from the central limit theorem, we know the sample mean,
$\bar{X} = \frac1n \sum_{i=1}^n X_i$, tends (as the number of samples increase)
to a normal distribution, i.e., in the limit of a large number of samples,
\\[ \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim \mathcal{N}(0,1) \\]
Clearly we have $\mathbb{E}[\bar{X}] = \mu$, and if all samples are independent,
$Var[\bar{X}] = \sigma^2/n$.
However if we do not know $\sigma^2$ a priori, and use instead the sampling
variance 
$$ s^2 = \frac1{n-1} \sum_{i=1}^n (X_i - \bar{X})^2$$, the distribution becomes
\\[ \frac{\bar{X} - \mu}{s/\sqrt{n}} \sim t(n-1) \\]

To apply a one-sample t-test to the parameters of a **linear regression**, the
variance is not scaled by the square root of the number of samples. 
The standard error is calculated directly from the regression.
For an OLS, $Y = X.\beta +
\varepsilon$, with $\varepsilon \sim \mathcal{N}(0, \sigma^2 I)$, the parameters
are estimated by $b = (X^T \cdotp X)^{-1} (X^T \cdotp Y) = \beta + (X^T \cdotp
X)^{-1} X^T \varepsilon$. The variance of the estiamte $b$ is then $Var[b] =
\sigma^2 (X^T \cdotp X)^{-1}$. Since $\sigma^2$ is unknown, we use instead the
sampling variance $s^2 = \frac1{n-1} \sum_{i=1}^n (y_i - \hat{y}_i)^2$, where
$\hat{y}_i$ is the estimate for $y_i$.

#### Independent two sample t-test
We can use an [independent two sample
t-test](https://en.wikipedia.org/wiki/Student%27s_t-test#Independent_two-sample_t-test)
to compare the population mean of two populations, when the samples for each
population do not have a clear connection with each other. We'll look at the
case of the dependent two-sample t-test afterward.
Again, we typically do not
know the variance of each population and must resort to the sampling variance,
which leads to a Student's t distribution. The statistic we use here is
\\[ \frac{ \bar{X}_1 - \bar{X}_2}{s_d} \sim t(df) \\]as 
where $s_d$ is the standard deviation and $df$ is the number of degrees of
freedom. The correct values to use depend on the situation.

**If the two populations have the same variance**, we can use a [pooled sample
variance](https://en.wikipedia.org/wiki/Pooled_variance) $s_p$ to compute $s_d$, i.e., 
\\[ s_d = s_p \sqrt{1/n_1 + 1/n_2}, \\] 
where $$s_p^2 = (\sum_i (n_i-1) s_i^2) / (\sum_j (n_j-1))$$, and 
\\[ df = n_1 + n_2 - 2 \\]

**If the two populations have different variance** (and in the general case
different number of samples), then
\\[ s_d = \sqrt{s_1^1/n_1 + s_2^2/n_2} . \\]
The exact distribution in that case is a mess, but for all practical cases it
can be approximated by a Student's t-test with degrees of freedom
\\[ df = \frac{(s_1^1/n_1 + s_2^2/n_2)^2}{(s_1^2/n_1)^2/(n_1-1) +
(s_2^2/n_2)^2/(n_2-1)} \\]


**A dependent t-test for paired samples** is when two samples are related to
each other, for instance, if those are the same patients before and after a
treatment. In that case, the solution is to test the difference of the pairs in
a one-sample t-test.


## Chi-square tests

There are a different flavours of [chi-square
tests](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test).
I'm here looking at the goodness-of-fit, i.e., test if a categorical population
is distributed according to a theoretical distribution (null hypothesis). In
that case, Pearson's chi-square test is actually an approximation to the
[G-test](https://en.wikipedia.org/wiki/G-test),
\\[ G = 2 \sum_i O_i \ln (O_i/E_i) \sim \chi^2(df) \\]
where $O_i$ is the observed count for category $i$, $E_i$ is the expected count
for category $i$ (under the null). The degrees of freedom is $df = $ number of
categories $-$ (number of parameters in the distribution + 1); for instance, the
number of parameters for a uniform distribution is 0, for a standard normal is
2,$\dots$

How do we get to the chi-square test from a G-test? 
We use the expansion $\ln(1+u) \approx u - u^2/2$ when $|u|\ll 1$.
If we assume that $O_i$ and
$E_i$ are close to each other, then 
\\[ O_i \ln(E_i/O_i) = O_i \ln \left( 1 + \frac{E_i-O_i}{O_i} \right)
\approx (E_i - O_i) - \frac{(E_i-O_i)^2}{2O_i} \\]
Going back to the G statistic, and using the fact that $\sum_i E_i = \sum_i
O_i$, we have
\\[ G = -2 \sum_i O_i \ln (E_i/O_i) 
\approx \sum_i \frac{(O_i-E_i)^2}{O_i} \\]
which is the chi-square test.


## ANOVA test

I won't go much in details. The [ANOVA
test](https://en.wikipedia.org/wiki/Analysis_of_variance) can be seen as a
generalization of a two-sample t-test to the case of multiple populations.
There is also a whole chapter dedicated to it in Casella & Berger's Statistical
Inference textbook.


## Ljung-Box test

The [Ljung-Box](https://otexts.org/fpp2/residuals.html) test is a portmanteau
test to test the correlation of a time-series. It allows to test whether
the first $h$ auto-correlations of a time-series are like white noise (null) or
not (serial correlation). We define the statistic
\\[ Q = n (n+2) \sum_{k=1}^h \frac{\hat{\rho}_k^2}{n-k} \sim \chi^2(h) \\]
where $\hat{\rho}_k$ is the lag-k sample autocorrelation. Note that this is a
one-sided test.


## Unit root test

If a time-series has a unit root, it is, among other things, non-stationary.
For instance, we can test for the presence of a unit root to decide whether a time-series
needs to be differencied or not.
The Dickey-Fuller test is a popular test for unit roots.
