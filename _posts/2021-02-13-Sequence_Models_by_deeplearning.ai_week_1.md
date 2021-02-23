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

## Video: Word Representation

One-hot encoding does not give any indication about the similarity between 2 words. They all have the same distance with each other.

Another way to represent words is to use an embedding, ie, a lower-dimensional vector representation, where words with similar meaning are (hopefully) close to each other.

Also mention t-SNE that is a way to visualize in 2D very high dimensional data (eg, word embeddings).

## Video: Using Word Embeddings

Transfer learning and word embeddings:
1. Train word embeddings from large corpus online (1B-100B words); or even use pre-trained word embedding
2. Transfer embedding to new task with smaller training set (~100K words). For instance, use word embedding as input for name recognition algorithm -> word embedding should simplify task as it recognizes similar words and present them as similar input to your model.
3. (Optional) fine-tune word embedding with new data.

Transfer Learning typically useful when you have lots of data for task 1, but limited data for task 2.

Relation to face encoding: encoding (as in face encoding) ~ embedding (as in word embedding). 

## Video: Properties of word embeddings

Word embedding can learn analogies between words (eg, man->king, woman-> queen).

Note that t-SNE is a non-linear mapping (or rather, not an isometry), the geometrical properties found in high-dimensions are not preserved with t-SNE.

How to measure similarity between vectors?
* Cosine similarity (inner product divided by product of norms)
* squared norm of the difference between 2 vectors

## Video: Embedding matrix

Can store all your embeddings into a matrix of dimension "embedding dim" (row) x "number of words in corpus" (col). So if you right-multiply this embedding matrix by a one-hot encoder, you recover the embedding for that word.

## Video: Learning word embeddings

Alg for learning word embedding have been simplified over time. But it's informative to look at the first, more complex, algorithms.

You can learn word embedding by building a neural language model. In [A neural probabilistic language model](https://www.jmlr.org/papers/volume3/tmp/bengio03a.pdf), the authors build a simple neural network that takes a sentence, convert each word to its embedding, pass it through a linear layer, then a softmax to predict which one is the next word. You can train the entire network (weights and embeddings) on all text data you have, using SGD/Adam/...
Sometimes, people will only use the last few (eg, 4) words to predcit the next (instead of the whole sentence).

Sometimes, people also use words before and after (eg, 4 words before, 4 words after) to predict the word in the middle. Or you could use only the last word. Or even use a nearby 1 word (idea of a skip-gram model).

In the end, to build a language model, use the last N-words. But if you just want to build a word embedding, then you can use any of the other contexts mentioned here (words around, last 1-word, nearby 1-word,...).

## Video: Word2Vec

Introduce the skip-gram model used to build a Word2Vec representation. This
[blog
post](https://kelvinniu.com/posts/word2vec-and-negative-sampling/)
provides a nice introduction. The basic model is very simple. It is basically
the succession of 2 matrix multiplication. The first one by a matrix of size
$\mathbb{R}^{N \times d}$ converts a one-hot encoder representation of a word
(corpus of dimension N) into a word embedding (dim d). The second one does the
opposite and has dimension $\mathbb{R}^{d \times N}$. That last layer is
followed by a softmax, $e^{x_i}/\sum_j e^{x_j}$, for each potential output word
$i$. The loss if the typical
cross-entropy loss, that is $-\sum_k y_k \text{log}(\hat{y}_k)$, where $y \in
mathbb{R}^N$ is zero everywhere except for a single entry.

For any sentence, the input (context) is a random word, and the quantity we are trying to
predict is any word in that same sentence, within a certain window around the
input word. That output word is taken at random. In the end, it doesn't really
matter as we're not trying to predict that word, we are just trying to build an
embedding.

The problem of that approach is that it is extremely slow due to the need to
sum over all $N$ outputs of the softmax for every prediction. A workaround is to
use a hierarchical approach.
But better methods have been designed and will be presented in the next videos.

Original paper: [Efficient Estimation of Word Representations in
Vector
Space](https://arxiv.org/pdf/1301.3781.pdf%C3%AC%E2%80%94%20%C3%AC%E2%80%9E%C5%93)

## Video: Negative Sampling

Reference paper: [Distributed Representations of Words and Phrases
and their Compositionality](https://arxiv.org/pdf/1310.4546.pdf),)

That previous [blog
post](https://kelvinniu.com/posts/word2vec-and-negative-sampling/) also covers
negative sampling.

Actually, the blog post and the video kind of differ about the exact details of
the implementation. So we can also look at [Manning's
notes](https://web.stanford.edu/class/cs224n/readings/cs224n-2019-notes01-wordvecs1.pdf).

In the end, the idea is to not look at all $N$ words in the vocabulary, but only
the one true word that matches the context and a small number (5-20) of words
that are not correct. 
You therefore turn to a small number of binary classifications.
You can hence use a sigmoid loss to force your network to
have the true word match the output and the other words return 0.
The actual details seem to be that the sigmoid loss is applied to the inner
product between the embeddings of both words. Words that are close in a sentence
are assumed to be similar.

## Video: GloVe word vectors

[GloVe = Global Vectors for Word
Representations](https://web.stanford.edu/class/cs224n/readings/cs224n-2019-notes02-wordvecs2.pdf)

GloVe builds from the co-occurrence matrix $X_{ij}$ which counts how often word
$i$ falls within the vicinity of word $j$. Then we train the word embedding so
that the inner product between 2 words match (more or less) the logarithm of
their co-occurence. The match is enforced by a square loss, and a weighting term
is placed in front, which also takes care of cancelling the loss when
$X_{ij}=0$.

## Video: Sentiment Classification

Typical situation is that you don't have that many reviews to train your
sentiment classifier. But you were able to use a very large dataset to train
your word embedding. So you can use the embedding of the words in your review
(instead of the words direclty) to learn a more robust sentiment classifier with
a small dataset.

Also, you could just average the embeddings of all the words in your sentence,
then pass it through a softmax layer (for each of the possible ratings). But
this doesn't take the order into account. A better way is to pass the embeddings
of each word to a LSTM and output a classification at the very end
(many-to-one).

## Video: Debiasing word embeddings

Bias is likely to creep into the dataset used to train a Word2Vec. So it's
important to be aware of it, and if possible remove that bias.

One way this can be done is by
1. identifying the bias directions: for instance for gender bias, take all the
gender directions (boy - girl, king - queen, ...), and take the average
2. Neutralize: all words that should be free of gendre bias, just project them
perpendicularly to the gender directiojn
3. Equalize: some words are associated to gender, but should be at the same
distance to gender-free words (eg, nurse shouldn't be closer to woman than man).
So you can also fix that


# Week 3

## Video: Basic Models

Introduced 2 types of models:
* Sequence-to-sequence: this can be used for text translation. This uses a
 encoder-decoder architecture, which is a many-to-many architecture with $T_x$
and $T_y$ that are different. So you just pass the input to your LSTM, without
paying attention to the output generated (encoder), then start generating the $T_y$
outputs by feeding any genereated token back to the LSTM (decoder).
* Image Captioning: You can automatically generate captions from an image, by
 using a similar idea. You would simply replace the encoder in the previous part
with a CNN (eg, AlexNet) w/o the output (softmax) layer and feed the generated
embedding of that image into an LSTM, that would then produce the caption.

## Video: Picking the most likely sentence

In machine translation, the encoder-decoder architecture can be interpreted as a
condition language model. That is the decode part looks very much like a
language model, but instead of being instantiade by a hidden cell of zeros, it
is instantiated by the output of the encoder part.

When generating a translation, you don't want to sample the joint probability
distribution of your decoder at random. You instead want to pick the most likely
translation, i.e., $\arg \max P(y_1, y_2, \ldots | x)$. A naive approach is to
pick each most likely work successibley, ie, $\hat{y}_1 = \arg \max P(y_1|x)$,
then $\hat{y}_2 = \arg \max P(y_2 | \hat{y})_1, x)$,... However, this tends to
return sub-optimal results. Instead, the correct approach is to search the joint
probability space directly. This space, unfortunately, is too large to be
sampled exactly. For instance, imagine your look for the most likely 10 words
translation with a vocabulary of 10,000 words, that means $10,000^{10}$
possibilities. That's why we need to use an approxiamte search, eg, beam search.

## Video: Beam search

Beam search is an approximate search algorithm to search for the maximum of a
joint probability distribution.
The key parameter is the **beam width**, which defines the number of
most likely combinations that the beam search algorithm keep at each step. 
So for instance if the beam width is 3, then at each step $k$, beam search only
keeps the 3 most likely combinations of words (or partial sentences) when moving on to the next step
$k+1$, i.e, $(y_1^1, y_2^1,\ldots ,y_k^1), (y_1^2, y_2^2, \ldots, y_k^2),
(y_1^3, y_2^3,\ldots, y_k^3)$. At the next step, it only starts from these 3
combinations, then search for the 3 most likely combinations $(y_1,y_2,\ldots,
y_k, y_{k+1})$ across those 3 networks.
So at each setp, no matter after how many recursions, we only have to consider
$3N$ combinations, with $N$ the size of the vocabulary. Instead of $N^2$ with
the exhaustive search (not that $N^2$ is only at one step, but this compounds
with the depth).

Notice that when the beam width is set to 1, we recover the greedy algorithm
described in the previous video.

Ref: [Dive Into Deep Learning](https://d2l.ai/chapter_recurrent-modern/beam-search.html)

## Video: Refinements to Beam Search

Introduce length normalization. Beam search, as introduced before, tends to
favor short sentences as it searches to maximize the product of smaller numbers
(less than 1.0).
To circumvent that problem, a heuristic is to replce the joint probability by
$P^{1/T_y^\alpha}$ where $T_y$ is the length of the sentence and $0 < \alpha
\leq 1$. Since we typically maximize the log of the joint probability
distribution, and after writing the latter as a product of conditional pdf, we
get $1/T_y^\alpha \sum_i P(y_i | x, y_1, y_2,\ldots)$.

The optimal hyperparameter needs to be found empirically, as for the beam width.
$\alpha = 1$ will promote long sentences, while $\alpha=0$ will not normalize at
all. Beam width of $1$ will be like greedy search (cheap, but very sub-optimal).
On the other hand, a large beam width will yield much better results but at much
higher compute cost.

## Video: Error analysis in beam search

Now we have a model made of 2 parts: i) estimate the probability of the language
model (RNN); then ii) estimate the most likely sentence (beam search).
Using human translated sentences, you can check what part of your model (RNN or
Beam search) is at fault, then calculate the fraction of errors for each part.
You can then act on the faulty part of your model (modify model/add more
data/..., or increase beam width)

## Video: Bleu score

A pretty terrible video. Probably best to look at the [Wikipedia
page](https://en.wikipedia.org/wiki/BLEU).
Roughly, Bleu computed a modified precision for a machine-generated translation
compared to several reference (human-generated) translations.
There exists modification factors to penalize short translations.

## Video: Attention Model -- Intuition

Attention model replaces standard encoder-decoder architecture. The encoder is
still the same. However the decoder is a different network that at each step
takes as input a
combination of all the outputs from the encoder weighted by attention weights.
These attention weights tell the decoder on what part of the input it should
focus its attention. These weights are computed from the previous hidden values
and all the outputs of the encoder.

## Video: Attention Model


In the classical paper that introduced attention, [neural machine translation by jointly learning to align and
translate](https://arxiv.org/pdf/1409.0473.pdf?utm_source=ColumnsChannel), they
use a BRNN for the encoder and RNN for the decoder with attention.
At each step of the decoder, the RNN receives the previous state, along with a
context that is a linear combination of the outputs of each encoder step.

The weights are all non-negative and sum to 1. To get that, you simply pass the
intermediate weights to a softmax layer.
Each intermediate weight comes from an alignment model, which is (typically) a
single layer neural network that takes the previous state of the decoder and the
output of that step from the encoder. Then tthis alignment model returns a score
for each step of the encoder. All these scores are converted to attention
weights, which are then used to combine the output of the encoder into an input
context for that step of the decoder.

## Video; Speech recognition

Speech recognition systems takes waveform from speech and returns text. This is
typically done with sequence models, at the character level, using the CTC cost
(Connectionist temporal classification). What this does is that it has a "blank"
character, and it allows repetition of characters. Then it collapses all
repeated characters not seperated by blanks, then remove the blanks, to end up
with the sentence.

Note that speech recognition requires very large dataset (~100,000h for best
industrial applications)

## Video: Trigger Word Detection

Can train network to get triggered by certain words. Could pass waveform through
a RNN/LSTM/... and return 0 all the time except when trigger word is pronounced
in which case you return 1.

Might have some issue with an imbalance dataset though.
