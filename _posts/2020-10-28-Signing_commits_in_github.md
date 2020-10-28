---
layout: post
title: Signing commits in github
tags: github
---

My company asked us to start signing our commits. Let's see how we can do that.

Github put together a
[page](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/managing-commit-signature-verification)
to explain the different steps.

The first step is to add a GPG key to you github account. You can check if you
already have one by going to Settings > SSH and GPG keys. If the field for GPG
is empty, then you need to create one. To do so, you need
[gnupg](https://blog.ghostinthemachines.com/2015/03/01/how-to-use-gpg-command-line/).
On Mac OSX, you can simply install the command line by typing `brew install
gpg`.

When this is installed, you can create a GPG key by typing `gpg
--full-generate-key`. You'll be prompted with a series of questions, and after
that you get a key. Now you need to export your public key. To do, find the info
of your key, by typing `gpg --list-secret-keys --keyid-format LONG`; on the row
`sec`, you'll see `rsa4096` if you chose 4,096 bits RSA key, and after that is
your key ID. You can next export that key by typing `gpg --armor --export
<key_ID> > .gpg/public.key`; this will save your public key to a file
`.gpg/public.key`. You can share that file with whoever needs it.

In the case of github, you'll copy the content of that file into the box
provided when you want to add a new GPG key.

Now that this is done, you add your GPG key to your local git config by doing
`git config --global user.signingkey <key_ID>`. You can then sign your commit by
adding the `-S` argument when doing `git commit`..... Well, that is if we didn't
break anything. Turns out that homebrew upgraded in the process of installing
gpg, and it broke all my symlinks for python3. It actually installed 3.9, which
as unversioned symlinks placed in a different folder. So I had to fix all that,
and re-install our library.


