---
layout: post
title: Install pdflatex on MacOS
tags: latex mac
---

# Tex distributions
First step is to install a latex distribution, either `basictex` or `mactex`.
If you want to be thrifty, go for `basictex`. But be prepared to install a lot of missing style files.
Both ways can done via `brew`,
```
brew install --cask basictex
```

# Installing missing style files
All of this is done via `tlmgr`. You can first update it,
```
sudo tlmgr update --self
```
Then, if you're missing `comment.sty` when trying to compile a latex document, you'll need to do
```
sudo tlmgr install comment
```
Notice that you always run `tlmgr` in `sudo` mode.

A last comment: I went with `basictex`. But if I had to do it again, I would install the full distribution so that I don't have to install so many missing style files.

Ref: [Getting started and productive with latex basictex on OSX terminal](https://bilalakil.me/getting-started-and-productive-with-latex-basictex-on-os-x-terminal)
