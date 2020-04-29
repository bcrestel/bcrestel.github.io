---
layout: post
title: Confidence score for time series prediction
tags: time-series uncertainty
---

A confidence score can be defined as a metric to quantify how certain one can be
about a model prediction. As described in [Confidence Scoring Using Whitebox
Meta-models with Linear Classifier
Probes](https://arxiv.org/pdf/1805.05396.pdf), this does not have to be a
probability; but it needs to relate to the uncertainty in the prediction. 
At a high level, this can summarized as asking the network to tell us when it
"doesn't know".


There are 2 main schools of thought to solve that problem. The first is to use
the output of the model (along with some uncertainty) directly. And the second
is to develop a meta-model on top of the prediction model to estimate that
uncertainty.

# Using the output of the model directly

With a classifier model, one could use the values of the softmax layer as a
quantification of uncertainty. Unfortunately, and at least with modern deep
networks, it appears that networks are not well calibrated anymore.
[temperature scaling](https://arxiv.org/pdf/1706.04599.pdf) offers a simple way
to re-calibrate a network.  Another approach would be to work with a [Bayesian
model](https://www.quora.com/How-can-one-make-the-artificial-neural-networks-say-I-dont-know-not-sure),
and use the predictive uncertainty as a measure of confidence. In addition to
variational inference, multiple methods have been designed over the last few
years to come up with approximately Bayesian models, like [Dropout as a Bayesian
Approximation](http://proceedings.mlr.press/v48/gal16.pdf) or
[SWA-Gaussian](https://papers.nips.cc/paper/9472-a-simple-baseline-for-bayesian-uncertainty-in-deep-learning.pdf).

Remains the question of how that would all work under dataset shift.
A NeurIPS 2019 paper, [Can You Trust Your Model’s Uncertainty? Evaluating
Predictive Uncertainty Under Dataset
Shift](https://papers.nips.cc/paper/9547-can-you-trust-your-models-uncertainty-evaluating-predictive-uncertainty-under-dataset-shift.pdf),
compares different methods to estimate model uncertainty in the specific setting
of dataset shift.


# Meta-model approach

In the meta-model approach, the idea is to train a second model (meta-model)
that sits on top of the classifier and is trained to decide whether the
classifier should make a prediction or not.

In [Selective Classification for Deep Neural
Networks](https://arxiv.org/pdf/1705.08500.pdf), the authors leverages the field
of selective prediction (or reject option).

The approach recommended in the paper, [Confidence Scoring Using Whitebox
Meta-models with Linear Classifier
Probes](https://arxiv.org/pdf/1805.05396.pdf), is to use a meta-model that will
learn to predict the "confidence score". They use [Linear Classifier
Probes](https://arxiv.org/pdf/1610.01644.pdf) to extract information from the
layers of a neural network image classifier, and train a confidence score
predictor. They compare the performance of their model (with or without probes
into the hidden layers, and using logistic regression or gradient boosting)
against the selective prediction technique described in [Selective
Classification for Deep Neural Networks](https://arxiv.org/pdf/1705.08500.pdf).
They train the classifier and the meta-model on different datasets. Then
validate hyperparameters on a validation set. And finally used the test set for
held-out performance reporting. In some cases, they introduce noise in the
labels of the training set, so that the classifier is poorly trained.  They also
test out of distribution by passing, at test time, images with labels that were
not in the training set.  The model with probes and GBM perform only slightly
better (AUC) than the softmax. But not by a shockingly large margin. The gap
widens in the case of out-of-sample noisy labels. They also compare with
[temperature scaling](https://arxiv.org/pdf/1706.04599.pdf), and claims that
temperature scaling did not modify the results much.  Anyway, it's an
interesting approach that our XAI team has pursued. They obtained great results,
but did not test it in the context of dataset shift.



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


