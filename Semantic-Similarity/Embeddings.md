# Embeddings
The vectors derived by looking at [context](Context.md) are called **embeddings**. This new name is given because you can't directly interpret the resulting vectors any more, like you can with [connotation](Connotations.md) vectors. Although embeddings derived by counting are still very interpretable. It more means that to interpret one column, you need the other columns. But embedding is basically a [synonym](../Languages/Synonyms.md) for vector part of a [vector space](Vector%20Space.md). Embeddings are used in the more recent literature. 

There are many ways to derive these vectors which all differ and result in different sizes. 
Depending on how the vectors are derived the same word (the same surface from, as in it could also be tokens) can also have the different embeddings.  However, **the actual values of the vector don't mean anything by themselves**. You can't interpret the numbers like you can with connotations, it is just to find the distance to other embeddings. The dimensions of an embedding space are **not symbolic**. 

Below is a 60 dimensional embedding space [projected](Dimensionality%20reduction.md) down to 2 dimensions.  

![A two-dimensional (t-SNE) projection of embeddings for some words and phrases, showing that words with similar meanings are nearby in space](../images/Pasted%20image%2020220601145459.png)

Using word embeddings seems to work really well in [Natural Language](../Languages/Natural%20languages.md) Processing (NLP) applications as it allows comparing words on a deeper level than where they appear beyond just [symbols](../Data/Symbol.md) which are all equally different. With embeddings, words can be compared through where they appear in the n-dimensional space. Embeddings are used everywhere because they work really well. 

For instance, [classification](../Classification.md) models can assign sentiment as long as some words seem to have [similar](Word%20similarity.md) meanings, i.e. being close to other positive sentiment words in the embedding n-dimensional space. 

## Deriving embeddings 
### One hot encoding 
To change the categorical data into numbers, you can use one hot encoding. The idea is to make a Boolean dimension features for each possible category, in this case words. This results in something like this:

|       | Cat | Food | Music | Beans |
| ----- | --- | ---- | ----- | ----- |
| Cat   | 1   | 0    | 0     | 0     |
| Food  | 0   | 1    | 0     | 0     |
| Music | 0   | 0    | 1     | 0     |
| Beans | 0   | 0    | 0     | 1     | 

This does not really encode the meaning though. 

### Co-occurrence 
One way to derive embeddings is to use [co-occurrence](Co-occurrence.md) (counts). The idea is to count and put in a table how often some words occur in a context with other words. This encodes meaning because according to the [Distributional hypothesis](Distributional%20hypothesis.md), words with the same meaning are used around the same words. So words which mean the same should result in similar vectors.

This is much like how our cognition deals with words. There are much more ways to get embeddings from words, supervised and non supervised, with different hyperparameters to tweak. Some might work better for the problem you are trying to solve than others. 

This generates **[Vector Space](Vector%20Space.md)**. A vector space is like an all the generated occurrence count vectors stacked on top of each other to form a matrix from the vectors. We can put all the embeddings in a matrix because they all occupy the same space. All the vectors are the same length. 

This is how a vector space might look like (real ones are much bigger):

|       | Cat | Food | Music | Beans |
| ----- | --- | ---- | ----- | ----- |
| Cat   | 20  | 16   | 2     | 6     |
| Food  | 16  | 21    | 1     | 70    |
| Music | 2   | 1    | 16    | 0     | 
| Beans | 6   | 70   | 0     | 15     |

Or like below where the contexts are documents. Knowing something about the document will also tell you something about the co-occurrences. 

|       | Document 1 | Document 2 | Document 3 | Document 4 |
| ----- | ---------- | ---------- | ---------- | ---------- |
| Cat   | x          | 16         | 2          | 6          |
| Food  | 16         | x          | 1          | 70         |
| Music | 2          | 1          | x          | 0          |
| Beans | 6          | 70         | 0          | x          |


The rows (word at the left) are the target words, and each column keeps track if a word occurred in the context of that target word.  

There are a lot of different variations you can apply when deriving embeddings. You can leave out the top x most frequent words, as these don't provide a lot of information, for example. 

Usually you also apply an [association measure](Association%20measure.md) to in an attempt to bring out more useful information and lower less important information. 

### Neural networks 
Instead of using counting to derive embeddings, you can also use machine learning techniques to derive embeddings. In particular, using [Feed forward neural networks (FFNN)](../Prediction/Feed%20forward%20neural%20networks%20(FFNN).md). This has the advantage of getting dense vectors immediately instead of first having sparse embeddings and then projecting them into lower dimensions like with the count based methods. A popular way to do this is [Word2Vec](Word2Vec.md).  

