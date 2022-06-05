# Words 
What is a word? This is a hard question to answer and is very language dependant. Today, one might say it is the characters between spaces? But spaces actually didn't exist yet until 400 years ago. There are also languages without words. This is why we have to talk about [morphemes](Morphemes.md) to define it better and to segment words.

This is also why when doing analysis, you want to tokenize your text, which is basically deciding what the words are from the string. 

## Representing words as numbers 
We usually think of words and letters as [symbols](Symbol.md). In that case, each symbol identical to itself and equally different from all other symbols of the same [type](Type.md). 

Alternatively, you can also encode words and letters as numbers or [lists of numbers](../Semantic-Similarity/Vector%20semantics.md) 
called vectors or [embeddings](../Semantic-Similarity/Embeddings.md). When you do this, a wide range of math tools become available to analyse **graded relations** between symbols. This allows you to say things about how similar dog and cat are. 