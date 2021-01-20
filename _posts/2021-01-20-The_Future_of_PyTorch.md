---
layout: post
title: The Future of PyTorch
tags: deeplearning pytorch
---

PyTorch
[announced](https://ai.facebook.com/blog/reengineering-facebook-ais-deep-learning-platforms-for-interoperability/)
that it will make some changes to its library, fully integrating
[Lightning](https://www.pytorchlightning.ai/) and [Hydra](https://hydra.cc/).

PyTorch Lightning is a framework used for all engineering matters of a Deep
Learning model, for instance it can be used to simplify the training loops. It
recently
[released](https://medium.com/pytorch/pytorch-lightning-1-0-from-0-600k-80fc65e2fab0)
its version 1.0 with a stable API. Lightning will also allow easy quantization,
checkpointing, and others.

For Hydra, I'm less sure what it's about, but it is
[described](https://medium.com/pytorch/hydra-a-fresh-look-at-configuration-for-machine-learning-projects-50583186b710)
as a way to handle all the config files.
