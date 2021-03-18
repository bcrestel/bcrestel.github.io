---
layout: post
title: Sample from categorical distribution
tags: distributions probabilistic
---

It is possible to (approximately) sample from a categorical distribution in a continuous, differentiable form. This [ICLR 2017 paper](https://arxiv.org/pdf/1611.01144.pdf) introduces the Gumbel-Softmax distribution which relies on the [Gumbel distribution](https://lips.cs.princeton.edu/the-gumbel-max-trick-for-discrete-distributions/) to sample one-hot vectors from a categorical distribution.

The blog post I linked shows how the Gumbel-Max trick is equivalent to a softmax output. And the paper shows that you can sample.

This Gumbel-Softmax distribution can be used for neural architecture search, like for instance
the Differentiable Neural Architecture Search ([DNAS](https://arxiv.org/pdf/1812.03443v3.pdf)).
