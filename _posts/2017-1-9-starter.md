---
layout: post
title: Getting started
tag: jekyll
---

For this blog, I am using the [poole/hyde](https://github.com/poole/hyde)
example. Unfortunately, this repo does not seem to be maintained anymore, and
the list of pull requests has grown steadily since 2015. The main modifications I
had to make to run this blog are:
* in `_config.yml`:
    - change the markdown to `kramdown`
    - remove `relative_permalinks: true`
    - add the gems `jekyll-paginate, jekyll-seo-tag, jekyll-sitemap, jekyll-gist`
* in the `_includes/head.html`
    - replace the ` { { site.baseurl }} ` with a simple slash

I also added Mathjax. I found online different approaches to do that. What seems
to work was to add the Mathjax script in the header of the html pages. Building
on the original organization, this meant adding the script to the file
`_includes/head.html`. Following this discussion on
[github](https://github.com/github/pages-gem/issues/307), I added the following
lines,  
```html  
<!-- Mathjax -->
<script type="text/x-mathjax-config"> MathJax.Hub.Config({ TeX: { equationNumbers: { autoNumber: "all" } } }); </script>
<script type="text/x-mathjax-config">
 MathJax.Hub.Config({
   tex2jax: {
     inlineMath: [ ['$','$'], ["\\(","\\)"] ],
     displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
     processEscapes: true
   }
 });
</script>
<script
src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
```
Let's check that it works inline $x^2 + y^2 = z^2$. It also works in displayMath
mode,
\\[ \mathbb{P}(A|B) = \frac{\mathbb{P}(B|A) \mathbb{P}(A)}{\mathbb{P}(B)} \\]

