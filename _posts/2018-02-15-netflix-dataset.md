---
layout: post
title: Playing with the Netflix dataset
tags: pandas netflix ML
---

I downloaded the Netflix dataset from
[Kaggle](https://www.kaggle.com/netflix-inc/netflix-prize-data). The Netflix
dataset is a list of movie ratings entered by different customers. It was
provided by Netflix for the [Netflix
Prize](https://en.wikipedia.org/wiki/Netflix_Prize) competition.
The goal of the competition was to predict missing movie ratings.

So far, I have been
[playing](https://github.com/bcrestel/ML/datasets/netflix/read_netflix.py) with
the data to format them in an interesting way. My approach is
1. create column for movieID by copying custID and removing all entries not
finishing by ':', then extend movieID 'ffill'.
2. create sparse matrix with movie ratings for each customer
3. create SparseDataFrame from sparse matrix

An interesting question is how do you reconcile ratings from different
customers. One approach is to normalize the ratings for each customer, by
substracting the mean rating and dividing by the standard deviation of the
ratings for that customer.
Also, as I don't want to have to deal with pathological cases, I am going to
remove all customers with a single rating.

Unfortunately, the SparseDateFrame object appears to be extremely slow for any
sort of operation (subtract, mean,...). I ended making all operations prior to
the transformation to sparse dataframe.
