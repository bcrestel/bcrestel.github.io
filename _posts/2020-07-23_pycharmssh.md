---
layout: post
title: Pycharm with ssh interpreter
tags: pycharm
---

If you have a Docker image running on a remote server, you can set up PyCharm to
use the python interpreter in that image locally.
To do so, you go to `Preferences > Project > Project Interpreter`. You then
select the `SSH Interpreter` option. Then you need to set up your connection,
indicate the right port.
There is more on this in this
[article](https://www.jetbrains.com/help/pycharm/configuring-remote-interpreters-via-ssh.html).

Anyway, once this all done properly, I was still having some issue with running
`pytest` with this ssh interpreter. `pytest` would point to my local path. I had
to define a path mapping between my local path and my remote path. To do so, you
go to `Preferences > Project > Project Interpreter`. Below the project
interpreter, you see `Path mappings`, and you can define one from your local to
your remote. After that, `pytest` should be able to find your test.
