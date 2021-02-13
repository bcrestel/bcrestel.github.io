---
layout: post
title: Sequence Models by deeplearning.ai 
tags: rnn deeplearning course
---

# Week 1

## Video: Notation

$$x^{<t>}$$: $$t^\text{th}$$ entry in sequence $x$

$T_x$: length of sequence $x$

$$x^{(i)<t>}$$: entry $t$ in training example $i$.

Vocabulary, Dictionary: ordered list of all words used (10,000-1M).
Then each word in that vocabulary can be encoded via one-hot encoding.
For unknown words, you can have an "unknown" token.

## Video: RNN Model

Typically set $$a^{<0>}=0$$, then

Activation which is passed from one step to the next is called $a$.
$$a^{<t>} = g_1(W_{aa} a^{<t-1>} + W_{ax} x^{<t>} + b_a)$$. Activation function
typically tanh/ReLU.
Notation often condensed by stacking the matrices such that $W_a = [W_{aa},
W_{ax}]$.

Output of RNN layer at step t is called $y$.
$$y^{<t>} = g_2(W_{ya} a^{<t>} + b_y)$$. Activation function typically sigmoid.

Important details is that the weights $W_a, W_y$ are shared across all time
steps.

## Video: Backpropagation through time

Don't give much details, simply that the loss is the sum of an elementary loss
at each time step. Something that can be denoted by
$$ L(y, \hat{y}) = \sum_{t=1}^{T_y} L(y^{<t>}, \hat{y}^{<t>})$$.
When you back-propagate, you back propagate through time, ie, "from right to
left". Again, keep in mind that the weights are shared across all time steps.

## Video: Different types of RNNs

* one-to-one: not really an RNN; it's just a fc layer
* one-to-many: only have an input for the first step. After that first step, $$x^{<t>}$$ is 
replaced by the output generated in the previous step $$y^{<t-1>}$$ (like when
DeepAR is predicting). This is the case of music generating, for example.
* many-to-one: You have multiple intputs, but only one output you care about.
In that case, you only care about the last output.
This is the case of sentiment analysis, for example.
* many-to-many ($T_x=T_y$): standard case where each input gives an output, at
each step. There is a limitation that sometimes the output only depends on the
previous steps, but this can be remedied with bidirectionnal RNNs (or LSTMs).
* many-to-many ($T_x \neq T_y$): in that case, you want to use an
 encoder-decoder architecture. That is, you first pass all of the inputs
($T_x$), without using the outputs. Then after passing the input, you start
generating the output (most likely feeding each output as an input at the next
step).

## Video: Language model and sequence generation

Language model gives you probability of a sentence vs another, so you can decide
what was most likely said for instance.

To do that, you can formulate it as a many-to-many RNN, where the output is of
the RNN is passed through a softmax and is trained to predict the probability of
the next work, given the first few words in the sentence, $$P(y^{<t>} |
x^{<1>},...)$$. Because you now have a lag, you start with the first input being
0, ie, $$x^{<0>}=0$$.

You define the loss at each time step to be $$-\sum_i y_i log(\hat{y}_i$$, with
$y_i$ being non-zero (ie, 1) for the true word. Then for the overall loss you
sum over all time steps. That is equivalent to the log-likelihood of the
probability of that sentence, as you recursively condition on the previous works
in the sentence. That is
$log $P(x_1, x_2, x_3) = log P(x_3|x_1,x_2) + log P(x_2 | x_1) + log P(x_1)$$.
