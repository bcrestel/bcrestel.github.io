---
layout: post
title: Signing commits in github
tags: github
---

My company asked us to start signing our commits. Let's see how we can do that.

Github put together a
[page](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/managing-commit-signature-verification)
to explain the different steps.

# On my local machine

## Create a GPG key

The first step is to add a GPG key to you github account. You can check if you
already have one by going to Settings > SSH and GPG keys. If the field for GPG
is empty, then you need to create one. To do so, you need
[gnupg](https://blog.ghostinthemachines.com/2015/03/01/how-to-use-gpg-command-line/).
On Mac OSX, you can simply install the command line by typing `brew install
gpg`.

When this is installed, you can create a GPG key by typing `gpg
--full-generate-key`. You'll be prompted with a series of questions, and after
that you get a key. 

## Exporting your key to github

Now you need to export your public key. To do, find the info
of your key, by typing 
```
gpg --list-secret-keys --keyid-format LONG
``` 
On the row
`sec`, you'll see `rsa4096` if you chose 4,096 bits RSA key, and after that is
your key ID. You can next export that key by typing 
```
gpg --armor --export <key_ID> > .gpg/public.key
```
This will save your public key to a file
`.gpg/public.key`. You can share that file with whoever needs it.

In the case of github, you'll copy the content of that file into the box
provided when you want to add a new GPG key.

## Sign your commits

Now that this is done, you add your GPG key to your local git config by doing
`git config --global user.signingkey <key_ID>`. You can then sign your commit by
adding the `-S` argument when doing `git commit`..... Well, that is if we didn't
break anything. Turns out that homebrew upgraded in the process of installing
gpg, and it broke all my symlinks for python3. It actually installed 3.9, which
as unversioned symlinks placed in a different folder. So I had to fix all that,
and re-install our library.

Now that this works, I still had a few things to do before being able to sign my
commits. The first, mandatory step is to
[create](https://github.com/keybase/keybase-issues/issues/2798) the following
environment variable `export GPG_TTY=$(tty)`. Otherwise, you will never get a
prompt for the gpg passphrase and your signed commit will fail.
Once this is done, you can sign your commit with the argument `-S`, then enter
your GPG passphrase. 
You can check that a commit was signed by doing
```
git verify-commit <commit_hash>
```

If you want to automate all that, just enter the following
2 lines:
```
git config gpg.program gpg
git config commit.gpgsign true
```
and you can commit the same way you were doing before (without the `-S`
argument).

## Save passphrase of the GPG key

Now I still had to enter my passphrase when signing commits. Which can quickly
become annoying. So I followed the steps highlighted
[here](https://gist.github.com/bcomnes/647477a3a143774069755d672cb395ca). At a
high level, you need to `brew install pinentry-mac`, then create 2 files,
`~/.gnupg/gpg-agent.conf` in which you add
```
# Connects gpg-agent to the OSX keychain via the brew-installed$
# pinentry program from GPGtools. This is the OSX 'magic sauce',$
# allowing the gpg key's passphrase to be stored in the login$
# keychain, enabling automatic key signing.$
pinentry-program /usr/local/bin/pinentry-mac
```
then `~/.gnupg/gpg.conf` where you add
```
use-agent
```

# On a remote server
Obvioulsy, you don't need to re-create the key. You can simply modify the global
`.gitconfig` file to add `user.name, user.email, user.signingkey`.

Then, you also need to add your **private** key to `gpg` on the remote server.
To do that, you first need to export your private key from your local machine,
```
gpg --armor --export-secret-keys <key_ID> > ~/.gpg/private.key
```
Then on the remote server, you add that private key by doing
```
gpg --import ~/.../private.key
```
You will be prompted for your GPG passphrase, and that's it. You can check that
you added the GPG key successfully doing
```
gpg --list-secret-keys --keyid-format LONG
``` 

After that, you can sign your commits with the `-S` option
``` 
git commit -S
``` 
Note that I didn't have to set up the environment variable `GPG_TTY` (even
though that environment variable was not defined).

You can automate the signing of commits the way you would do locally.

It looks like we could use `pinentry` on a unix server. But I haven't tried yet.



# References

This
[post](https://juliansimioni.com/blog/troubleshooting-gpg-git-commit-signing/)
is pretty good.
