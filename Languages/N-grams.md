# N-Gram 

N-Grams is a contiguous sequence of _n_ items from a given sample of text or speech.

When doing [Normalization](../Data/Normalization.md) of a sequence, your first intuition when working with a language that has spaces might be to split the words along the spaces, but often having shorter splits of maybe 2-3 symbols gives better results. These remaining symbols are N-grams. So when splitting this sentence: "Attack at dawn" up into 3-Grams you get:  ["Att", "ack", " at", "Daw", "n"]

## Word N-Gram
A word N-Gram is a sequence of n words:
- Uni-Gram: Dog
- Uni-Gram: You are 
- Tri-Gram: The building blocks 
- Tetra-Gram: City of shivering darkness 
...


## Encoding position
[Naïve Bayes Classifier](../Classification/Native%20baiyes/Naïve%20Bayes%20Classifier.md) is bad for making [language models](../Prediction/Language%20Modeling.md) because the bag of words assumption but the idea where it splits off the words to normalize the probability can also be used for making language models. 

## Predicting N-grams
A great use case for N-grams is using them for language models. 

### Predicting next word
For instance, to predict the next word: How likely is it that given words W1 to Wn we observe Wn+1? So given a Tree, how likely is it we observe a number. 

### Predicting the likelihood of whole sentences
Out of all the sequences of n words, how likely is sequence A? Out of all sequences of 6 words, how likely is “The earth revolves around the sun”. 

## Getting probabilities 

We can calculate chance of number given A tree has with : $$p(\text{leaves}|\text{A tree has }) = \text{c}\frac{\text{leaves}}{\text{c(a tree has)}}$$

Here c is a count function which counts how many times “a tree has” appears (regardless of continuation) in the big [corpus](../Data/Corpus.md) and how many times it is followed by “leaves” in the corpus. Then you divide them to get a probability. This is always between 0…1 because the continuation is at most all the times, and then you get x/x = 1.


### Probabilities for sequences 
To get the probability for a sequence we do the same, but we divide how often the sequence you are interested in appears by the number of all the sequences of the same length. So for 4 word sequences that is: $$p(\text{a tree has leaves}) = \text{c}\frac{\text{c(a tree has leaves)}}{\text{c(sequences of 4 words)}}$$

Because there are probably a lot more sequences of the length than the sequence that you are interested in, the probabilities are going to be very small (sparse). So small even that it could be considered unreliable. This is why it is better to calculate the probability of a sentence based on the probability of each word * the probability of the words before it appearing before it. We can just calculate the probabilities like this because of the **probabilities chain rule**. So that looks like this: $$p(w_{1},...,w_{m})$$ $$= p(w_{1} \cdot p(w_2|w_{1}) \cdot p(w_3|w_{1},w_{2}) \cdot ... p(w_{m}|w_1,...,w_{m-1})$$ $$=\prod_{{i}=1}^m(p(w_i|w_{1:i-1}))$$

So every time, you multiply the probability of the word by the probability of the sequence before it. This you repeat for the entire sequence. 

### Problem's 
Language is infinite, which makes language models age, but it also means that you can come up with sequences that are not in the corpus. The higher the n of an n-gram, the lower the chance that the n-gram appears at all in the corpus. Or the larger the n-gram, the higher the chance that we won't find it anywhere in a finite corpus. This is solved by assuming the [Markov assumption](../Prediction/Markov%20assumption.md).

### Log space
Whenever you deal with chained probabilities, it is best to convert all probabilities to logs so that we can sum instead of multiplying and avoid having very little numbers. This is a risk because of underflow. (Computers can't deal well with very small numbers). Another benefit is that we can sum instead of having to multiply. 

$$\log \text{p}(w_{1},...,w_{m} \approx \sum\limits^{m}_{i=1} (\log p(w_{i}|w_{i-n:i-1}))$$


## Sequence boundaries
It is very important to put sequence boundaries at the start and end of your sequence. When using N-grams the start boundaries need to be N-symbols long while the end boundaries are N-1. This way there you can still have valid N-grams. 

### Example
^^Hi there^ when using bigrams. This way you can go over the text with n-gram length. Kind of like a sliding window, but you still know what is at the start because of the ^. 

### Abbreviations 

End of sequence is activated so EoS. 
Beginning of sequence is activated so BoS. 

## Overfitting
The longer the N-gram choice the better you can fit the specific training data you have, which means the more chance of [Overfitting](../Prediction/Overfitting.md). The more overfitting, the less general your model becomes. 

