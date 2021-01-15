---
layout: post
title: Michelangelo Uber ML platform
tags: ML
---

Uber has a blog
[post](https://eng.uber.com/michelangelo-machine-learning-platform/) detailing
their ML platform which I found interesting.  
I'm using this post to save highlights and comments.

Their article is from 2017. They
started building Michelangelo around mid-2015.
_It is designed to cover the end-to-end ML workflow: manage data, train,
evaluate, and deploy models, make predictions, and monitor predictions. The
system also supports traditional ML models, time series forecasting, and deep
learning._: That looks like a pretty comprehensive system, at least on the
paper.

They mention that prior to Michelangelo, all ML was ad-hoc, done on a desktop
(!), and with different production solutions for each team. So basically, it was
a patchwork, a very heterogeneous picture. They were starting to see technical
debt in their ML projects. So the plan: _Michelangelo is designed to address
these gaps by standardizing the workflows and tools across teams though an
end-to-end system that enables users across the company to easily build and
operate machine learning systems at scale._

They mention different open-source softwars that they used to build
Michelangelo:
* HDFS: Hadoop Distributed File System
* Spark: Compute engine for Apache Hadoop
* Samza: Samza is Linkedin's framework for continusou data processing
* Cassandra: it is a free and open-source, distributed, wide column store, NoSQL
 database management system designed to handle large amounts of data across
 many commodity servers, providing high availability with no single point of
 failure.
* MLLIB: Apache's scalable ML library; fits into Spark and interoperates with
 Numpy and R.
* XGBoost: they mention that they use gradient boosted decision trees to solve
 the meal time delivery problem at UberEats.
* TensorFlow
* (Apache) Kafka: open-source stream processing platform; to handle real-time
 data feeds.

I understand that they do not describe their datalake in this post, but mentions
its existence (duh): _Michelangelo is built on top of Uber’s data and compute
infrastructure, providing a data lake that stores all of Uber’s transactional
and logged data, Kafka brokers that aggregate logged messages from all Uber’s
services, a Samza streaming compute engine, managed Cassandra clusters, and
Uber’s in-house service provisioning and deployment tools._


Standard ML workflow handled by Michelangelo:
1. Manage data: handle create of data pipeline (generate features, labels,...) +
allow data management in the form of a Feature Store (save features to share
with another project). Detail some technical challenges with online acces (no
HDFS; need to pre-compute). Features in Feature Store are updated daily. Also
created a Domain Specific Language to transform existing features (extract
day-of-week, eg); this DSL is part of the model configuration and therefore
guarantees that the same transforms are applied for training and inference.
2. Train models: _A model configuration specifies the model type,
hyper-parameters, data source reference, and feature DSL expressions, as well as
compute resource requirements (the number of machines, how much memory, whether
or not to use GPUs, etc.). It is used to configure the training job, which is
run on a YARN or Mesos cluster._ At the time of the article, framework only did
offline training. After training completed, publish a report with 
performance metrics and results plots, and save _the original configuration, the learned
parameters, and the evaluation report_. Michelangelo can be used for
hyperparameters search, and works with single models or _partitioned models_,
i.e. models trained on multiple folds.
3. Evaluate models: Michelangelo typically used to identify best model then push
it to production. They have a system to keep track of all experiments run (ie,
all models trained) by storing: basic info (user name, time, duration,...),
datasets used, model configuration (ie, also including features, and even
features importance visualization), results (metrics, charts, full learned
parameters of the trained model, info/data required for model visualization).
4. Deploy models: 3 types of deployment: offline (model packaged in a container,
ready to be loaded on demand), online (model deployed and queried via Remote
Procedure Calls), or library deployment (invoked via Java API). _In all cases,
the required model artifacts (metadata files, model parameter files, and
compiled DSL expressions) are packaged in a ZIP archive and copied to the
relevant hosts across Uber’s data centers using our standard code deployment
infrastructure._ 
5. Make predictions: Framework allows to deploy multiple models to the same
servicing constainer which can be used for A/B testing or seamless model update.
They have a nice summary
[plot](http://1fykyq3mdn5r21tpna3wkdyi-wpengine.netdna-ssl.com/wp-content/uploads/2017/09/image3.png)
of the different scenarios.
6. Monitor predictions: Michelangelo allows to log a percentage of the
prediction data then combine with realized values to calculate real performance
of the model. They can then visualize evoluation of model performance and/or set
threshold for automatic alerts. See
[here](http://1fykyq3mdn5r21tpna3wkdyi-wpengine.netdna-ssl.com/wp-content/uploads/2017/09/image8.png).

Future developments (at the time): autoML, model viz, online learning,
distributed DL.
