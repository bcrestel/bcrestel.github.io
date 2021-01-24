---
layout: post
title: Notes for CNN course by deeplearning.ai (week 2)
tags: cnn course deeplearning
---

These are my notes for [week
2](https://www.coursera.org/learn/convolutional-neural-networks/home/week/2),
focusing on case studies.

## Video: Why look at case studies?

Look at classic CNN is a good way to gain intuition about how CNNs work. Also,
in computer vision, successful architecture for one task is often good for
another task.

Classic CNN examples looked at this week:
* LeNet-5
* AlexNet
* VGG
* ResNet
* Inception

## Video: Classic Networks

### [LeNet-5 (1998)](http://www.iro.umontreal.ca/~lisa/bib/pub_subject/finance/pointeurs/lecun-98.pdf)
Introduced to recognize black&white hand-written digits (32x32x1). The
[architecture](https://miro.medium.com/max/4308/1*1TI1aGBZ4dybR6__DI9dzA.png) is
described below. Note that 
at the time of the paper, padding was not common. So all convolutional layers
shrink the size of the image.
* Convolutional layer: 5x5, stride=1, 6 channels -> output: 28x28xg
* average pooling (today would probably use max pooling): 2x2, stride=2 ->
 output: 14x14x6.
* Convolutional layer: 5x5, stride=1, 16 channels -> output: 10x10x16
* average pooling : 2x2, stride=2 -> output: 5x5x16.
* fully connected layers: 400x120, 120x84, 84x10.
* output layer today would probably be a softmax. In the paper, they used
 something else that is not common today.
All non-linearities were tanh or sigmoid. Also, they applied activation
functions after the pooling layers.
Total network had about 60,000 parameters, which is small by today's standard
(>1M parameters).
However variation in image size through the network remains current: height and
width go down, number of channels go up.
Another aspect that remains often true today is the alternance of the layers:
conv, pool, conv, pool, fc, output.
A last note, they had a different way of apply the kernels to the input image
(i.e, didn't have kernels with the same number of channels as the input).

### [AlexNet (2012)](https://courses.grainger.illinois.edu/ece544na/fa2013/krizhevsky2012.pdf)

The
[architecture](https://neurohive.io/wp-content/uploads/2018/10/AlexNet-1.png) is
described below. The input image is 227x227x3.
* conv layer, 11x11, stride=4, 96 channels -> 55x55x96
* max pooling, 3x3, stride=2 -> 27x27x96
* conv layer, 5x5, same padding, 256 channels -> 27x27x256
* max pooling, 3x3, stride=2 -> 13x13x256
* conv layer, 3x3, same padding, 384 channels ->13x13x384 
* conv layer, 3x3, same padding, 384 channels ->13x13x384 
* conv layer, 3x3, same padding, 256 channels ->13x13x256
* max pooling, 3x3, stride=2 -> 6x6x256
* conv layer, 3x3, same padding, 384 channels ->13x13x384 
* conv layer, 3x3, same padding, 384 channels ->13x13x384 
* conv layer, 3x3, same padding, 256 channels ->13x13x256
* Fully-connected layers: 9216 -> 4096 -> 4096 -> 1,000 (Softmax)
Many similarities with LeNet-5, but AlexNet has about 60M parameters.
Also, they used ReLU activation functions.
They also used another type of layer called Local Response Normalization, which
normalizes each pixel/position across all channels. This type of layer is not
really used anymore as it was found that it had a very small impact on the
results.

### [VGG-16 (2015)](https://arxiv.org/pdf/1409.1556.pdf%20http://arxiv.org/abs/1409.1556.pdf)

The architecture can be visualized
[here](https://miro.medium.com/max/850/1*_Lg1i7wv1pLpzp2F4MLrvw.png).
VGG-16 really simplified the neural networks architecture. It only relies on a
single type of convolutional layer (3x3, stride=1, same padding) and a single
type of max pooling (2x2, stride=2).
The input is 224x224x3.
* conv: 64 channels
* conv: 64 channels -> 224x224x64
* max pooling -> 112x112x64
* conv: 128 channels
* conv: 128 channels -> 112x112x128
* max pooling -> 56x56x128
* conv: 256 channels
* conv: 256 channels
* conv: 256 channels -> 56x56x256
* max pooling -> 28x28x256 
* conv: 512 channels
* conv: 512 channels
* conv: 512 channels -> 28x28x512
* max pooling -> 14x14x512
* conv: 512 channels
* conv: 512 channels
* conv: 512 channels -> 14x14x512
* max pooling -> 7x7x512
* fc: 4096 -> 4096 -> 10,000 (softmax)
VGG-16 has about 138M parameters, which is large even by today's standards.
16 is the number of layers. There is also a VGG-19, but performance is
comparable.
VGG is attractive to the community b/c it simplifies the construction of the
network by systematizing the change in height/width and channels from one layer
to the next.

## Video: [ResNets (2016)](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf)

ResNets was introduced to help training of very deep neural networks.
In practice, we notice that training error for plain network will start to
increase after a certain depth is reached.
ResNets allows to train networks of 100 or 1,000 layers deep and still see the
training error gradually decrease as the depth of the network increases. ResNets
helps with the problems of vanishing and exploding gradients.

Elementary block of a ResNet is a Residual Block, which adds a skip connection
(or shortcut) to typical fully-connected layers. In a given layer, after the
linear part but before the application of the ReLU activation function, the
value of layer output a few levels below is added, eg, 
$a^{[l+2]} = g(z^{[l+1]} + a^{[l]})$.

