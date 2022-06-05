# Normalization

Normalization is the act of trying to reduce noise, so the signal becomes stronger, and so it can be picked up. When analysing a text, normalization can be useful. This can entail:

- Segmenting sentences from text
- Segmenting individual words (tokenization)
- Lemmatization
- Spelling correcting
- Making everything lowercase. 
- Eliminating undesirable characteristics
- Remove the most frequent [words](Words.md).

Sometimes you want to create a bag of words after you have done lemmatization if you don't care about the variability between dog and dogs. 

You can also use [regular expressions](../Languages/Regular%20expression.md) to transfer words that you consider the same into the same word. Or transfer all email address to EMAIL. Or you could say DAYOFWEEK for each week day. 

## Losing information
You always lose information when normalizing, so you have to be careful. Often you want to lose this information, but for instance God and god can mean different things and things like this you might want to keep. Or so and soooooo can be considered the same or not, it depends. You might care about this difference and loose it if you normalize it. 

## Ambiguous words
- gold-digger, 2 words? 1 word?
- Clitecs: I'm, 2 words? 1 word?
- Abbreviations: e.t.c. 3 words? 1 word?

You can keep going. 

This is why you have **tokenizers** that turn the text into tokens. The tokens don't have this problem.

### LCD

LCD is a standard for tokenizing . 

For instance, you always consider `.` a separate token. Abbreviations are one word. `Doesn't` should be tokenized, as `does` and `n't`. The people that made LCD thought hard about what tokenizing decisions should be made.

