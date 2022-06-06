# Using FFNN for language modelling
You can also use [Feed forward neural networks (FFNN)](Feed%20forward%20neural%20networks%20(FFNN).md) for language modelling. These models make the same [Markov assumption](Markov%20assumption.md) as [Markov chain models](Markov%20models.md). So the neural network is tasked with finding the preceding word to the n-gram it gets as input. FFNN seem to work better than models based on a large matrix of probabilities.

The neural networks are very popular because of the following advantages:

## Advantages of FFNN 
- No need to apply [Smoothing](Smoothing.md) 
- Can handle longer histories ([N-gram](../Languages/N-grams.md) with large n)
- Generalize better over histories consisting of similar but not identical words. 

The main reason why this approach works and the reason for these advantages is because [embeddings](../Semantic-Similarity/Embeddings.md) are used to represent the words. Embeddings are an antidote to sparsity. A better antidote than smoothing. They also allow the model to deal with n-grams they have not seen before by just comparing them with vectors which are [similar](../Semantic-Similarity/Similarity.md) (are close together in the [Vector Space](../Semantic-Similarity/Vector%20Space.md) and thus probably have similar meaning) and just using those vectors. 

### Example
So for example if the model has not seen the n-gram “the silver pike” but it does have the word embeddings for “the”, “silver” and “pike”. The model can look for similar embeddings for all of these words for which it has seen an n-gram. So a close embedding to “silver” is "blue" and a close embedding to “pike” is “fish”. Then the model has seen the engram “the blue fish” before, and the most likely next token after that was stored as “swims”. So based on all that, the model will assign a high probability to “swims” as the next word. 

## What does it mean

So you can see that you can use embeddings to switch out words which you the model doesn't know much about to other words which the model knows more about. This removes the need to move probability space around like with smoothing. 

You can use higher n with the n-grams when using embeddings. This increases the change that you get an N-gram you haven't seen because, but the neural network models can deal with this by switching the tokens you have not seen before with the closest embeddings you have seen before. With [Markov chains](Markov%20models.md), when you encounter an N-gram you have not seen before you are basically out of luck and you have to use [smoothing](Smoothing.md). However, you can still not increase N by a huge amount as you will still need larger corpora when you do and there is a limit as you will run in to the language is infinite problem.

## How to get embeddings 
You can get off the shelves embeddings which have been trained by someone else. These you can also fine tune to your specific problem. You can of course use any corpus that you want. The N-grams of some corpus might work better for your problem. You can also derive your own embeddings of course.  The embeddings derived by the big companies will be much larger than you can probably ever really make. 

## Can we get rid of the Markov assumption 

The [Markov assumption](Markov%20assumption.md) **limits the size of context arbitrarily** by specifying only one n in the n-grams. Sometimes however we care about short windows and sometimes we care about longer windows. But so far we have always been using the same n while saying that a higher n will lead to better predictions (if you have enough data to back it up). Recurrence can be used to overcome this problem. 

FFNN still assume the Markov assumption. We can use [recurrence](Recurrence.md) to overcome this problem. This leads to recurrent neural networks. 

