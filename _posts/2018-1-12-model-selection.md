---
layout: post
title: AIC in linear regression
tags: statistics model_selection regression
---

Model selection is a central problem of statistical inference, whether you have to choose the independent variables to include in your linear regression, or compare between completely unrelated techniques.
In the context of linear regression, using $R^2$ to compare models would lead to over-fitting, and even the adjusted \$R^2\$ does not necessarily penalize larger models sufficiently.
An army of other methods exist (see [here](http://www.modelselection.org/model-selection.pdf)), among which 3 really stands out:
* cross-validation: it comes in many different flavours, but at its core, the idea is to leave out some of your training data to later test your model on. You can repeat the procedure leaving different distinct datasets, or not.
One obvious disadvantage of cross-validation is its potential computational cost, especially if you want to exhaust all possible splitting of the parameter space. 
However, in the case of linear regression, the cross-validation error can be
computed directly after solving the regression. 
Also, cross-validation is more restricted when applied to time-series data.
* Akaike Information Criterion (AIC) and Bayesian Information Criterion (BIC): these two criteria do explicitly penalize models with large number of parameters.
  * AIC: It is generally given as
  \\[ AIC(\beta) = 2k - 2\ln(\mathcal{L}) \\]
  where $k$ is the number of parameters and $\mathcal{L}$ is the likelihood at the MLE.
  * BIC: the BIC criterion imposes a stronger penalty on the number of parameters of the model,
  \\[ BIC(\beta) = \ln(n) k - 2\ln(\mathcal{L}) \\]
These two criteria are extremely popular; one disadvantage is their reliance on the Likelihood function which requires a specific distributional assumption.


Just as an exercise, let us derive the AIC in the case of linear regression. For the linear regression, assuming Gaussian noise $\varepsilon \sim \mathcal{N}(0, \Sigma)$, we have $ Y = X \cdotp \beta + \beta $.
The log-likelihood function is then given by
\\[ \ln(\mathcal{L}) = -\frac12 \left( \ln( \det(2\pi \Sigma) ) \right) - \frac12 (Y - X \cdotp \beta)^T \Sigma^{-1} (Y - X \cdotp \beta) \\]
In the case of iid normal noise, i.e., $\Sigma = \sigma^2 I$, we have
\\[ \ln(\mathcal{L}) = -\frac12 \left( n \ln( 2\pi \sigma^2 ) \right) - \frac1{2\sigma^2} e^T e \\]
where $e = Y - X \cdotp \beta$ and $n$ is the number of observations. 
Let us denote by $\hat{\beta}$ the MLE (and $\hat{e}=Y-X \cdotp \hat{\beta}$)
As we typically do not know the value of $\sigma^2$, we instead estimate it with the standard error $s^2 = \frac{e^Te}{n}$. This gives
\\[ AIC = 2k+n + n \ln(2\pi) + n \ln \left( \frac{\hat{e}^T\hat{e}}{n} \right) = n \left[ 1 + 2\ln(2\pi) + \frac{2k}n + \ln \left( \frac{\hat{e}^T\hat{e}}{n} \right) \right]. \\]
As a comparision, in Greene (2005) they use $2k/n + \ln(e^Te/n)$, which is, up to constant terms that do not vary in-between models, the same.
An additional reference for model selection in regression is [here](http://statweb.stanford.edu/~jtaylo/courses/stats203/notes/selection.pdf).

In a future post, I'd like to talk about [model averaging](https://arxiv.org/pdf/1709.08221.pdf).
