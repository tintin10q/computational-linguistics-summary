# Vector Semantics
The idea of vector semantics is to represent words (or your surface form) as a vector of numbers. These vectors represent a word, a point in a multidimensional semantic space. This allows you to compare the words on a deeper level because vectors can be more or less [Similar](Similarity.md)  instead of being all equally different or based on [Edit distance](../Languages/Edit%20distance.md).  

These vectors can be derived from the distributions of word neighbours / context of the other words because of the [distributional hypothesis](Distributional%20hypothesis.md). This allows computers to compare the meaning of words with just a [corpus](../Data/Corpus.md) and without something like [wordnet](../Data/Thesaurus.md). This is deeper than looking at [edit distance](../Languages/Edit%20distance.md).

## Getting the vectors 
An early idea to get the vectors was with [connotations](Connotations.md). This requires humans to annotate data in a 3 dimensional space of valence, arousal and dominance. Later, linguists started looking at the [context](Context.md) around words to create the vectors. 

### Connotations
Early on this was done with [connotations](Connotations.md). The idea is to ask a bunch of humans to rate words along the valence arousal and dominance dimensions and average the results. This then gives you vectors 3 numbers for each word. An advantage of connotations is that the resulting vectors can be meaningfully interpreted. If a word has a vector of high valence, then you know it is probably a positive sentiment word.  

### Context
Later, linguists started looking at [context](Context.md). This can yield vector representations from a corpus without needing humans. One way of doing this is with counting. You can use an algorithm that scans a corpus and counts which words are used close to other words. If eye dokter and oculist are used in the same contexts next to the same words, then the computer will assign the similar vectors to these words meaning, as they will be close in the vector space. This is based on the [distributional hypothesis](Distributional%20hypothesis.md). Ways of getting the vectors include [Co-occurrence (counting)](Co-occurrence.md) and using hidden layers of neural networks like  [Feed forward neural networks (FFNN)](../Prediction/Feed%20forward%20neural%20networks%20(FFNN).md) for instance using [Word2Vec](Word2Vec.md) or [Recurrent neural network (RNN)](../Prediction/Recurrent%20neural%20network%20(RNN).md) .  

All the vectors have a place in a [vector space](Vector%20Space.md) this allows to compare them.

The vectors derived from context are also called [embeddings](Embeddings.md) in the more recent literature. This new name is given because you can't directly interpret the resulting vectors any more, like you can with connotation vectors. 

## The pipeline 
So how to you do get the vectors? 
1. Choose a [Context](Context.md) size (documents, sentences, paragraphs etc.)
2. Derive the base vectors either by using [Co-occurrence](Co-occurrence.md) or [machine learning techniques](../Classification/Logistic%20Regression.md) (Word2Vec). 
3. Choose an [Association measure](Association%20measure.md) like [PMI](Point%20wise%20mutual%20information%20(PMI).md) or don't.
4. Use a [Dimensionality reduction](Dimensionality%20reduction.md) technique, or don't.
5. Use a [Similarity](Similarity.md) measure to compare vectors. Basically always [Cosine](Cosine.md).

Models that use this pipeline fall under the name of **distributional semantic models**. Which all make use of the distributional hypothesis. 