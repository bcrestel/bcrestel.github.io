---
layout: post
title: Fixing jekyll
tags: jekyll ruby mac
---

After upgrading to Catalina, I could not run `jekyll` locally to render that
website on my laptop. I was getting a weird error message about the ruby
interpreter being bad.

The solution is to use a different ruby interpreter, installed via Homebrew:
`brew install ruby`. Then update all your paths so that the command line will
default to this newly installed interpreter:
```
export PATH="/Users/bencrestel/local/homebrew/opt/ruby/bin:$PATH"
```
Once this is done, we can install the jekyll gem (and bundler, but I'm not sure
what that is): `gem install --user-install bundler jekyll`. Next, you add that
to your PATH
```
export PATH="/Users/bencrestel/.gem/ruby/2.7.0/bin":$PATH
```
so that the right version of `jekyll` will be used. And you're good to go.

Ref: All the info was in that
[post](https://github.com/MichaelCurrin/learn-to-code/blob/master/en/topics/scripting_languages/Ruby/README.md#install-and-upgrade).
