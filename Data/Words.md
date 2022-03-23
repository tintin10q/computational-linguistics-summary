# Words 
What is a word? This is a hard question to awnser and is very language dependant. Today one might say it is the characters between spaces? But spaces actually didn't exist yet until 400 years ago. There are also langauges without words. This is why we have to talk about [Morphemes](Data/Morphemes.md) to define it better and to segment words.

This is also why when doing analysis you want to tokenize your text which is basically deciding what the words are from the string. 

## Losing information
You always loose information when normalizing so you have to be carefull. Often you want to lose this information but for intance God and god can mean different things. Or so and soooooo can be considered the same or not it depends. You might care about this difference and loose it if you normalize it. 

## Ambious words
- gold-digger, 2 words? 1 word?
- clitecs: I'm, 2 words? 1 word?
- abbreviations: e.t.c. 3 words? 1 word?

You can keep going. 

This is why you have tokenizers that turns the text into tokens. The tokens don't have this problem.

# LCD
LCD is a standart for tokenizing. 

For instance, you always consider . a seperate token. Abberivatios are one word. Doesn't is should be tokenised as does n't. The people that made LCD thought hard about what tokenizing decisions should be made.



