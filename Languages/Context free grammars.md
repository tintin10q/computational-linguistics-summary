# Context free grammars

The context free grammars are grammars where you can form rules of the form:

- N = (N $\cup$ $\sum$)*

The left-hand side can only be ONE non-terminal. The right-hand side can be any ordered combination of terminals and non-terminals, of any length. 

Context free grammars are much more expressive than [Regular Languages](Regular%20Languages.md).

You can [parse](Parsing.md) context free grammars with parser combinators, parser generators or the [CKY](CKY.md) algorithm which might just be a parser combinator.  

## Context 
The context are the parts of a discourse that surround a word or passage and can throw light on its meaning. So the [words](../Data/Words.md) or [tokens](../Data/Token.md) around the words or tokens you are analysing. 

To learn about the meaning of a word you can look/count the words surrounding the words your interested in (the context). If you do this with a lot of text you get an idea of what the context around a particular word usually is. Then you can compare the context of one word with the context of another word to see how similar it is. If the context seems similar the word probably means something similar. This can be said based on the [distributional hypothesis](../Semantic-Similarity/Distributional%20hypothesis.md). From these counts of words appearing in the context you can also construct a [vector](../Semantic-Similarity/Vector%20semantics.md) which words really well as you can then compare words based on how [close](../Semantic-Similarity/Similarity.md) the vectors are.

This is very much the same as the [Lesk similarity](../Data/Thesaurus.md). There you check the overlap in the glosses of two words in the [thesaurus](../Data/Thesaurus.md). But with context you just do it with the contexts of words in a [corpus](../Data/Corpus.md). Arguably this is better as for this no human annotation is required. 

This approximates meaning. Basically the computer can never grasp the meaning of a word but it can know if two words are likely to mean the same / are [synonyms](../Languages/Synonyms.md) because the vectors are close. 