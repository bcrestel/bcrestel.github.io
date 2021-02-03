---
layout: post
title: How to rename a commit
tags: git
---

In all cases, I'm assuming the targeted commit hasn't been pushed. If that's the
case, then it's a different story (and probably a bad idea to do it).

## If it's the latest commit

You can simply amend the latest commit by doing
```
git commit --amend
```
then change the commit name and save

## If it's not the latest commit

In that case, you will need to rebase.
Assume you want to change the Nth commit from the top (the latest is the first).
Then interactively rebase the last N commits,
```
git rebase -i HEAD~N
```
This will prompt a window that shows the last N commits. From there, you can do
a few things (and a lot of damage, so careful!). But in our case, you just want
to change `pick` to `reword` in front of the commits that you want to modify.
Then save. It will then open each commit windows for the commits you selected in
the previous step. For each commit, modify the name the way you want it, then
save.
