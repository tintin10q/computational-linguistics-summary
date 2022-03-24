# Normalization
When analysing a text normalization can be useful. Normalization is the act of trying to reduce noise, so the signal becomes stronger, and so it can be picked up. This can entail:

- Segmenting sentences from text
- Segmenting individual words (tokenization)
- Lemmatization
- Spelling correcting
- Making everything lowercase. 
- Eliminating undesirable characteristics
- Remove the most frequent words

Sometimes you want to create a bag of words after you have done lemmatization if you don't care about the variability between dog and dogs. 

You can also use [regular expressions](Regular%20expression.md) to transfer words that you consider the same into the same word. Or transfer all email address to EMAIL. Or you could say DAYOFWEEK for each week day. 

