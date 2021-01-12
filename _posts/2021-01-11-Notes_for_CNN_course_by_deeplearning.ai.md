---
layout: post
title: Notes for CNN course by deeplearning.ai
tags: cnn course deeplearning
---

I decided to take the course [Convolutional Neural
Networks](https://www.coursera.org/learn/convolutional-neural-networks) by
[deeplearning.ai](https://www.deeplearning.ai/) and hosted by Coursera. And I'm
going to take some notes in this document

# Week 1: Foundations of Convolutional Neural Networks

Objectives:
* Explain the convolution operation
* Apply two different types of pooling operations
* Identify the components used in a convolutional neural network (padding, stride, filter, ...) and their purpose
* Build and train a ConvNet in TensorFlow for a classification problem

## Video: Computer Vision

Example of vision problems:
* Image classification: decide what picture represents (given set number of categories)
* object detection: draw boxes around specific objects in a picture
* neural style transfer: content image + style image -> content image with the
 style of the style image

Challenges:
Input can be really big: 64x64x3 images -> 12288 pixels; very small. Large
images can get really big very quickly. 1000x1000x3 = 3M pixels. With a first
layer of 1,000 nodes, you end up with 30M weights just for the first layer. With
so many parameters, hard not to overfit; plus need lots of memory.

To still be able to use large images, you need to use CNN.

## Video: Edge Detection Example

CNN based off the [convolution
operation](https://en.wikipedia.org/wiki/Convolution). Illustrated by the edge detection
example.
Another interest ref for convolution is [Colah's
blog](https://colah.github.io/posts/2014-07-Understanding-Convolutions/).

How do you detect edges in an image?
Show an example of a 6x6 matrix convolved with a 3x3 kernel (or filter), giving
a 4x4 image.
You just slide the kernel over the image and at each step multiply the entries
pointwise then sum them all.
Similar to what you would do with the actual operator, $$ f \star g = \int_{-\infty}^{\infty} f(\tau)g(t-\tau) d\tau $$, where for each
$t$ the function $g$ (the kernal, or filter) is shifted by an amount $t$.

Don't need to re-implement a convolution operator: python -> conv_forward,
tensorflow -> tf.nn.conv2d, keras -> cond2D

Why is this doing edge detection?
Look at picture with 2 colors separated by a vertical edge. 
Apply 3x3 kernel: 1,0,-1 (in x direction; same in y).
Obtain a thick edge, in your 4x4 image, in the middle.
