# Smoothing 

Increasing all the probabilities by a little bit, so you don't have impossible continuations (zero probability). 

## The problem
When training [[Language Modeling|language models]] you always have the problem that [[Natural languages]] are infinite. This means that any sample that you train your model on is actually just a small sample of the entire data or population. It is a **finite number** of [[Token|tokens]], [[Type|types]] and [[Lemma|lemmas]]. This also means that the model will encounter things it has never seen before in the future. This will cause the model to say that a sequence is ungrammatical. Most often this is true and what we want, but it could be false. 

### Unknown words  (OOV words)

If the model encounters a word it didn't see in training it can't even start looking for transitions from the preceeding [[N-grams|N-gram]]. This can be quantified in the [[OOV rate]] (percentage of never seen before words in the test set). Because language is infinite the OOV rate will always be more than 0 when using the model in the wild. 

### Zipfian 
Because natural language follows a [[Zipfian Distribution]] there are a lot of words that only appear once in a [[Corpus|corpus]] less but still a lot of words that appear twice in a corpus but not a lot of words that often appear in a corpus. 

Because there are few words that appear often and a lot of words that appear once or twice in a corpus the sequences that contain rare words are frequent. So transitions with rare words are frequent but hard to predict. Because you can't just have of the same words. So how do you estimate rare transitions?


## Solutions
How do we deal with this all this?

### Make it a close world
We pretend that an open vocabulary situation is a closed vocabulary problem where we know all the possible words in advance by replacing some words in training (usually the rare ones) with a single token. This is for instance called |UNK|. With this token you can make the maximum likelihood estimates the usual way. Now in the future you can just replace all the unknown words with |UNK| and you can use your model again. Pretty clever I would say. This is basically normalization by replacing all the unknown words with the unknown words token. It is like replacing all the emails addresses with the EMAIL token.

Basically we say rare things are the same. We leverage the relationship between rare things that they are rare. 

You can look at this by saying that you reserve some probability mass for unknown words. 

### The zero problem
Replacing words that the model hasn't seen before with a special token solves part of the problem but what if the model encounters a transition that it has not seen before? This means an N-Gram that doesn't appear in the transition matrix. Then the model will think that the probability of it occurring is zero. As soon as this happens the model will get stuck because [[Markov models]] uses the Markov chains which means that if you multiply by 0 or take the log of 0 you get problems. So we can not afford the probability of a word or transition to be 0. 

![[Pasted image 20220224152619.webp]]

In this example the continuation painful, horrible and boring is zero and that is a problem. 

# Smoothing 
To solve this zero probability problem we apply **smoothing**. What it does is that we never say that a probability of a transition or N-gram occurring is zero. We just make it a small number above zero but never zero.

So if we were to apply smoothing on the model from the picture from before we would get:

![[Pasted image 20220224152946.webp]]

Now everything is above zero. 

Of course there are multiple algorithms to do smoothing with different results.

## Laplace
The Laplace smooth method just adds 1 to all frequency counts of words before normalization. We have to be sure that we can still turn the frequencies into a probability distribution. 

For transitions this means that transitions with a frequency of 0 in the training corpus get a frequency of 1, transition with a frequency of 1 get a frequency of 2, ... In maths this looks like $$c^{*}= (c+1)\frac{N}{N+V}$$ Where N is the number of tokens, V is the number of types and c is a count of how often something occurs in the training data.

G. Cassani calls Laplace smoothing a quick and dirty solution. Because with large vocabularies and not so high frequencies, smoothed probability are too different from the non-smoothed ones.  The reason for this is basically that because there are only 100 percentage points to give out and even if we assign a little probability to unobserved transitions, there are still really a lot of unobserved transitions. This makes it so that the probability distribution shifts a lot. This is captured in the image below:

![[Pasted image 20220224154616.webp]]

We want that what we don't observe gets a small probability but because there are so many things we didn't observe adding 1 to everything makes what we didn't observe a lot more likely than we would like. 

### Add K
An improvement is to decrease the amount of probability mass which gets moved around by adding less than 1 to each count. We can just add 0.001 or something in the probability. Now the smoothing looks like this: $$p^{*}(W_{n}|W_{n-1}) = \frac{c(W_{n-1}\cdot W_{n}) + k}{c(W_{n-1}) + k \cdot V}$$

This means adding less than one. Apparently you have to do k on both sides otherwise it is not a probability any more. 

But really this is just a hack upon a hack. Estimates have too little variance and are still off. 

## Interpolation
We can try to look at more sources of data and assigns weights to the data which indicates how sure we are about it. Higher weights to more reliable sources of knowledge. 

### Linear combinations
This is done with linear combinations. The idea is to always also consider transitions for smaller n-grams using a weighted linear combination of the probabilities. So you look at other N-grams and assign a weight to each different type of N-gram which indicates how much you want to rely on the data. The weights are called $\lambda$ here. This causes the formula for a probability of a transition in a language model to look like this (When considering trigrams): $$\hat{p}=(w_i|w_{n-2}, w_{n-1}) = \lambda_1(w_i|w_{n-2}, w_{n-1}) + \lambda_2(w_{i}|w_{n-1}) + \lambda_3(w_i)$$

The probability of a word given the previous word and the previous word is the probability of the word given the previous word and the previous word times a weight plus the probability of the word given the previous word times a weight plus the probability of the word alone times a weight. Everything on the right comes from the probability distribution. 

So you assign weights to each source of information telling you something about the probability. This allows you to consider different N-grams because we can add another constrained: $\lambda_{1}+ \lambda_{2} + \lambda_{3} = 1$. Of course the amount of lambda's depends on the N you choose for your N-Grams. 

Now the trick is that $\lambda_3(w_i)$ is never zero because of the closed word assumption we made a little earlier. If we don't know the word it turns into |UNK| and that (also) has a probability of occuring. Just like the probability of other words. So as long as $\lambda_3$ is not zero this formula with linear combinations will never be zero. Even if the transitions are 0. 

### Backoff 
Backof is an algoritm that instead of doing weights recusivaly uses the best source of information it can find.  So if there is an 4-Gram use that but if there is not. Then go to 3-Gram etc until if you have to, you get to the probability of the word. 

Anytime a transition from an n-gram to a state found in the test set didn't ocur in training, recursively fall back on to the smaller n-grams (from why did you to did you to you for example) until a non-zero transition is found. 

This sounds really good. But it does mean that you no longer have probabilities because you no longer have the thing that the lambda s add up to 1. 