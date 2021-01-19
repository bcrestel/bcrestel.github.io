---
layout: post
title: Google AutoML for forecasting
tags: timeseries forecasting automl
---

GoogleAI wrote a [blog
post](https://ai.googleblog.com/2020/12/using-automl-for-time-series-forecasting.html)
about its new autoML solution for time series forecasting. They tested their
framework on a few different Kaggle competitions, including M5, and obtained
very good results (top 10%) without any manual intervention.

I actually find that as a proof of quality (as in, not overfitting) that they
get very good results, but not the best results.
There is still a bit of hand-crafted features like the way they deal with
sparsity, very common in retail time series; they add a separate predictor for
whether the next prediciton will be 0 or not (in addition to predicting the
value).
Overall, it's hard to judge as they don't provide much information besides the
standard
[skecth](https://1.bp.blogspot.com/-5VIKGwKurE4/X8p0t96KlzI/AAAAAAAAG3w/R_mfc8UOYG8tSbn0RjvdNhS8z9RPYxxZwCLcBGAsYHQ/s1999/image2.png)
of an autoML pipeline: feature engineering, architecture search, hyperparameter
search, ensembling of best models. It is likely that for the architecture search
part, they re-used results from Google previous
[work](https://ai.googleblog.com/2017/05/using-machine-learning-to-explore.html)
on the matter (evolutionary algorithms and RL).

I don't really like their exclusive reliance on RNN layers, but this is still
considered standard by many. And it'd be interesting to see how this behaves in
"real" real-life scenarios, not in competitions.
Overall, I still feel there is a lot of manual work that is required for
ML-based time series forecasting. Whether you hide that in a pipeline and call
that autoML or not is a different topic.
