#### Context 

Latent Dirichlet allocation (LDA) is a generative statistical model in natural language processing, and can be used to discover ‘topics’ in a large set of documents. This is first presented by David Blei, Andrew Ng, and Michael Jordan.

The key idea is that if we see a ‘topic’ as a collection of certain words, we can look at each document as a collection of topics, the proportion of each topic depends on the proportion of words in the document that are associated with that topic. For example, the ‘sports’ topic may consist of the words: tennis, football, gymnastics. When given a set of documents, we can calculate the posterior distribution for the topics. In the original LDA paper, this is done using a coordinate descent algorithm for mean-field variational inference, and later on researchers also used Gibbs Sampling and expectation propagation. In this tutorial we will be looking only at Stochastic Variational Inference for LDA. SVI was first published in 2013 by Matt Hoffman, David Blei, Chong Wang, and John Paisley.

Traditional coordinate-descent variational inference requires each update to be carried out with all of the data, and these updates become inefficient when the dataset gets large as each update scales linearly with the size of the data. The key idea with SVI is to update global variational parameters more frequently. Using local and global parameters, and given the dataset with a known number of datapoints, we could randomly take 1 data point at a time, update the local parameter, and project the change into the global parameters. Like traditional coordinate-descent variational inference, this is done until the result converges, i.e., the change in the global parameters is smaller than a certain value. The implementation we will be talking about is a naive implementation of the algorithm described in the original paper

#### Problem Statement

Using MIT EECS faclty data, perform stochastic variational inference on LDA. 

