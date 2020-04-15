---
layout: post
title: CausalNex, a toolkit for causal reasoning
tags: causality python
---

[CausalNex](https://causalnex.readthedocs.io/en/latest/index.html) is a library
developped by QuantumBlack to facilitate the causal analysis of a dataset.  At
its root, CausalNex relies on Bayesian Networks.  
For more on Bayesian Networks, have a look at
[Wikipedia](https://en.wikipedia.org/wiki/Bayesian_network) and a
[tutorial](https://www.cs.ubc.ca/~murphyk/Bayes/bnintro.html) by Kevin Murphy.
The training of these Bayesian
Networks (causal inference) uses the algorithm introduced in the paper [DAGs
with NO TEARS](https://arxiv.org/pdf/1803.01422.pdf).

# Installation

The [documentation](https://causalnex.readthedocs.io/en/latest/02_getting_started/02_install.html) is pretty clear.
The library can be easily installed by doing `pip install causalnex`.
Note that for some reason (not clear to me), we can't install via `poetry`.
Also, `causalnex` requires `pandas=0.24.0`, which seems to be a problem with the
current project.

Last, but not least, `causalnex` requires the library `pygraphviz` which has to
be installed separately. And of course, `pip install pygraphviz` returns an
error. I ended up having to install everything but `causalnex` via `conda` the
`pip install causalnex`. But this may not be convenient for everyone, and it's
weird that the library is so finicky.

# Tutorial

The documentation contains (for now) a single
[tutorial](https://causalnex.readthedocs.io/en/latest/03_tutorial/03_tutorial.html#)
that I will go through.
The first thing we need to do is download the
[dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip), and unzip it.

