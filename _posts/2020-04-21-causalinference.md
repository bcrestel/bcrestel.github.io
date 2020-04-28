---
layout: post
title: Causal Inference 
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

First up, [Inferring causation from time series in Earth
system](https://www.nature.com/articles/s41467-019-10105-3.pdf), by Runge and a
bunch of other people.
Because intervention are hard (impossible?) to put in place in Earth science,
there is a strong need to rely on recent data-driven methods (observational
causal discovery).
They give a few examples of situations where causality was used in Earth
science, in particular examples where Granger causality and/or correlation-based
methods failed to identify the correct causal links.
Next, they introduced the main methods for causality inference with time
seriesa. Many (?) causal inference methods for time series are grounded on a few
common assumptions: time-order (past events influence future events, not the
other way around), causal sufficiency (no unobserved common factor exists), for graphical
models the Causal Markov condition (conditional independence on all variables
who don't have a direct impact),...
They first introduce _Granger causality_, which is probably the foundational
method of causal inference in time series. The high-level idea to assess whether
variable X causes variable Y is to test whether knowledge of past values of X
help improve or not the prediction of future values of Y (reduction in residual
variance). Different variations of that idea have been developped over the
years, mainly depending on the type of model that is used to predict Y: AR,
nonlinear, or transfer entropy (a non-parametric statistic measuring the amount
of directed time-asymmetric transfer of information between 2 random processes;
the amount of information is measured using Shannon's entropy). One potential
limitation of Granger causality is that it can only detect "lagged causality",
i.e., causal relation coming from past data; if the idea is to apply a causality
screening prior to forecast, then this is probably sufficient as we'll only rely
on past information. On the other hand, Granger causality typically fails to
identify conditionally independent links. Also, multivariate extensions of GC
fail if too many variables are considered.
Next, they discuss _nonlinear state-space methods_, in particular convergent
cross-mapping (CCM) methods. These methods look for interactions in the
underlying dynamic process that generated the data. They don't say much about
that class of methods, except that CCM is not well suited for multivariate,
purely stochastic processes, as it doesn't explicitly condition on other
variables.
_Causal network learning algorithms_ use [probabilistic
graphical models](/2020/04/14/bn) (think Bayesian networks) to infer causality
structure. They work well in large-scale applications. There are 2 main families
of methods depending whether one starts from an empty graph and add links, or
one starts from a fully connected graph and remove links. The decision to
add/remove links is based on the results of some tests (e.g., conditional
independence statistical test, or some score function,...). They highlight 2
methods: PCMCI, designed to handle auto-correlated and nonlinear time series,
and FCI which does not rely on the Causal Sufficiency assumption.
Lastly, the _structural causal model (SCM) framework_, promoted by Judea Pearl.
Causal graphs cannot always identify the direction of contemporaneous causality
links (i.e., within the Markov equivalence class). SCM allows to make
assumptions about the possible causal relationships we accept.

Based on the literature review of the Runge paper above, let's focus on 2
specific causal network algorithms, PCMCI and FCI.
In the case of [PCMCI](https://advances.sciencemag.org/content/advances/5/11/eaau4996.full.pdf)
there is the added advantage that the authors provided
[code](https://github.com/jakobrunge/tigramite).
The claim to fame of PCMCI is its capacity to handle high-dimensional datasets
and highly interdependent time series, along with linear and nonlinear
relationship in the data. In the paper, they also show some robustness to
nonstationarity. The main shortcomings remain the reliance on the Causality
Sufficiency hypothesis.
The PCMCI algorithm builds on top of the PC algorithm. The latter is a Markov
discovery algorithm that relies on the causal Markov property to identify
parents of a variable. However, as shown in the paper, the PC algorithm cannot
be used as is with time series. So the authors add a momentary condition
independence (MCI) test after the PC step. The PC step (PC1) iteratively removes links
that are independent conditioned on the most important drivers in the previous
step. After that PC1 step, each variable is left with the causal parents and
potentially some false positives. The MCI step tests each potential causal link
and assess causal strenght. The MCI step conditions on the parents and the
parents of the potential parent tested (to account for autocorrelation).
The significance level to reject/accept the independence test in the MCI step is
the one parameter of the method that can be adjusted; it can selected via
typical techniques (information theory, or cross-validation).
Any kinf of conditional independence test can be used in this algorithm, whether
linear (e.g., linear partical correlation) or nonlinear (e.g., GPDC, or CMI).

In section 6 of the book [Causation, Prediction, and
Search](http://www.cs.cmu.edu/afs/cs.cmu.edu/project/learn-43/lib/photoz/.g/web/.g/scottd/fullbook.pdf)
by Spirtes et al, the authors introduce the Fast Causal Inference (FCI)
algorithm to conduct causal inference without relying on the Causal Sufficiency
condition. The main limitation of that algorithm is its computational
complexity. Therefore, a few different authors tried to improve on it. In
particular in [Learning high-dimensional directed acyclic graphs
with latent and selection
variables](https://projecteuclid.org/download/pdfview_1/euclid.aos/1333567191)
the authors introduce Really Fast Causal Inference (RFCI) that limits the number
of independence tests performed to reduce the computational complexity.

In [Granger causality for state space
models](https://arxiv.org/pdf/1501.06502.pdf), the authors show that
Granger-causality should be tested via a state-space model, instead of an AR
model as is typically the case, as in most cases the data contain a moving
average part that yield spurious results. The state-space model doesn't suffer
from that problem.


[//]: TODO: Look at Runge
[//]: [thesis](https://edoc.hu-berlin.de/bitstream/handle/18452/17669/runge.pdf?sequence=1),
[//]: especially the litt review
[//]: Keep in mind the blog post
[//]: https://towardsdatascience.com/inferring-causality-in-time-series-data-b8b75fe52c46#2c77
[//]: Good review paper on statistical methdods (Granger-causality): "Simulation Study of Direct Causality Measures in Multivariate Time Series" 


# Other references

* A survey [paper](https://arxiv.org/pdf/1809.09337.pdf) published in 2019 focuses
specifically on inferring causality from observational data, and discuss both
cross sectional and temporal data. It didn't have much citations however.
