---
layout: post
title: Goodhart's law
tags: overfitting statistics
---

I recently discovered what is termed [Goodhart's law](https://en.wikipedia.org/wiki/Goodhart%27s_law). It has different forms, but the most relevant for me goes as follows: "When a measure becomes a target, it ceases to be a good measure." 
The first application that came to mind was overfitting in machine learning. And I am not alone. 
This [blog post](https://datascience741.wordpress.com/2020/10/26/goodharts-law-overfitting-and-ai/) discusses the connection and the potential pitfall of massive grid search for hyperparameter search.àIIn practice, we'll tend to use a test set after hp search to estimate the expected out-of-sample model performance. But I think this is still an interesting observation.
Also, I feel this really applies when we select a model based on its performance on a downstream application, instead of on the first application of the model. For instance, in a forecast + optimization application, if we select the forecasting model not based on its forecasting ability, but on the performance of the entire pipeline. I'm convinced that will lead to severe cases of overfitting.
