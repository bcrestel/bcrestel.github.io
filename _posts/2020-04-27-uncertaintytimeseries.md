---
layout: post
title: Uncertainty, concept drift, and time series
tags: time-series drift
---

We want to quantify how much the prediciton of a foreacsting model should be
trusted. That is not the same as the uncertainty of the prediction. Under
dataset shift, a model can deliver a very confident wrong answer. The ultimate
goal would be to identify when the model is not capable of delivering an answer.
There are different ways of approaching that problem.

# Allow the model say "I don't know"

In the context of a multi-label classification model, we could imagine having an
extra label that would correspond to "I don't know". The problem with that
approach is that this model is still trained by supervised learning and
therefore doesn't have examples of data it hasn't seen (duh...). 

The alternative is to check how certain the model is about its prediction. In
the case of a classifier, one would be tempted to use the value of the softmax
layer, but it turns out this should not be trusted a measure of uncertainty (see
[Intriguing properties of neural networks](https://arxiv.org/pdf/1312.6199.pdf)
(2014), by Szegedy et al.,). On the other hand, if we have a [Bayesian
model](https://www.quora.com/How-can-one-make-the-artificial-neural-networks-say-I-dont-know-not-sure),
we propagate the uncertainty on the model parameters to the predicted quantity,
and use that uncertainty to decide whether we can trust the model or not. In the
case, where the model is very uncertain (rather flat predictive pdf), we can
conclude the model does not know.

A NeurIPS 2019 paper, [Can You Trust Your Model’s Uncertainty? Evaluating
Predictive Uncertainty Under Dataset
Shift](https://papers.nips.cc/paper/9547-can-you-trust-your-models-uncertainty-evaluating-predictive-uncertainty-under-dataset-shift.pdf),
compares different methods to estimate model uncertainty in the specific setting
of dataset shift.

# Out of Distribution detection

The other approach is to treat the problem as a dataset shift, i.e., trying to
detect that the data used for new prediction is from a different distribution as
the data used for training.

This is a problem that is addressed by concept drift, or change point detection:
* A fundamental paper is the one by Yamanishi & Takeushi, "Unifying Framework
 for Detecting Outliers and Change Points from Non-Stationary Time Series Data"
 [link](https://dl.acm.org/doi/pdf/10.1145/775047.775148).

This could also be done with (conditional) generative models, like an anomaly
detection problem. If a generative model trained on the training data is
unlikely to generate a given time series, then probably there has been a dataset
shift. This could be done with a model like DeepAR, or a GAN.
Alternatively, we could use an autoencoder and check how far the reconstruction
is from the original. For this, we could force a decomposition in latent space
into basis functions (like N-Beats). After a dataset shift, the basis functions
would be unlikely to remain the same.
