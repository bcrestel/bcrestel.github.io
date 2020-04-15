---
layout: post
title: Running a jupyter notebook on a remote server
tags: python remote notebook
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

When running inside a Docker image, you need to take a few more steps. First,
you need to publish the `8888` port of your machine, i.e.,
```
docker run -it -p 8888:8888 -v <...> image:version /bin/bash
```
Then inside your container
```
jupyter notebook --ip=$(hostname -I) --allow-root
```
Then on my laptop, the second url was the one that worked
(`http://127.0.0.1:888/?token=...`).
