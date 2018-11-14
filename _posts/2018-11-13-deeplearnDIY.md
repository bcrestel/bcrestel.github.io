---
layout: post
title: DIY Deep Learning
tags: deeplearning ML optimization python
---

As a learning tool, and inspired by that interesting
[article](https://arxiv.org/abs/1801.05894), I want to build my own artificial
neural network in Python.

## Notations

The first step is define all the notations I'm going to use.
**Layers** are indexed by $l=0,1,\dots,L$. 
The input layer is indexed by $0$, and the output layer is $L$. In each layer $l$,
we have $n_l$ **neurons**, each producing an output $a^l_i$ for $i=1,\dots,n_l$.
All outputs from layer $l$ are stored in the vector ${\bf a}^l =
[a^l_1,\dots,a^l_{n_l}]^T$.
In layer $l$, each neuron takes an affine combination of the $n_{l-1}$ outputs
from the previous layer, then pass them through an **activation function** 
$f: \mathbb{R} \rightarrow \mathbb{R}$ 
to produce the $n_l$ outputs. The **weights** of the linear
combination are denoted ${\bf w}^l_i= [w^l_{i1}, \dots, w^l_{in_{l-1}}]^T$ 
and the **constant** is denoted $b^l_i$, such
that

$$ a^l_i = f(({\bf w}^l_i)^T {\bf a}^{l-1} + b^l_i ) $$

Let's shorten the notations a bit using vectorial notations. Let's define the total
activation function for layer $l$ as $F^l: \mathbb{R}^{n_l} \rightarrow
\mathbb{R}^{n_l}$ with $F^l(x) = [f(x_1), \dots, f(x_{n_l})]^T$. Let's
introduce the weight matrix at layer $l$, ${\bf W}^l = [{\bf w}^l_1, \dots, {\bf
w}^l_{n_l}]^T \in \mathbb{R}^{n_l \times n_{l-1}}$, 
and the constant vector ${\bf b}^l = [b^l_1, \dots, b^l_{n_l}]^T$.
We can then write, for $l=1,\dots,L$,

$$ {\bf a}^l = F^l \left({\bf W}^l \cdotp {\bf a}^{l-1} + {\bf b}^l \right) $$

I'll introduce one last variable to simplify the notation. Let's call ${\bf
z}^l$ the input for layer $l$, i.e.,

$$ {\bf z}^l = {\bf W}^l \cdotp {\bf a}^{l-1} + {\bf b}^l $$

Then we can write the activation at layer $l$ as,
$$ {\bf a}^l = F^l \left( {\bf z}^l \right) $$.

The only exception is for the input layer $l=0$ where $a^0$ is not calculated
but is an input variable.
At every layer, we therefore have $n_l (n_{l-1} + 1)$ parameters for a
grand total of $\sum_{l=1}^N n_l ( n_{l-1}+1)$ parameters in the entire network.

## Loss function

To train the network, we need to define a loss function. Let's assume we have
data $$\{ ({\bf x}_i,{\bf y}_i) \}_{i=1}^N$$, where ${\bf x}_i$ is fed in the input
layer and ${\bf y}_i$ is compared with the output of the network. The output of
the network is therefore a function of all parameters and the input variable,
i.e., $${\bf a}^L = {\bf a}^L( \{ {\bf W}^l, {\bf b}^l \}_l; {\bf x})$$.
For the loss function, I will use a least-square misfit, which leads to 

$$ L(\{ {\bf W}^l, {\bf b}^l \}_l) = 
\frac1{2N} \sum_{i=1}^N 
\| {\bf a}^L( \{ {\bf W}^l, {\bf b}^l \}_l; {\bf x_i}) 
- {\bf y}_i 
\|^2$$

To estimate the loss function, we simply plug, for each data pair $({\bf x}_i,
{\bf y}_i)$, the input ${\bf x}_i$ in the input layer, i.e., we set ${\bf a}^0 =
{\bf x}_i$, then propagate that forward recursively

$$ \begin{align*}
{\bf a}^1 & = F^1({\bf W}^1 {\bf x}_i + {\bf b}^1) \\
{\bf a}^2 & = F^2({\bf W}^2 {\bf a}^1 + {\bf b}^2) \\
\vdots & \\
{\bf a}^L & = F^L({\bf W}^L {\bf a}^{L-1} + {\bf b}^L) 
\end{align*} $$


## Calculating derivatives

To minimize the loss function, we need to calculate derivatives of that loss
function $L$ with respect to the parameters ${\bf W}^l$ and ${\bf b}^l$ at each
layers. This is done via the backpropagation algorithm; for more details on the
backpropagation, see this <a href="/2018/11/13/backprop">post</a>.
The main results are that, after a forward propagation (see previous section),
the gradient of the loss function with respect to all parameters can be
recursively calculated starting from the output layer $L$ by using the formulas

$$ \begin{align*}
\frac{\partial L}{\partial {\bf b}^L} & = \frac1N \sum_{i=1}^N
\begin{bmatrix} f'( z_1^L )  & & 0 \\   &   \ddots & \\  0    &  &   f'(z_{n_L}^L)
\end{bmatrix} \cdotp ({\bf a}^L({\bf x}_i) - {\bf y}_i) \\
\frac{\partial L}{\partial {\bf b}^l} & = \begin{bmatrix}
f'( z_1^l )  & & 0 \\   &   \ddots & \\  0    &  &   f'(z_{n_l}^l)
\end{bmatrix} \cdotp ({\bf W}^{l+1})^T \cdotp \frac{\partial L}{\partial {\bf
b}^{l+1}} , \quad \forall l=1,\dots,L-1\\
 \frac{\partial L}{\partial {\bf W}^l} & =
\frac{\partial L}{\partial {\bf b}^l} \cdotp ({\bf a}^{l-1})^T , \quad \forall l=1,\dots,L
\end{align*} $$
