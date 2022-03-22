# Markov Assumption
The Markov assumption says (in the language modeling domain) that the conditional probability of a word apearing next in the sequence can be approximated by looking at its local history instead of the entire history. In this case the preceding history is an [n-gram](N-grams.md) of words which indicates how far you look back.  This can be expresed with math as: $$p(W_{1},...,W_{m}) `\approx \prod^{m}_{i = 1}(p(W_{i}|W_{i-n:i-1}))$$

The sequence of symbols you consider to try predict the next symbols is called the context. The bigger the N in N-gram the bigger the context.

So basically don't look at the entire history but just look at the context (an N-gram at the end). 

## Bigram model
With the Bigram model you take N=2. Only look at the preceding word as history and then find the probability of the next word. 

So if you use this model and try to predict what comes after "a tree has" and you look at  "leaves" then you would get p(has|leaves). You would get p(a tree has|leaves) if you where to consider the entire history. 

So here we are working under the assumption: $\text{p}(\text{a tree has}|\text{leaves}) \approx \text{p}(\text{has}|\text{leaves})$

The nice thing here is that "has leaves" is much more likely to appear in a [Corpus](Corpus.md) than "a tree if leaves". This is good because if your n-gram does not appear at all in the corpus the probability will be 0. 

### Pros
- Easy to estimate transitions, reduces sparcity. 
- We can use smaller corpera.
- The chance that you don't find the n-gram in the corpus is the smallest as possible.

### Cons
- Throws away a lot of information as can be seen above. Tree gives a lot of information much more then has. But you could filter words like has out with [normalization](Normalization.md) because that in general does not give a lot of information. 


### Maximum likelihood 
The probabilities that we compute are maximum likelihood estimates. So if we wanted to do has leaves it would be: 

1. Find and record the occures of "has" followed by the word "leaves". 
2. Devide by the frequency count of all the bigrams that start with "has" regarless of what follows (frequency of "has").

If we do this then we maximize the liklihood of the corpus used to collect the counts. This means that given the model, the iput corpus is the likeliest set of sequences we could expect in the [language models](Language%20Modeling.md). This makes sense because the data that the model is based on decides the probability distrobutions. 

## How to choose n?
Choosing n is a trade of between being able to predict and the information needed. In practical applications, trigrams (or higher) models are usually preferred to bigram models. A reason for this is that practical application often use larger corpera. Because if you increase n you really need much larger copera to be able to predict things. 

The higher the n the more fine-grained the information, the weaker the Markov assumption, and the more severse the sparcity. 