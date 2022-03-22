# Parts-of-Speech (PoS)

PoS are clusters of words which have a similar behavior in a language. For instance, they have a similar context of occuring, or they can be combined with the same set of morphological affixes. PoS tags are also called lexical clusters. 

You should think of examples as: Nouns, Verbs, Adjectives, Pronouns etc. These parts of speech again contain smaller parts which are even more consistant with themselves. For instance past verbs, present verbs or irregular verbs etc. Different languages have different PoS tags. The more closer a language the more close the PoS. 

## Open Class words
One very famous PoS is the open class of words. This includes nouns, verbs, adjectives, adverbs. This calss is called **productive** because it changes often. New words are added to this class all the time. Other words disapear or go undercover. Typically, open class words are content words. This means the words that convey the contents of a message. Most lanagues have all 4 major open classes.

## Closed Class Words
This class is words is closed. It includes conjunctions, determiners, pronouns, prepositionsm, etc. This class is **not productive**. It barly changes and is basically fixed. The words in this class can be contained in a single courses. 


## Special corpora 
There are special corpora with information about the PoS of every word in it. Examples are:
- Brown Corpus - 1 milion words, balanced
- WSJ - 1 milion words, news articals 
- Switchboard - 2 milion words, transcribed phone conversations

Often these annotations are hand corrected versions of an automated system which assigned PoS to words. How is this done in an automated way? Doing this is called PoS tagging. 

# PoS Tagging
The process of **automatically** assigning PoS tags to words in a corpus. This process takes a tokenized corpus as input and outputs a sequence of PoS tags for each input token. 

First of all why not just have a list of words and their PoS tags? We could even use dictionaries for this. We can't do this because of [ambiguity](Ambiguity.md). PoS tagging aims to resolve this ambiguity.  

PoS tagging is usefull for [parsing](parsing.md), named entity recognition and coreference resolution and more!

## Baseline
Most of the [types](Type.md) in a corpus are nouns. The baseline is to assume everything is a noun. This will get you an accuracy of around 60% on types, but much lower on tokens.  

## Most frequent 
We can already do better by looking at the most frequent examples of tags. Cat can be a verb, but it is almost always a noun. If you hit an ambiguous word then you just assign the most frequent PoS tag (which is noun). However, if you do this you are bound to make mistakes because you are ignoring the lower frequency explicitly. 

## Context
Can we do better? We can look at words that come before to predict a PoS just like with [Language Modeling](Language%20Modeling.md). You can also look at words that come after (preceding words).