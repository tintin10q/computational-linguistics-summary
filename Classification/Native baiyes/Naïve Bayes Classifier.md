# Naïve Bayes Classifier
Using Bayesian statistics to decide on a class. Given this what would the class be if we consider the chance for all classes. You take the percentage for that has the highest class. There are also 2 assumptions you have to make.

This is the simplest linear generative probabilistic [classifier](../Classification.md). Given a document d, it returns a probability of certainly, so that is nice.

Given a document d, it returns the class c with the highest posterior probability given the document. Because the probability of a document is constant we can simply the Bayes rule to $$c = \text{argmax}_{c \in C}~p(c|d)$$
For text, the assumptions are bag of words and naïve Bayes. 

## Bag of words 

The bag of words assumption says that you deal with a bag of words instead of a text. A bag is a set where items can occur multiple times. A multi set. 

![Pasted image 20220215090517](../../images/Pasted%20image%2020220215090517.webp)

## Naïve Bayes assumption
Here you assume that the tokens in the bag are all independent based on the class. So a class doesn't cause that words are in it. At least that is what we assume because this allows us to just multiply probabilities. 

The second is commonly called the naïve Bayes assumption: this is the conditional independence assumption that the probabilities P( fi |c)

![Pasted image 20220215090607](../../images/Pasted%20image%2020220215090607.webp)

If you don't assume this, you can't multiply them because you also need to multiply the probability of them both occurring at the same time. 

## Prior 
The Prior is what you thought beforehand of how likely the output class will be. It is like bias. It is like the naïve classifier if you could not consider any data. So you would just simply say OK the language is Chinese because that is the most spoken.

The prior probabilities for each class are approximated as $p(c) = \frac{N_{\text{classes}}}{N_{\text{documents}}}$ 

You always have a tiny subset of language. 

## Likelihood 

Likelihood is approximated by: $p(f|c) = \text{count}\sum\limits~\text{count}(f|c)$

### Smoothing
What if there is not a feature for a certain class? Then we multiply once by 0 that messes everything up. So we can either add one to every count or add one and add the number of features.

$$p(f|c) = \frac{\text{count}(f|c)+1}{\sum\limits~\text{count}(f|c) + |F|} = \frac{\text{count}(f|c)+1}{\sum\limits~\text{count}(f|c) + 1} $$

F is the entire set of features. Otherwise, the probabilities are wrong if you only add missing features. 

## Out of vocabulary word  
If you don't have a word in the training set, then you can't assign probabilities to it. So you basically just have to remove these words from the input.

## Stop Word  
Some words occur super often and so are uninformative, so you can also just filter them out. For instance, "the" occurs, so frequently it really doesn't tell you much. But if you try to classify languages, you wouldn't want to remove these. 

# Example 

Let's say you want to do sentiment detection.

You have these sentences
The movie was awful!  
The actors were not believable!  
Meh, did not like it.  
I have seen better movies...  
Horrible!  
Too long...

The movie was amazing!  
The actors were incredible!  
I liked it a lot.  
Never seen anything better.

Then we create a table of negative or positive.  

| Word       | Negative | Positive |
| ---------- | -------- | -------- |
| movie      | 2        | 1        |
| awful      | 1        | 0        |
| actor      | 1        | 1        |
| !          | 2        | 2        |
| ...        | 2        | 0        |
| believable | 1        | 0        |
| meh        | 1        | 0        |
| do         | 1        | 0        |
| like       | 1        | 1        |
| have       | 1        | 0        |
| see        | 1        | 1        |
| good       | 1        | 1        |
| amazing    | 0        | 1        |
| incredible | 0        | 1        |
| lot        | 0        | 1        |
| never      | 0        | 1        |
| anything   | 0        | 1        |
| horrible   | 1        | 0        |
| too        | 1        | 0        |
| long       | 1        | 0        |


Then we smooth so add 1. 

| Word       | Negative | Positive |
| ---------- | -------- | -------- |
| movie      | 3        | 2        |
| awful      | 2        | 1        |
| actor      | 2        | 2        |
| !          | 3        | 3        |
| ...        | 3        | 1        |
| believable | 2        | 1        |
| meh        | 2        | 1        |
| do         | 2        | 1        |
| like       | 2        | 2        |
| have       | 2        | 1        |
| see        | 2        | 2        |
| good       | 2        | 2        |
| amazing    | 1        | 2        |
| incredible | 1        | 2        |
| lot        | 1        | 2        |
| never      | 1        | 2        |
| anything   | 1        | 2        |
| horrible   | 2        | 1        | 
| too        | 2        | 1        |
| long       | 2        | 1        |

Now we can make probabilities from this:

![Pasted image 20220216154345](../../images/Pasted%20image%2020220216154345.webp)

Now we can Test lets say we have: "I liked the movie a lot!"

Normalisation → like movie lot !  

```
p(neg|test) = p(neg) * p(test|neg)  
			  p(neg) * p(like|neg) * p(movie|neg) * p(lot|neg) * p(!|neg)  
			  0.6 * 0.5 * 0.6 * 0.33 * 0.5 = 0.0297  

p(pos|test) = p(pos) * p(test|pos)  
			  p(pos) * p(like|pos) * p(movie|pos) * p(lot|pos) * p(!|pos)  
              0.4 * 0.5 * 0.4 * 0.67 * 0.5 = 0.0268  

argmax(p(neg|test), p(pos|test)) = 0.0297 = neg


```
We assign the label neg to the test text.

# Naïeve Bayes for language models 
Are Naïve Bayes a good fit for [language models](../../Prediction/Language%20Modeling.md)? No, they are not. With language models, we try to predict how fluent a sentence is. For this, we exploit the previous sequence. Because of the bag of words assumption, we throw all this information away. 