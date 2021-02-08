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
* Object Localization: Box around all objects in the picture (typically multiple
 objects per picture)

Classification with localization:
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

## Video: Bounding Box Predictions

Sliding windows return bounding boxes that are not very accurate, as box could
not be exactly rectangular and/or sliding windows may not overlap exact location
of best box.

Solution: [YOLO (You Only Look Once)
algorithm](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Redmon_You_Only_Look_CVPR_2016_paper.pdf).
The idea is actually very close to the one introduced for the classification
with localization problem. Except that here you split your image into a grid.
Then in each grid, you return the 8-dimensional vector described earlier: pc,
bx, by, bh, bw, c1, c2, c3. So you run your image through a ConvNet only once
and output a tensor of dimension $N \times N \times 8$, where $N$ is the
dimension of your output grid. For each grid, you try to match the target 8-d
vector. That way, the boxes can be defined much more precisely (no fixed boxes;
instead the network infers the center and dimensions of the box).
Also, because we only use the input image once, the YOLO algorithm is quite fast
and can be used for real-time image detection.

The box is encoded relatively to each individual sub-grid. The position must be
between 0 and 1 (sometimes passed through a sigmoid), but height and width can
be greater than 1 (sometimes passed through an exponential to force
non-negativity).

## Video: Intersection Over Union

How can you evaluate object localization algorithm? You can use Intersection
Over Union, which is a measure of overlap between 2 boxes. It takes the ratio of
the area of their intersection over the area of their union. That ratio is
between 0 (both boxes don't intersect at all) and 1 (both boxes are equal).
Often, it is considered that a IoU greater than 0.5 means the box is correct.

## Video: Non-max Suppression

Even though each target box only belongs to a single cell in the grid, when
predicting, the network is likely to return multiple boxes corresponding to the
same object. A simple solution is to use the non-max suppression algo. While
there are boxes, pick the one with the highest pc score (in case there is only a
single category detected) and discard all other boxes that have a high IoU score
with that box (eg, greater than 0.5). Then move on to the box with next highest
score, etc...

## Video: Anchor Boxes

What can you do if multiple boxes have their center inside the same grid cell?
Even though it doesn't happen too often (especially with a fine enough grid),
it's good to have a plan for that. 

The solution propoosed is simply to repeat the output vector for a single object
by the number of objects you want to be able to detect. So for instance, to
allow detection of 2 objects per grid cell, the output will be: pc,
h_x,...,c_1,c_2,c_3, pc, h_x,...,c_3. How do you decide which object is object 1
and object 2?

You can do that using anchor boxes. You set 2 anchor boxes, for instance 2
rectangular boxes, one vertical and one horizontal. In each grid cell, if an
object has a shape more vertical it is object 1 and if it is more horizontal it
is object 2 (can use IoU to categorize each object)). Then you classify each target object according to that rule, and
you train your object detection network. It will allow the network to specialize
its output to each type of box.

## Video: YOLO Algorithm

The YOLO algorithm puts together all the different components we saw in that
week to do fast object detection.

Set your target vectors using the box parametrization we introduced before (pc,
hx,...,c1,...) and the idea of anchor boxes. Then you can train your network
using that dataset.
After running prediction, you post-process the results using a non-max
suppression algorithm. And you're done.

## Region Proposals

Alternative idea to first propose a small number of regions where an object
could be, then classify each proposed region. The proposed regions come from a
segmentation type algorithm. Different approaches exist, with fastest approach
being formulated as a convnet.
