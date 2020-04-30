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
* `optim`: provides a broad selection of optimizer that can be used to train your
 neural network. You still need to compute the gradient yourself, and zero out
the gradient after the update step.
The parameters of the NN are passed to the optimizer when being instantiated,
which, in addition to telling the optimizer what parameters to optimize, also
provide the optimizer with gradient information.
* `Dataset`: provides a convenient way to manipulate datasets; allows to slice
train and test sets together.
* `DataLoader`: manages mini-batches automatically; you just give it a Dataset and
a batch size.
* `conv2d`: pytorch has a lot of layers already built-in that can be directly 
used when building an object of type `nn.Module`. 
* `nn.Sequential`:  it is another way of defining a model, instead of `nn.Module`. 
