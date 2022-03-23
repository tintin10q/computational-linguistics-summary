# Markov models 
When you actually try to implement a language model you are implementing a Markov model or a Markov Chain.

A Markov model is any model which makes use of the [markov assumption](markov%20assumption.md). A markov model is defined by:

- A set of history states **Q** $\set{q_{1},q_{2}, q_{3}, ..., q_{n}}$ 
- A set of predicted states **R** $\set{r_{1},r_{2}, r_{3}, ..., r_{m}}$ (What you try to predict)
- A transition probability matrix A (size: NxM)
- An initial probability distribution $\pi$

## States
In a bigram model, Q and R are the same set. With larger n-gram models they are not the same. Q is bigger then R because the histrories are longer. 

A difference between Q and R is that Q will contain the BoS while R contains the EoS.

## Transition matrix 
The transition probability matrix A encodes the probability of going from a state $q \in Q$ to a state $r \in R$, such that a cell $a_{ij} \in A$ with $i \leq |Q|$ and $j \leq |R|$ encodes the probabilitiy of finding state j given state i.

Q usually corresponds to the rows of A and R to the collums. This is done, so we can get relative frequencies by row-normalizing counts. 

## Initial distribution 
This is starting state. The initial distribution is given by the transitions between states Q which only consits of BoS symbols and the r states. This is where all sequences start. The initical distribtion can be set in advance or estimated. 

This is usually just embeded in A by augmenting Q with the BoS state.

So usually this a row in A with only beginning of sequence symbols. It is the inital state.

![Pasted image 20220223185953](../images/Pasted%20image%2020220223185953.webp)

Looking at this table really makes it more concrete. The idea is that the sum of an the entire row is one. The sum of a collum does not have to be one. 

## Fine tuning
How do you decide on the n-gram size? The [lambda's](Smoothing.md)? Which [discounting](Smoothing.md) method you will use? What k will you use if you use Laplace etc.

We can do this like any other machine learning problem. In this case the loss/cost/error function is [perplexity](perplexity.md) and we want to minimize it. Try to minimize the perplexity of the dev set by tuning the hyperparameters.  


## Trade of
Higher N-grams are more constraining and precise, but more sparce. If we have 20k [types](../Data/Type.md), then there are:
- 20K$^2$ bigrams = $4*10^8$. 
- 20K$^{3}$ trigrams = $8 * 10^{12}$. 
- 20K$^{4}$ tetragrams = $1.6 * 10^{17}$. 

So you need to have the data to support this otherwise you will hit something you have not seen before too often. 

THIS is why [Normalization](../Data/Normalization.md) is important because it reduces the number of different histrories from which you can predict. 