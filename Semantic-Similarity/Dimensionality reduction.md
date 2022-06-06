# Dimensionality reduction 
When using [Co-occurrence](Co-occurrence.md) to derive a [Vector Space](Vector%20Space.md) becomes very large with each row being typically having 10^5 dimensions of which most of the values are 0 because the target words never appearing with other words in the context. This takes a lot of storage and feeds into the curse of dimensionality. 

## Goals 
Every [context](Context.md) is considered an atomic context. This basically means that each context is considered separate. So we consider the context cat and lion to be separate, but they are not. 

So ultimately want to 

- **Reduce noise and brittleness**: Some co-occurrences may happen by chance or under a very specific, non-conventional use of a word. It is a good idea to give these low importance. 
- **Discover latent meaning**: Leverage the fact that some contexts are similar and may represent a broader domain. 

So, how can we reduce the dimensionality of the vector space?

## Projection 
We can project the vector space into a lower dimension. So you turn the matrix into a new matrix with the same number of rows and a lower number of columns. Each column is one dimension and also one context. You can compute which context provides the most information and only keep those contexts around. The columns with low information will have a lot of zeros. You have to decide how many columns to keep. 

More formally, we can **project** the distributional matrix of dimensionality N\*M into a lower-dimensional space N\*K where K < M (and K < N) **such that the reduced space preserves the maximum amount of variance possible**. You only want to get rid of redundant information. This should result in row vectors which are real-valued and dense (not a lot of zeros).

There are a lot of techniques for dimensionality reduction trough projection. There are many ways to project into lower dimensions like:

- Singular Value Decomposition 
- Non-negative Matrix Factorization
- Kernel Principal component Analysis 
- Latent Dirichlet Allocation (used with [Topic models](Word%20similarity.md)). 
- ... (there are more)

 The simplest trimming columns are explained below, in this method. The simplest way to remove not, so useful information from your vector space is to just trim entire columns from the matrix based on how many 0 there are. 

## Trimming Columns 
**When two targets have 0 in the same dimension, it doesn't influence the Cosine** because the angle between 0 and 0 is 0. So there is no reason to keep this around. You can just remove the columns with the most 0 in them, and then keep a certain number of columns around. 

This is quick and transparent (easy to interpret) but it doesn't reduce noise and doesn't bring latent meaning to the surface. Also, you can still interpret the remaining columns as the contexts. 

