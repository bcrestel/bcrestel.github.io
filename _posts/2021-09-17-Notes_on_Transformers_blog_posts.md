---
layout: post
title: Notes on the Transformer architecture
tags: transformers
---

Simon Prince put togethe a 3-parts series of blog posts about the Transformer architecture: [I](https://www.borealisai.com/en/blog/tutorial-14-transformers-i-introduction/?utm_source=pocket_mylist), [II](https://www.borealisai.com/en/blog/tutorial-16-transformers-ii-extensions/), and [III](https://www.borealisai.com/en/blog/tutorial-17-transformers-iii-training/).
I found the articles very clear and useful. I want to save a few notes that I took about these blog posts.

We assume we have $I$ inputs. Inputs could be words, tokens (elementary words that can be used to form all words in the dictionary), 
or something else it doesn't really matter. 
Each input is converted to its embedding which has dimension $D$. 
Such that, for NLP, if we want to pass a sentence, we can group each tokens in the sentence into a matrix $X \in \mathbb{R}^{I \times D}$.

Whereas attention was first introduced in the work of [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf?utm_source=ColumnsChannel), it was formalized in the paper [Attention is all you need](https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf) which introduced the Transformer architecture.
The main element is that the attention mechanism is split into 3 components: keys, queries, and values; vocabulary that comes from the field of information retrieval.
Informally, the query is what you are requesting (eg, the output of the decoder at the current step), the keys are what the queries are going to be compared with, and the values are what is going to be combined to generate the output.
The main aspect of the Transformer is the self-attention mechanism, which is to say that the same input is used for the queries and the keys.
Before being combined, the input $X$ is linearly transformed to a lower dimensional (column-)space through the matrices $\Phi_v, \Phi_k, \Phi_q \in \mathbb{R}^{D \times \tilde{D}}$, to obtain

$$ \begin{aligned}
X \cdotp \Phi_v & = V \in \mathbb{R}^{I \times \tilde{D}} \\
X \cdotp \Phi_k & = K \in \mathbb{R}^{I \times \tilde{D}}\\
X \cdotp \Phi_q & = Q \in \mathbb{R}^{I \times \tilde{D}}
\end{aligned}$$

Typically, $\tilde{D}$ is chosen such that it is lower than $D$, which reduces the computational cost of the linear algebra.
Once this transformation is done, the weights to combine the values are calculated by checking the similarity between the query and the keys (via a dot-product), 
$Q \cdotp V^T \in \mathbb{R}^{I \times I}$,
then normalizing the weights via a softmax (applied across each row independently),
$\text{softmax}(Q \cdotp K^T) \in \mathbb{R}^{I \times I}$.
Finally, we can apply these weights (that sum to $1$ for a given query, i.e., a given row) to the values

$$\text{softmax}(Q \cdotp K^T) V \in \mathbb{R}^{I \times \tilde{D}}$$
