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

Activation which is passed from one step to the next is called $a$.
Typically set $$a^{<0>}=0$$, then
$$a^{<t>} = g_1(W_{aa} a^{<t-1>} + W_{ax} x^{<t>} + b_a)$$. 
Activation function
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
DeepAR is predicting). This is the case of music generation, for example.
* many-to-one: You have multiple intputs, but only one output you care about.
In that case, you only care about the last output.
This is the case of sentiment analysis, for example.
* many-to-many ($T_x=T_y$): standard case where each input gives an output, at
each step. There is a potential limitation that the output only depends on the
previous steps; but this can be remedied with bidirectionnal RNNs (or LSTMs).
* many-to-many ($T_x \neq T_y$): in that case, you want to use an
 encoder-decoder architecture. That is, you first pass all of the inputs
($T_x$), without using the outputs. Then after passing the input, you start
generating the output (most likely feeding each output as an input at the next
step).

This list does not include attention, which is covered in week 3.

## Video: Language model and sequence generation

Language model returns the likelihood of a sentence; this can used to decide
what was most likely said for instance (by comparing likelihood of 2 sentences).

To do that, you can formulate it as a many-to-many RNN, where the output of
the RNN is passed through a softmax and is trained to predict the probability of
the next word, given the first few words in the sentence, $$P(y^{<t>} |
x^{<1>},...)$$. Because you now have a lag, you start with the first input being
0, ie, $$x^{<0>}=0$$.

You define the loss at each time step to be $$-\sum_i y_i log(\hat{y}_i)$$
(cross-entropy loss), with
$y_i$ being non-zero (ie, 1) only for the true word. Then for the overall loss you
sum over all time steps. That is equivalent to the log-likelihood of the
probability of that sentence, as you recursively condition on the previous works
in the sentence. That is
$$log P(x_1, x_2, x_3) = log P(x_3|x_1,x_2) + log P(x_2 | x_1) + log P(x_1)$$.

## Video: Sampling novel sequences

Sample from a trained language model (see previous video). You sample by
recursively sampling a word from your language model, then plugging it back into
your model as an input for the following step.

## Video: Vanishing gradients with RNNs

Deep neural networks are hard to train as they lead to vanishing/exploding
gradients. RNNs are no different; long sequences will make it resemble a deep
neural networks. If vanishing gradients can be hard to spot, exploding gradients
will lead to extremely large parameters (potentially NaN) and can be remedied by
gradient clipping (re-scaling the gradient so that its norm does not exceed a
fixed threshold).

## Video: Gated Recurrent Unit (GRU)

The main idea is to introduce a memory cell $c$ to try and keep information for
longer number of steps.
In GRU, $c$ directly replaces the activation $a$. It is updated in each cell by
taking a convex combination of its previous value and a tentative update
$\tilde{c}^t$,

$$c^t = \Gamma_u * \tilde{c}^t + (1-\Gamma_u) * c^{t-1}$$,
where $\Gamma_u$ is a gate value between 0 and 1, and the multiplications are
point-wise.  It is given by
$$\Gamma_u = \sigma(W_u [c^{t-1}, x^t] + b_u)$$ where $\sigma$ is the sigmoid
function. The tentative update is given by 

$$\tilde{c}^t = tanh(W_c [\Gamma_r * c^{t-1}, x^t] + b_c)$$, with $\Gamma_r$ a
relevance gate 
$$\Gamma_r = \sigma(W_r [c^{t-1}, x^t] + b_r)$$.

## Video: Long Short Term Memory (LSTM)

It is slightly different from the GRU with 3 gates (update, forget, output) instead of 2, and the
relevance gate is replaced by direclty using the previous output. 

$$\Gamma_{u,f,o} = \sigma(W_{u,f,o} [a^{t-1}, x^t] + b_{u,f,o})$$. 
Notice that
instead of $c^{t-1}$ in the gates, we now use $a^{t-1}$.

Now the udpate becomes

$$c^t = \Gamma_u * \tilde{c}^t + \Gamma_f * c^{t-1}$$. 
The $\tilde{c}$ is calcultaed in terms of $a^{t-1}$ instead of $c^{t-1}$, 

$$\tilde{c}^t = tanh(W_c [a^{t-1}, x^t] + b_c)$$.
And the output is

$$a^t = \Gamma_o * tanh(c^t)$$.

A really good reference for GRU and LSTM is [Colah's blog post on
LSTM](https://colah.github.io/posts/2015-08-Understanding-LSTMs/). There, he
uses
the more typical notation for LSTM and calls $h^t$ the output (instead of $a^t$).

## Video: Bidirectional RNN

Unroll input forward and backward (not backprop though). Then concatenate output
from both directions and pass to linear layer to generate output of each step.

Can also have Bidirectionnal LSTM or GRU. Actually BLSTM is very popular for
many NLP tasks.

Disadvantage: you need entire sequence before making a prediction. This can be
a problem for certain applications (eg, speech recognition).

## Video: Deep RNNs

You can stack layers of RNNs/LSTMs/GRUs on top of each other.
For each layer, the input stacks its activation from the previous step with the
output from the layer below at that same time steps. 


For RNNs, 3 layers is already quite a lot; so not very deep RNNs networks.
But sometimes, you find a bunch of RNN layers, then on top seats a fc deep
network.

# Week 2


