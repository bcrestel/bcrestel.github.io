---
layout: post
title: Upgrade jekyll and Ruby
tags: jekyll ruby mac
published: true
---

When switching to a new mac, my version of Ruby got bumped up to 3.0 and jekyll to 4.2.0. A few things changed along the way and broke this website.
So here is what I had to do to fix it:
* In the `_config.yml` file, replace `gems` with `plugins`. See [here](https://jekyllrb.com/docs/plugins/installation/)
* To install packages, you don't need to do `gem install <package>`. You can instead add it to a `Gemfile` which looks like something like this:

```
source "https://rubygems.org"

gem "webrick", "~> 1.7"

gem "kramdown-parser-gfm", "~> 1.1"

gem "jekyll-watch", "~> 2.2"

gem "jekyll-paginate"
gem "jekyll-seo-tag"
gem "jekyll-sitemap"
gem "jekyll-gist"
```
You then run `bundle install` (you obviously need to install `bundle` before).
* I had some version conflicts in my dependencies. This was resolved by resorting to `bundle` again. Instead of doing `jekyll serve`, you can do: 

```
bundle exec jekyll serve
```
