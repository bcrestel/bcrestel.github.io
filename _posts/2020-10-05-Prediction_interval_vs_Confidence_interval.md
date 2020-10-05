---
layout: post
title: Prediction interval vs Confidence interval
tags: statistics timeseries
---

Rob Hyndman has a blog [post](https://robjhyndman.com/hyndsight/intervals/)
where he details the difference between confidence interval, prediction
interval, and credible interval.

I think he makes an good point that confidence interval and prediction interval
are often used inter-changeably, even they are quite different. Confidence
interval comes from the realm of frequentist inference, and applies to a
parameter that has been evaluated using a statistical method. A 95% confidence
interval is an interval that will contain the true value of that parameter 95%
of the time, if we could repeat the experiment indefinitly.

A prediction interval is an interval for a predicted value. Not for a model
parameter. That predicted value does not exist yet (that's why we need to
predict it), and its uncertainty is represented by a random variable. A 70%
prediction interval will contain 70% of the mass of that random variable; or to
be more general, this would be the 70% HDI.

A credibility interval is kind of a mix between the two. It's the Bayesian
equivalent of a confidence interval, and therefore applies to the posterior
distribution of a model parameter. A 75% credibility interval is the 75% HDI of
the posterior distribution.
