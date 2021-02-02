---
layout: post
title: Notes for CNN course by deeplearning.ai (week 3)
tags: cnn course deeplearning
---

## Video: Object Localization

Distinguish:
* Classification: just tell what is on the picture (typically a single object
 per picture)
* Classification with localization: tell what it is + say where it is (box
 around object). Typically 1 object/picture
* Object Localization: Box around all objects in the picture.

Classification with locatliation:
in addition to softmax output layer, add another layer for box info: bx, by, bh,
bw = coordinates of center of the box (bx, by) and height/width of the box (bh,
bw).

Look at problem where object can be: pedestrian, car, motorcycle, or background
(no object). Proposes parametrization:
* pc = 1 if object (1,2,3) or 0 if no object (4)?
* bx, by, bh, bw
* c1, c2, c3: 1/0 if an object is there

What is the loss in that case? Loss will differ whether you have an object or
not. When no object (ie, pc=0), then loss = $\text{dist}(y_1, \hat{y}_h)$. If
there is an object (pc=1), then loss = $\sum_i \text{dist}(y_i,\hat{y}_i)$. For
the distance, we can use different distance depending on the outputs. For
instance, a log like feature loss (? log loss) for c1, c2, c3, a squared error
for the box, and logistic regression loss for pc.

I honestly don't like that parametrization. I would rather combine pc and c1,
c2, c3 and train that with a [cross entropy
loss](https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html)
(or softmax + log-likelihood) and use a squared error loss (or whatever) for the
box. In the case there is not object, just set the target box to be the entire
picture (centered at the center).


## Video: Landmark Detection

Instead of outputing the parameters of a box, you can simply output coordinates
of important parts of an image (called landmark).
Useful in AR, or snapchat features.

Can modify the output layer to return coordinates of as many landmarks as you
want. Problem is you need a training dataset. So someone has to annotate
pictures with all these landmarks on it.
Also, important for the labels to be consistent across all images (eg, label 1
always for left eye).

## Video: Object detection

Object detection means we want to place boxes around potentially multiple
objects on an image.

Introduces Sliding Windows Detection algorithm. If we try to detect cars on an
image:
1. Train a ConvNet to detect car from tightly cropped pictures
2. Then given an object where you want to detect objects, slide a window across
the entire image, and each time you slide it, run the small window through your
car detector (step 1)
3. Repeat procedure with larger and larger windows.

If there is a (or multiple) car(s) on the picture, at some point, one of the
windows should have isolated that car and the detector should have detected it.

Disadvantage of sliding windows detection: computational cost! Uses many, many
windows. Could use coarser strides (when shifting windows), but that will reduce
efficiency of the localization algorithm.

That technique worked when we had cheap detector. With ConvNet, this doesn't
work anymore. But there is a solution (next video)

## Video: Convolutional Implementation of Sliding Windows

Reference: [OverFeat, by Sermanet et al.,
2014](https://arxiv.org/abs/1312.6229).

When running the sliding window algorithm through a ConvNet, there is a lot of
repeated calculations. You can leverage this by running the entire image through
your ConvNet (instead of the cropped window). The result will be a larger output
and each additional values correspond to running additional cropped windows
through the network.
With that convolutional approach, the stride of the sliding window is given by
the size of the max pooling layer.
