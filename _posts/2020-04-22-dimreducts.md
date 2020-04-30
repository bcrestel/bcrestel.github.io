---
layout: post
title: Dimensionality reduction for time series
tags: time-series dimensionality deeplearning ML
---

One of the challenges of this project is to handle the sheer size of the data.
Starting with over a 100,000 features, this number is beyond reach for any
modern machine learning or deep learning forecasting model. We therefore need to
find a way to compress that information to a manageable size, meaning a 100x or
even 1,000x compression factor. The intent of this section is to review the
literature on the techniques we can apply to reach that ambitious compression
rate.

The classical appraoch for dimensionality reduction remains Principal Component
Analysis (PCA), which boils down to a Singular Value Decomposition (SVD) of the
matrix formed by all time serie stacked column-wise. For a probabilistic
interpretation, time series would be centered to zero. Then after decomposition
into principal components, we could retain only the first few components that
describe an acceptable percentage of the variance in the data. As described the
underlying machinery of PCA is a SVD which can quickly become intractable in
high dimension. In "Randomized numerical linear algebra: Foundations &
algorithms" [martinsson2020randomized], the authors describe how the tools from
randomized numerical linear algebra can facilitate SVD in very large dimension,
given that we're only interested in keeping a small number of dominant principal
components.  Another limitation of standard PCA is its brittleness in the
presence of corrupted data. In the presence of sometimes of even a small
fraction of outliers, the quality of the output of a standard PCA can
dramatically deterioriate. To remedy that shortcoming, several robust PCA
techniques have been developped in the low-dimensional regime. In "Principal
component analysis with contaminated data: The high dimensional case"
[xu2010principal], the authors introduced a robust PCA technique that can handle
up to 50% of corruption in high dimensional datasets.
PCA, despite its popularity, does not address some specificities of time series
datasets. In [yu2016temporal] ("Temporal regularized matrix factorization for
high-dimensional time series prediction"), the authors introduce a matrix
factorization technique that assumes a temporal dynamic in latent space,
therefore providing more sensible results.
In a different, albeit potentially complementary approach, we could first
cluster the time series [aghabozorgi2015time] ("Time-series clustering--a decade
review"), then apply a dimensionality reduction like PCA inside each cluster.

With the all the advantages of matrix factorization techniques, these methods
remain fundamentally linear. Kernel PCA was developped to remedy that potential
shortcoming. But with very large datasets, deep learning methods become an
interesting alternative. In this section, we survey the use of autoencoders
[goodfellow2016deep, ballard1987modular] to perform dimensionality reduction on
large multivariate time series.
Interestingly, we still find a number of papers in finance relying on
greedy layer-wise training of autoencoders (also referred to as stacked
autoencoders), like the highly cited
[bao2017deep](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5510866/pdf/pone.0180944.pdf).
However we do not explore that area of the literature, as it is believe today
that modern deep learning does not require this approach.
More traditionally, the standard approach for multivariate datasets would be to
encode across the features, at each time step. This could be done with a
fully-connected auto-encoder, but in order to capture the dynamics of the time
series, recurrent layers would be required.
More recently [bai2018empirical], it was shown that convolutional networks, in
particular a simple 1D dilated convolution model like the Temporal Convolutional
Network (TCN), can be better suited than recurrent networks for sequence modeling.





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



