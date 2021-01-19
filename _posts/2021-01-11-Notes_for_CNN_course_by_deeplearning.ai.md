---
layout: post
title: Notes for CNN course by deeplearning.ai (week 1)
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
Padded convoluted image has dim $n+2p-f+1 \times n+2p-f+1$.
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

## Video: Convolutions over volumes

Application: RGB images (3 color channels).\\
Convolve RGB image with a 3d kernel (same number of channels).

Notation: Image 6 x 6 x 3 = (height, width, channels).
Number of channels in image and kernel must be equal.

Really this is 2d convolutions repeated over a stack of 2d images. Not really a 3d
convolution. You could imagine having an image of dim 6 x 6 x 6, and convolve
along the third dim also.

Multiple filter:
You can apply different kernels to the same image(s) and stack the results to
generate also a 3d output. For intance, you could combine the output of a
vertical edge detector and horizontal edge detector.

Dim summary when using `nb_filters_used` filters on an image of `c` channels: image = n x n x c, kernel = f x f x c, then output = n-f+1 x n-f+1 x
nb_filters_used

## Video: One layer of a convolutional layer

Convolutional layer = activation_function (multiple filters--with the right
number of channels-- + a bias), where bias is a single real number.
So output has same dimension as the previous multiple filter example.

And number of parameters is equal to (dim of kernel + 1) x nb_kernels. And this
number of parameters is independent of the dimension of the input!

Notations for layer $l$:
* $f^{[l]}$ = filter size
* $p^{[l]}$ = padding
* $s^{[l]}$ = stride
* input: $n_H^{[l-1]} \times n_w^{[l-1]} \times n_C^{[l-1]}$
* output: $n_H^{[l]} \times n_w^{[l]} \times n_C^{[l]}$, where
$$n_{H/W}^{[l]} = (n_{H/W}^{[l-1]} + 2p^{[l]} - f^{[l]}) / s^{[l]} + 1$$.
* And $n_c^{[l]}$ is equal to the number of filters used in the convolutional
layer. 
* Each filter has dim $f^{[l]} \times f^{[l]} \times n_c^{[l-1]}$ as the
number of channels in the kernel has to be equal to the number of channels in
the input image.
* Weights: $f^{[l]} \times f^{[l]} \times n_c^{[l-1]} \times n_c^{[l]}$
* Bias: $n_c^{[l]}$

Note: ordering Batch, Height, Width, Channel is not universal as some people
will put channel after batch.

## Video: A simple convolutional network example

Basic idea is to stack convolutional layers one after the other. At the end, you
can flatten the last image and pass it to an appropriate loss function.

One general trend is that the image dimension is going down as we progress in
the net, while the number of channels go up.

Basic convolution network includes: convolutional layers, pooling layers, and
fully connected layers.

## Video: Pooling Layers

Pooling layers are often found in convolutional networks. The intuition behind
these layers is not well understood, but they are commonly used as they seem to
improve performance.

The idea is to apply a filter (or kernel), the same way we did it for
convolution layers. That is a pooling layers has a size $f$ and a stride $s$.
But instead of applying a convolution kernel for every step of the filter, we
instead apply a single function. In practice, we find max pooling (most common)
and average pooling (not as common). 
For max pooling for instance, at every step of the filter, we take the max
within that filter.
We sometimes find average pooling at the end of a network, to compress an image
into a single pixel.
Interestingly, pooling layers have no parameter to learn (only hyperparameters).

When the input image has multiple channels, we apply the pooling filter to each
layer.
Most commonly, we don't apply padding with pooling layers.

## Video: CNN example

Introduce an example of CNN to do digit recognition on a 32 x 32 x 3 RGB image.
The presented CNN is inspired by LeNet-5.

* convolutional layer 1: 6 filters with hyperparameters $f=5, s=1, p=0$
* max pooling layer 1: $f=2, s=2$.
* convolutional layer 2: 16 filters with hyperparameters $f=5, s=1, p=0$
* max pooling layer 2: $f=2, s=2$.
* fully-connected layer 3: flatten output of max pooling layer 2 -> fc3 = 400 x
 120
* fc4: 120 x 84
* Softmax layer (I guess fc5 + softmax): 84 x 10 (10 digits to recognize)

We notice that throughout the layers, the image decreases while the number of
channels increase.
Also, we notice the alternance conv layer / pool layer a few times, followed by
a few fully-connected layers.

## Video: Why convolutions?

What makes convolution layers efficient for image recognition?
* weight sharing: you work on the input image with limited number of parameters
* sparsity of connections: each output pixel only depends on a few of the input
 pixels
* Conv layers are believed to be good at preserving translation invariance.
