---
layout: post
title: Dimensionality reduction for time series
tags: time-series dimensionality deeplearning ML
---

When provided with a large amount of time-series data, it could be of interest
to compress that information into a lower-dimensional dataset.
This can be done inside a Deep Learning model, but we may also want to test
machine learning approaches, and an offline dimensionality reduction approach
could also benefit a Deep Learning model (e.g., pre-training offline, then
fine-tuning inside the model).

# Deep Learning 
* _Bao, W., Yue, J., & Rao, Y. (2017). A deep learning framework for financial
 time series using stacked autoencoders and long-short term memory. PloS one,
 12(7)_
[link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5510866/pdf/pone.0180944.pdf):
Stacked autoencoders for financial time series; not sure why the need to train
in a stack way (one layer at a time)--could train end-to-end

* _Zhao, R., Deng, Y., Dredze, M., Verma, A., Rosenberg, D., & Stent, A. (2019,
 May). Visual Attention Model for Cross-sectional Stock Return Prediction and
 End-to-End Multimodal Market Representation Learning. In The Thirty-Second
 International Flairs Conference_
[link](http://www.cs.jhu.edu/~mdredze/publications/2019_zhao_flairs.pdf):
deep autoencoder using convolutional layers

 * _Ma, Q., Zheng, J., Li, S., & Cottrell, G. W. (2019). Learning Representations
 for Time Series Clustering. In Advances in Neural Information Processing
 Systems (pp. 3776-3786)_
[link](https://papers.nips.cc/paper/8634-learning-representations-for-time-series-clustering.pdf):
 Recent paper (NeurIPS2019) that combines autoencoder and k-means clustering to
learn representations. Their goal is to learn representation for clustering
though, so not clear if that's really useful for dimensionality reduction as
they will compress one time series at a time (not multiple time series across
time)



## CNN based
* _Bai, S., Kolter, J. Z., & Koltun, V. (2018). An empirical evaluation of
 generic convolutional and recurrent networks for sequence modeling. arXiv
 preprint arXiv:1803.01271._ [link](https://arxiv.org/pdf/1803.01271.pdf):
authors compare TCN with LSTM/GRU and show TCN does a better job at dealing with
sequence data.

* A blog
 [post](https://dida.do/blog/temporal-convolutional-networks-for-sequence-modeling)
 explaining the basics of Temporal Convolutional Network (TCN).

* _Borovykh, A., Bohte, S., & Oosterlee, C. W. (2017). Conditional time series
 forecasting with convolutional neural networks. arXiv preprint
 arXiv:1703.04691_
 [link](https://arxiv.org/pdf/1703.04691.pdf?source=post_page---------------------------): 
Proposes a variation of wavenet specifically targeting forecasting of
multivariate time series and apply it to finance.

* _Sen, R.,
Yu, H. F., & Dhillon, I. S. (2019). Think globally, act locally: A deep neural
network approach to high-dimensional time series forecasting. In Advances in
Neural Information Processing Systems (pp. 4838-4847)_
[link](http://papers.nips.cc/paper/8730-think-globally-act-locally-a-deep-neural-network-approach-to-high-dimensional-time-series-forecasting.pdf):
combines temporal convolution network (TCN) with matrix factorization;
proposes an initialization scheme for TCN that allows high-dimensional data with
different scales.

* _Lai, G., Chang, W. C., Yang, Y., & Liu, H. (2018, June). Modeling long-and
 short-term temporal patterns with deep neural networks. In The 41st
 International ACM SIGIR Conference on Research & Development in Information
 Retrieval (pp. 95-104)._ [link](https://arxiv.org/pdf/1703.07015.pdf): combines
CNN and RNN for time-series prediction.

* _Franceschi, J. Y., Dieuleveut, A., & Jaggi, M. (2019). Unsupervised scalable
 representation learning for multivariate time series. In Advances in Neural
 Information Processing Systems (pp. 4652-4663)_
[link](https://papers.nips.cc/paper/8713-unsupervised-scalable-representation-learning-for-multivariate-time-series.pdf):
an interesting alternative to an AE, where the authors use a negative-sampling
approach (word2vec) to train an encoder (only, not decoder) which is a stacked
TCN.


# Matrix factorization

* standard methods: PCA with randomized SVD/KernelPCA

* _Xu, H., Caramanis, C., & Mannor, S. (2010). Principal component analysis with
 contaminated data: The high dimensional case. arXiv preprint arXiv:1002.4658_
[link](https://arxiv.org/pdf/1002.4658.pdf):
 High-dimensional Robust Principal Component Analysis

* _Yu, H. F., Rao, N., & Dhillon, I. S. (2016). Temporal regularized matrix
factorization for high-dimensional time series prediction. In Advances in neural
information processing systems (pp. 847-855)_
[link](https://papers.nips.cc/paper/6160-temporal-regularized-matrix-factorization-for-high-dimensional-time-series-prediction.pdf):
Matrix factorization that imposes causality in latent space

# Other non Deep-Learning based methods

* Copulas: There are a few papers that use Copulas to encode the dynamic of the
 time series, like for instance this recent
[paper](https://papers.nips.cc/paper/8907-high-dimensional-multivariate-forecasting-with-low-rank-gaussian-copula-processes.pdf).
However, Copulas are only work when the time series are stationary (see
[Wikpedia](https://en.wikipedia.org/wiki/Copula_(probability_theory)#Stationarity_condition)).
This is brushed off in the above paper by saying the time series can simply be
de-trended or differenced. I personally find the stationarity assumption to be a
major shortcoming.
More interestingly, in the paper
[Gaussian Process Conditional Copulas with
Applications to Financial Time
Series](http://papers.nips.cc/paper/5084-gaussian-process-conditional-copulas-with-applications-to-financial-time-series.pdf),
the authors explicitly the time-varying nature of the parameters of the copula.



# Clustering techniques

In order to improve performance, we may want to apply the dimensionality
reduction inside pre-computed clusters of time series. There is a nice review
paper published not too long ago:
* _Aghabozorgi, S., Shirkhorshidi, A. S., & Wah, T. Y. (2015). Time-series
 clustering–a decade review. Information Systems, 53, 16-38_
 [link](https://wiki.smu.edu.sg/18191isss608g1/img_auth.php/f/fd/Time_Series_Clustering_A_Decade_Review.pdf)



