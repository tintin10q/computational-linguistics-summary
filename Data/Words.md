# Words 
What is a word? This is a hard question to answer and is very language dependant. Today one might say it is the characters between spaces? But spaces actually didn't exist yet until 400 years ago. There are also languages without words. This is why we have to talk about [morphemes](Morphemes.md) to define it better and to segment words.

This is also why when doing analysis you want to tokenize your text which is basically deciding what the words are from the string. 

## Losing information
You always loose information when normalizing, so you have to be careful. Often you want to lose this information but for instance God and god can mean different things. Or so and soooooo can be considered the same or not it depends. You might care about this difference and loose it if you normalize it. 

## Ambious words
- gold-digger, 2 words? 1 word?
- Clitecs: I'm, 2 words? 1 word?
- Abbreviations: e.t.c. 3 words? 1 word?

You can keep going. 

This is why you have tokenizers that turn the text into tokens. The tokens don't have this problem.

## LCD
LCD is a standard for tokenizing. 

For instance, you always consider . a separate token. Abbreviations are one word. Doesn't should be tokenized as does and n't. The people that made LCD thought hard about what tokenizing decisions should be made.

## Representing words as numbers 
We usually think of words and letters as [symbols](Symbol.md). In that case each symbol identical to itself and equally different from all other symbols of the same type. 

Alternatively you can also encode words and letters as numbers or [lists of numbers](../Semantic-Similarity/Vector%20semantics.md) (vectors) and then a wide range of math tools are available to analyse **graded relations** between symbols. This allows you to say things about how similar dog and cat are for instance.