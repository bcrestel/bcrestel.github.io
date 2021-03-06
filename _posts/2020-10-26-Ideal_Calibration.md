---
layout: post
title: Ideal Calibration
tags: probabilistic calibration
---

In the paper [Accurate Uncertainties for Deep Learning Using Calibrated
Regression](https://arxiv.org/pdf/1807.00263.pdf), the authors detail the ideal
calibration. For background, a calibration $R$ takes a distributional forecast
$H(x_t)$ ($=F_x$) and returns a better approximation to the true cdf $F(y)$. First of
all, an ideal forecast will possess the property that
\\[ F_x(y) = F_Y(y) =  \mathbb{P}[Y \leq y ] , \\]
or equivalently if $y = F_x^{-1}(p)$ with $p\in[0,1]$,
\\[ p = \mathbb{P}[Y \leq F_x^{-1}(p)]. \\]

Now a calibration is a function $R: [0,1] \rightarrow [0,1]$ that applies to the
output of the distributional model. Let's see what $R$ needs to be to improve
the approximation of the initial forecast. That is,
\\[ 
\mathbb{P}[Y \leq (R \circ F_x)^{-1}(p) ]  = 
\mathbb{P}[Y \leq F_x^{-1}(R^{-1}(p))] 
\\]
If we define $R$ as 
\\[ R(p) = \mathbb{P}[Y \leq F_x^{-1}(p)] \\]
then we have
\\[ 
\mathbb{P}[Y \leq (R \circ F_x)^{-1}(p) ]  = 
\mathbb{P}[Y \leq F_x^{-1}(R^{-1}(p))] = R(R^{-1}(p))=p
\\]
In some sense, $R$ corresponds to the corrected quantile for $Y$ when
approximated by the cdf $F_x$.
