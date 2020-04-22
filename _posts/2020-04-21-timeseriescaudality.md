---
layout: post
title: Causality inference 
tags: causality 
---

In this post, I'd like to survey the main approaches to conduct causal inference. 
In the most general sense, The goal of causal inference can be phrased as the analysis of causes and
coutnerfactuals.
For researchers focused on medical experiments,
causal inference is often presented as the attempt to figure out the effect on
outcomes when different treatments are used (also called treatment effect, or
causal effect). This is the case of the Potential Outcome Framework.
Here treatment can be understood in the general sense of action, intervention, or
manipulation.
The most direct
way of doing this is randomized trials. However, due to the limitation  of this
approach (cost, time, ethics, impracticality), researchers focused on infering
causality from observational data, i.e., from data for which we have no way to
know why such or such treatments were administered; we can only see the treatment
and the effects.

# Comparison of the 2 main frameworks for causal inference

The two main frameworks for causal inference are
* Potential outcome Framework:
It is also known as the Neyman-Rubin Potential Outcome, or the Rubin Causal
Model.  In that framework, a potential "cause" must be manipulatable (e.g.,
intervention, treatment).  And if a cause has 2 options (take or do not take the
treatment), we can only observe one outcome every time. The Potential outcome
framework aims at estimating the other potential outcome and then calculate the
treatment effect. In that sense, the Potential Outcome Framework is focused on a
specific use of causality
There exists traditional statistical methods and more recent
machine learning methods that fit within that framework.  It includes propensity
scores and instrument variables
([source](http://www2.stat.duke.edu/~fl35/teaching/440-19F/Tutorial_PlusDS.pdf)).
A review [article](https://arxiv.org/pdf/2002.02770.pdf) about the Potential
Outcome Framework was published in 2020. In that review paper, the methods are
classified into 2 categories whether on 3 assumptions (re-weighting methods, matching methods,
tree-based methods, representation learning, multitask learning methods, meta
learning methods), or if they relax some of
them.
These 3 assumptions are: SUTVA (independence of the units receiving treatment, and
unicity of treatments administred), ignorability (treatment assignment done
independently from expected outcome; so random), and positivity (treatment assignmed
randomly for all background).  

* Structural causal models (SCM): 
Most papers draw a distinction between Potential Outcome Framework and SCM, but
[Pearl](https://projecteuclid.org/euclid.ssu/1255440554http://projecteuclid.org/euclid.ssu/1255440554)
claim that SCM is a general theory of causality, drawing from the structural
equation models (SEM), the Potential Outcome Framework, and [probabilistic
graphical models](/2020/04/14/bn)
The idea is to define a causal model that describe the causal
mechanism of the system.  The recommended survey paper for that framework is the
2009
[paper]
by Judea Pearl.

# The special case of causal inference with Time series data
% TODO: Look at Runge
% [thesis](https://edoc.hu-berlin.de/bitstream/handle/18452/17669/runge.pdf?sequence=1),
% especially the litt review
% Keep in mind the blog post
% https://towardsdatascience.com/inferring-causality-in-time-series-data-b8b75fe52c46#2c77
% PCMCI (derived from PC:
% https://cse.sc.edu/~mgv/csce582sp14/presentations/SpirtesGlymourPC.pdf):
% https://advances.sciencemag.org/content/advances/5/11/eaau4996.full.pdf along
% with the repo https://github.com/jakobrunge/tigramite
% and the website: https://causeme.uv.es/
% (maybe) recent paper from Runge:
% https://www.nature.com/articles/s41467-019-10105-3.pdf
% Good review paper on statistical methdods (Granger-causality): "Simulation Study of Direct Causality Measures in Multivariate
% Time Series" 


# Other references

* A survey [paper](https://arxiv.org/pdf/1809.09337.pdf) published in 2019 focuses
specifically on inferring causality from observational data, and discuss both
cross sectional and temporal data. It didn't have much citations however.
