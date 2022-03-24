# Perplexity

Perplexity is the standard way to intricately evaluate whether a predication system is working. Perplexity computes **how surprised** the system is of seeing what it is actually sees in the light of what it expected to see given what it knows. 

What the prediction system expects is caused by the training data. 

## More formally
At any new token in the data, the language model outputs a probability for every possible type as a continuation given the previously observed history and the transition probability matrix it [learned](Learning.md) on some other data. 

**The higher the probability a model assigns to new valid sentences , the better the language model.**

Perplexity based cased by the interaction of the model and the test set. But really it is caused by the test set because the model is a probability distribution matrix over the test set. This means that you can say that perplexity is the **inverse probability** of the test set under a language model, [normalized](Normalization.md) by the number of tokens (the more tokens there are, the lower the final probability of a sequence). In maths this is:

$$p(W) = 2^{-l}$$ where $$l = \frac{1}{|w|}\sum\limits^{|W|}_{i=1}\log p(w_i|w_{i-i-n:i-1})$$ with $w_{i} \in W$ where W is a sequence of tokens. 

So basically you have to normalize the perplexity to compare language models. Which means that you can only compare the complexity of models that use the same test set. 

## Best practices for evolution
1. Estimate the [language model](Language%20Modeling.md) (states and transition matrix) on some corpus. 
2. Fine tune the model on different corpus (test data)
3. Test the model to check how it fits on new data (validation data). 

NEVER test on the same data you trained on and NEVER validate on the test data! **[Learning](Learning.md) is not remembering.** If it were, it wouldn't be useful.  

Again you can only compare perplexity of different models if you use the same test set. Because otherwise the probability distribution is not the same. So the result states have to be the same.

Perplexity is an average, so it depends on the number of tokens in the vocabulary.