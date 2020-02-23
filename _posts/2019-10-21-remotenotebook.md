---
layout: post
title: Running a jupyter notebook on a remote server
tags: python jupyter remote
---

Super simple, but because I have the memory of a squirrel I need to mark it
down. So when you have session running on a remote server, you can start a
jupyter notebook on that server. The catch is that you need to specify the ip of
that remote server, otherwise you won't connect to the server but locally. If
you are in bash session on that server, you can do
```
jupyter notebook --ip=$(hostname -I)
```
If you want to start the notebook directly, without connecting to bash first,
you can do something like
```
<server exec sessionid> -- bash -c 'jupyter notebook --ip=$(hostname -I)'
```
