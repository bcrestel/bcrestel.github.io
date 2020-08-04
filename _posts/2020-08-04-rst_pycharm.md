---
layout: post
title: rst in pycharm
tags: pycharm doc rst
---

In order to render rst files in pycharm, you need to set up some environment
variables, otherwise you'll get the error `NameError: Cannot find docutils in selected interpreter.`
In short, you need to add
```
export LC_ALL=en_US.UTF-8  
export LANG=en_US.UTF-8
```
to your `.bash_profile`. You can then restart pycharm and it should work.

Ref: [Stackoverflow](https://stackoverflow.com/questions/55522176/pycharm-and-rst-nameerror-cannot-find-docutils-in-selected-interpreter)
