# Distance between vectors 
There are a large number of ways to calculate the similarity between two [vector semantics](Vector%20semantics.md) or [embeddings](Embeddings.md). You want to have the distance between points in space. There are a large number of ways to calculate distance between points in space. The ones discussed in the course are [Jaccard's distance](Jaccard's%20distance.md), [Euclidian distance](Euclidian%20distance.md),  and [cosine](Cosine.md).

Jaccard is to compare [Co-occurrence](Co-occurrence.md) sets.  [Euclidian distance](Euclidian%20distance.md) while being a more intuitive distance measure, it is very  influenced by just one coordinate of the vector being far removed from another word in the [embeddings space](Embeddings.md). Cosine is much better than Euclidian, as cosine gives prominence to similarity in relative values.

![Cosine vs Euclidian](../images/Pasted%20image%2020220602232429.png)

In this figure above, if a vector is high in y it occurs often with pet and high in x occurs high in road.  The absolute distance between possum and monocycle is very small, but the angle is large. While the angle of cat and possum is more similar, which is also correct.  