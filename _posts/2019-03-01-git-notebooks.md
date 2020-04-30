---
layout: post
title: Tracking notebooks with git
tags: git notebook python
---

The main challent of tracking notebooks with git is that every time you
re-generate an output, git will keep track of that. It makes each commit large,
and hard to keep track of.
Fortunately, there is a script that removes the output prior to your commit. I'm
using [nbstripout](https://pypi.org/project/nbstripout/). You can turn it on by
doing, inside your git repo,
```
nbstripout --install
```
and turn it off by doing
```
nbstripout --install
```
It works great. Unfortunately, it doesn't behave super well when switching to
other branches where nbstripout was not applied; basically, it removes the
output from every notebook it fines, and then requires you to `git commit`
before you can switch out of that branch. Not great. So instead, I apply it
manually to the notebook that I want to commit. You can do so by typing
```
nbstripout FILE.ipynb
```

