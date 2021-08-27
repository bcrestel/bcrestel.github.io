---
layout: post
title: ssh access via ssh key
tags: ssh
---

When accessing a remote server, you typically have to enter your password every time you connect (ssh, sshfs,...). If you access that server via the ssh protocol, you can instead identify via a ssh key.

It's actually pretty easy to do. All you have to do is add you public ssh key to the file `~/.ssh/authorized_keys` on the server side. On your laptop, you need to have your ssh key added to your keychain. Then every time you ssh to the server, the remote server will send you a challenge that can only be resolved by your private ssh key.

That [article](https://www.linode.com/docs/guides/use-public-key-authentication-with-ssh/) contains a lot of information about that topic.
