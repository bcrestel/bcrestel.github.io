---
layout: post
title: Jupyter Extensions
tags: notebook python
---

Jupyter Notebook offer really neat extensions that can honestly transform your
experience working with notebooks.

# How to install
First step is to install. There are different ways (`conda`, `pip`,
`poetry`,...). You can check out the documentation
[here](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html).
When you install `jupyter_contrib_nbextensions`, it will automatically install
`jupyter_nbextensions_configurator` (see
[here](https://github.com/Jupyter-contrib/jupyter_nbextensions_configurator)),
which provides a nice GUI to enable/disable the extensions.

The whole process is pretty easy, but there are 2 actions that you need to take
before having the luxury of enjoying all the goodies:
1. Activate the configurator
```
jupyter nbextensions_configurator enable --user
```
then
2. Activate the extensions
```
jupyter contrib nbextension install --user
```
I'm honestly not sure of the order. I did in that order, but maybe it doesn't
matter.

# What extensions?
A few useful extensions:
* table of content
* collapsible headings
* move selected cells
