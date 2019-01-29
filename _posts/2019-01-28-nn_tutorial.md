---
layout: post
title: Fast AI's Pytorch tutorial
tags: deeplearning pytorch
---

Fast AI wrote a really nice pytorch
[tutorial](https://pytorch.org/tutorials/beginner/nn_tutorial.html)
which starts from a very manual
implementation of a one hidden layer neural network trained on MNIST data, then
gradually adds on pytorch built-in capabilities.
It nicely shows off what pytorch can do, and how it simplifies the coding.
The different steps involve using:
* `torch.nn.functional`: provides already built-in function for most common activation 
functions and loss functions.
* `nn.Module`: provides a class to define a neural network that can be inherited
 when defining your own NN.
* `nn.Linear`: already defines a linear layer (also have convolution
layers,....)
* optim: provides a broad selection of optimizer that can be used to train your
 neural network. Also using those optimizers (in particular, the `step` method)
avoid having to use `torch.no_grad()`.
The parameters of the NN are passed to the optimizer when being instantiated,
which, in addition to telling the optimizer what parameters to optimize, also
provide the optimizer with gradient information.
* Dataset: provides a convenient way to manipulate datasets; allows to combine
 train and test set when slicing.
