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

Actually, this mathematical definition is a little bit different as the kernel
is mirrored around its axes (we have $g(t-\tau)$ as a function of $\tau$). This
is discussed in the section on [Video: Strided Convolutions](## Video: Strided Convolutions).

Don't need to re-implement a convolution operator: python -> conv_forward,
tensorflow -> tf.nn.conv2d, keras -> cond2D

Why is this doing edge detection?
Look at picture with 2 colors separated by a vertical edge. 
Apply 3x3 kernel: 1,0,-1 (in x direction; same in y).
Obtain a thick edge, in your 4x4 image, in the middle.

## Video: More Edge Detection

Introduces more examples for filters, for instance for horizontal edge
detection. But also different types of vertical edge detectors:
eg, 1,0,-1//2,0,-2//1,0,-1 (Sobel filter)
or 3,0,-3//10,0,-10//3,0,-3/ (Scharr filter).
But you can parametrize the values of your kernel, and learn the ideal kernel
for your problem. And that is a key idea of modern computer vision.

## Video: Padding

Discrete convolution presented shrink the image, so you could only apply it a
few times. Initial image n x n, kernel f x f, then convolved image $n-f+1 \times
n-f+1$.

Also, pixels close to the edge of an image are used much less in the convolution
compared to central pixels.

Solution for both problems: pad the image before applying convolution operator,
i.e., add pixels on the outside of the image: eg, 6x6 ->(padding) 8x8
->(convolution w/ 3x3 kernel) 6x6. 
Padded convoluted image has dim $n+2p-f+1 \times n+2p-f+1$
By convention, you pad with 0's.

How much to pad? Valid convolution vs Same convolution
* Valid convolution = no padding
* Same convolution: pad so as to offset the shrinking effect of the convolution
(final image has same dim as input image) -> $2p = f-1$

Note that by convention, in computer vision, f is typically an odd number: 1
(less common), 3,
5, 7. That
has the advantage that you can have a symmetric padding.

## Video: Strided Convolutions

Stride = by how many pixels you shift the kernel (vertically and horizontally).
So the convolved image will be smaller with stride 2 than with stride 1.
Resulting image side length: $(n+2p-f)/s+1$ (potentially rounded if needed)

[Cross-correlation](https://en.wikipedia.org/wiki/Cross-correlation) vs
convolution:\\
As discussed earlier, the actual convolution operator would require to flip the
kernel around its axes, since we do $$\int_{-\infty}^{\infty} f(\tau) g(t-\tau)
d\tau $$. But in deep learning, people don't flip it. So in that sense, this is
closer to the cross-correlation operator whic is defined, for real functions, as
$$\int_{-\infty}^{\infty} f(\tau) g(t+\tau) d\tau$$. 
But as explained in the video, the convention is such that people in deep
learning still call that a convolution operator.


