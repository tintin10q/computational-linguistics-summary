# Cosine 
The **cosine** [similarity](Similarity.md) can calculate the semantic similarity between two [words](../Data/Words.md), [sentences](../Data/Sentences.md) or two documents when represented as [vectors](Vector%20semantics.md) or [embeddings](Embeddings.md). 

The idea of the cosine metric when comparing [embeddings](Word%20similarity.md) is to calculate the cosine of the angle between the vectors (in n-dimensional space) This means that the two word vectors you want to compare have to have the same shape/dimensionality. 

Let's say we have the words Village and Waiter and those are represented with the vectors **v** and **w** of the same size. Now we want to use cosine to calculate the similarity of **v** and **w**. First you can take the dot product of the two vectors: $$\textbf{v} \cdot \textbf{w}$$
> **Reminder**
> Dot product is defined as: $$\sum\limits_{i=1}^Nv_iw_i=v_1w_1+v_2w_2+...+v_Nw_N$$

The dot product acts as a similarity metric because it will tend to be high just when the two vectors have large values in the same dimensions and vectors that have zeros in different dimensions (orthogonal vectors) will have a dot product of 0, representing their strong dissimilarity.

This raw dot product favours vector length long vectors because the dot product is higher if a vector is longer (with higher values in each dimension). More frequent words have longer vectors, since they tend to co-occur with more words and have higher co-occurrence values with each of them. 

This is not good because it would mean longer vectors are more similar, which doesn't make sense. Longer here is not the number of items in the vector, it is the length of the vector from the center of the n-dimensional space to 'final location' of the vector. See below:

> The vector length is written as $|\textbf{v}|$ so with those two | |
> The vector length is defined as: $$|\textbf{v}| = \sqrt{\sum\limits^{N}_{i=1}{v^2_i}}$$ 
> So you take the sum of the elements after you multiplied all the elements of the vector by themselves, and then you take the square root of that.  

We would like a similarity metric that tells us how similar two words are regardless of their frequency. To overcome this issue, we modify the dot product to normalize for the vector length by dividing the dot product by the lengths of each of the two vectors. $$\frac{\textbf{v} \cdot \textbf{w}}{|\textbf{v}||\textbf{w}|}$$
This normalized dot product turns out to be the same as the cosine of the angle between the two vectors . 

$$\frac{\textbf{v} \cdot \textbf{w}}{|\textbf{v}||\textbf{w}|} = \cos{\theta}$$
So then this is also true:$$\textbf{v} \cdot \textbf{w} = |\textbf{v}||\textbf{w}| \cos{\theta}$$
This means we calculate the **cosine** metric between two vectors **v** and **w** as: $$\text{cosine}(\textbf{v},\textbf{w}) = \frac{\textbf{v} \cdot \textbf{w}}{|\textbf{v}||\textbf{w}|} = \frac{\sum\limits^N_{i=1}{v_iw_i}}{\sqrt{\sum\limits^N_{i=1}{v_i^2}}\sqrt{\sum\limits^N_{i=1}{w_i^2}}}$$
These are all the same. Even though the most to the right looks daunting, it is just the dot product on top and the vector length calculations expressed with the sum sigma notation.


![Cosine distance](../images/Pasted%20image%2020220606220028.png)