# Smoothing 

Smoothing (in the context of language models) means increasing all the probabilities of a probability distribution by a little bit, so you don't have impossible continuations (zero probability). What it does is that we never say that a probability of a transition or N-gram occurring is zero. We just make it a small number above zero but never zero.

## The infinite problem
When training [language models](Language%20Modeling.md) you always have the problem that [Natural languages](../Languages/Natural%20languages.md) are infinite. This means that any sample that you train your model on is actually just a small sample of the entire data or population. It is a **finite number** of [tokens](../Data/Token.md), [types](../Data/Type.md) and [lemmas](../Data/Lemma.md). This also means that the it is guaranteed that a model will encounter things it has never seen before in the future. This will cause the model to say that a sequence is ungrammatical. Most often this is true and what we want, but it could be false. 

### Unknown words  (OOV words)

If the model encounters a word it didn't see in training it can't even start looking for transitions from the preceding [N-gram](../Languages/N-grams.md). This can be quantified in the [OOV rate](OOV%20rate.md) (percentage of never seen before words in the test set). Because language is infinite the OOV rate will always be more than 0 when using the model in the wild. 

### Zipfian 
Because natural language follows a [Zipfian Distribution](../Languages/Zipfian%20Distribution.md) there are a lot of words that only appear once in a [corpus](../Data/Corpus.md) less but still a lot of words that appear twice in a corpus but not a lot of words that often appear in a corpus. 

Because there are few words that appear often and a lot of words that appear once or twice in a corpus the sequences that contain rare words are frequent. So transitions with rare words are frequent but hard to predict. Because you can't just have of the same words. So how do you estimate rare transitions?

## Solutions
How do we deal with this all this?

### Make it a close world
We pretend that an open vocabulary situation is a closed vocabulary problem where we know all the possible words in advance by replacing some words in training (usually the rare ones) with a single token, for instance called |UNK|. Then, with this token you make the maximum likelihood estimates the usual way. Now in the future you can just replace all the unknown words in a new sentence with |UNK| and you can use your model again with any sentence. Pretty clever I would say. This is basically normalization by replacing all the unknown words with the unknown words token. Kind of like replacing all the emails addresses with the EMAIL token.

Basically we say rare things are the same. We leverage the relationship between rare things that they are rare. 

You can look at this by saying that you reserve some probability mass for unknown words. 

## The zero probability transition problem
Replacing words that the model hasn't seen before with a special token solves part of the problem but what if the model encounters a transition that it has not seen before? This means an N-Gram that doesn't appear in the transition matrix. Then the model will think that the probability of it occurring is zero. As soon as this happens the model will get stuck because [Markov models](Markov%20models.md) uses the Markov chains which means that if you multiply by 0 or take the log of 0 you get problems. So we can not afford the probability of a word or transition to be 0. 

![Probability distributions before smoothing](../images/Pasted%20image%2020220224152619.png)

In this example the continuation painful, horrible and boring is zero and that is a problem. 

To solve this zero probability transition problem we apply **smoothing**. 

If we were to apply smoothing on the model from the picture from before we would get:

![Probability distributions after smoothing](../images/Pasted%20image%2020220224152946.png)

Now everything is above zero. 

Of course there are multiple algorithms to do smoothing with different results.

### Laplace
The Laplace smooth method just adds 1 to all frequency counts of words before normalization. We have to be sure that we can still turn the frequencies into a probability distribution. 

For transitions this means that transitions with a frequency of 0 in the training corpus get a frequency of 1, transition with a frequency of 1 get a frequency of 2, ... In maths this looks like $$c^{*}= (c+1)\frac{N}{N+V}$$ 
Where N is the number of tokens, V is the number of types and c is a count of how often something occurs in the training data.

In the lecture Laplace smoothing is called a quick and dirty solution. Because with large vocabularies and not so high frequencies, smoothed probability are too different from the non-smoothed ones. This is because there are only 100 percentage points to give out and even if we assign a little probability to unobserved transitions, there are still really a lot of unobserved transitions. This makes it so that the probability distribution shifts a lot. This is captured in the image below:

![Result of Laplace parsing](../images/Pasted%20image%2020220224154616.png)

We want that what we don't observe gets a small probability but because there are so many things we didn't observe adding 1 to every count makes what we didn't observe a lot more likely than we would like. 

#### Add K
An improvement is to decrease the amount of probability mass which gets moved around by adding less than 1 to each count. We can just add 0.001 or something in the probability. Now the smoothing looks like this: $$p^{*}(W_{n}|W_{n-1}) = \frac{c(W_{n-1}\cdot W_{n}) + k}{c(W_{n-1}) + k \cdot V}$$

This means adding less than one. Apparently you have to do k on both sides otherwise it is not a probability any more. 

But really this is just a hack upon a hack. Estimates have too little variance and are still off. 

### Interpolation Smoothing
We can try to look at more sources of data and assigns weights to the data which indicates how sure we are about it. Higher weights to more reliable sources of knowledge. 

#### Linear combinations
This interpolation is done with linear combinations. The idea is to always also consider transitions for smaller n-grams using a weighted linear combination of the probabilities. So you look at other N-grams and assign a weight to each different type of N-gram which indicates how much you want to rely on the data. The weights are called $\lambda$ here. This causes the formula for a probability of a transition in a language model to look like this (When considering trigrams): $$\hat{p}=(w_i|w_{n-2}, w_{n-1}) = \lambda_1(w_i|w_{n-2}, w_{n-1}) + \lambda_2(w_{i}|w_{n-1}) + \lambda_3(w_i)$$

This math translates to: 

the probability of a word given the previous word and the previous word
= the probability of the word given the previous word and the previous word \* a weight 
\+ the probability of the word given the previous word \* a weight 
\+ the probability of the word alone \* a weight. 

Everything on the right comes from the probability distribution. 

So you assign weights to each source of information, telling you something about the probability. This allows you to consider different N-grams because we can add another constrained: $\lambda_{1}+ \lambda_{2} + \lambda_{3} = 1$. Of course, the amount of lambda's depends on the N you choose for your N-Grams. 

Now the trick is that $\lambda_3(w_i)$ is never zero because we are still applying the closed word assumption. If we don't know the word, it turns into |UNK| and that (also) has a probability of occurring. Just like the probability of other words. So as long as $\lambda_3$ is not zero, this formula with linear combinations will never be zero. Even if the transitions are 0. 

### Back off 

Backof is an algorithm that instead of doing weights reclusively uses the best source of information it can find.  So if there is an 4-Gram use that, but if there is not then go to 3-gram etc until, if you have to, use probability of the word and disregard the context. This never fails because of the |UNK| token if it is needed.  

Anytime a transition from an n-gram to a state found in the test set didn't occur in training, recursively fall back on to the smaller n-grams (For example from "why did you" to "did you" to "you") until a non-zero transition is found. 

This sounds really good. But it does mean that you no longer have probabilities because you no longer have the thing that the lambdas add up to 1. 