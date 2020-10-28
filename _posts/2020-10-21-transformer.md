---
layout: post
title: Transformer
tags: deeplearning attention nlp
---

I started looking into the Transformer model. It was first introduced in the
paper [Attention is all you
need](https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf). I don't
have time to dive into the details, but one key part of the paper is the
generalization of the concept of attention. In the
[paper](https://arxiv.org/pdf/1409.0473.pdf) that made attention works,
attention is applied to an encoder-decoder model, and the attention score is
calculated as a linear combination of all the hidden states of the encoder. That
linear combination is calculated by another neural network (feedforward, I
believe) that takes as input the current hidden state of the decoder and all the
hidden states of the encoder). The output is then passed to a softmax, then that
score multiply each hidden states of the encoder, which we call the values. So
the attention score is
\\[ Attention = \sum_i Scores_i  Values_i \\]
where $Scores \in \mathbb{R}^n, Values \in \mathbb{R}^{n \times d_v}$, and $d_v$
is the number of hidden cells.

The problem of that approach is that you actually calculate each attention score
one point at a time, so if you have $m$ words in your input sequence and $n$
words in your output sequence, you'll pass through that network $m \times n$,
which can get slow pretty quickly.
So in the Tranformers paper, the authors replace the scores generated by a
neural network with a dot product. To do so, they introduce the new concepts of
queries and keys. One analogy that I heard to describe is that would like a
fuzzy lookup in a dict: if your query matches a key, no problem, but if not,
this fuzzy dict will return a mix of the values whose keys resemble the most the
query. That is the idea of the attention mechanism.
So with symbols, the attention mechanism becomes
\\[ Attention = \text{softmax}(\frac{Q K^T}{\sqrt{d_k}}) V \\]
where $Q \in \mathbb{R}^{m \times d_k}, K \in \mathbb{R}^{n \times d_k}, V \in
\mathbb{R}^{n \times d_v}$.
In the initial attention paper, the keys and values are the same, the query is
the hidden cell from the decoder, and the dot
product $Q K^T$ is replaced with a neural network that takes $Q, K$ as inputs.

Additional References: 
* [Illustrated Transformer](http://jalammar.github.io/illustrated-transformer/)
* [stackexchange](https://stats.stackexchange.com/questions/421935/what-exactly-are-keys-queries-and-values-in-attention-mechanisms)