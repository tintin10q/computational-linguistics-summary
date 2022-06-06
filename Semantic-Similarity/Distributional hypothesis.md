# Distributional hypothesis

The **distributional hypothesis** says that [words](../Data/Words.md) which are [similar](Similarity.md) in meaning tent to appear in the same context and places in [sentences](../Data/Sentences.md). In other words, similar words are used with the same other words. 

For instance, *eye doctor* and *oculist* are a [synonym](Synonyms.md). However, a computer doesn't know this without looking at for instance a [thesaurus](../Data/Thesaurus.md). With the distributional hypothesis, a computer can also [learn](../Other/Learning.md) which words are similar semantically by looking if they appear in the same places and context in sentences. 

So the distributional hypothesis says that two words are more similar when the overlap of their contexts is large.

Models which use the distributional hypothesis are called distributed semantic models (DSM).

> **You shall know a word by the company it keeps**
> J.R. Firth (1957)

## Example 
Suppose you didn’t know the meaning of the word ongchoi (a recent borrowing from Cantonese) but you see it in the following contexts: 
- Ongchoi is delicious sautéed with garlic.
- Ongchoi is superb over rice.
-  ...ongchoi leaves with salty sauces... 

And suppose that you had seen many of these context words in other contexts: 
- ...spinach sautéed with garlic over rice... 
- ...chard stems and leaves are delicious... 
- ...collard greens and other salty leafy greens 

The fact that ongchoi occurs with words like rice and garlic and delicious and salty, as do words like spinach, chard, and collard greens might suggest that ongchoi is a leafy green similar to these other leafy greens. The same thing can be done computationally by just counting words in the context of ongchoi. The computer would not know what ongchoi means, but it would know that it shares meaning with food words. 


## Problem with the distributional hypothesis
One large problem with the distributional hypothesis is that some words can have multiple [senses](../Data/Lemma.md) (multiple meanings). For instance, table can be something like this (sense 1):

![Table](../images/Pasted%20image%2020220603161925.png)

Or something like this (sense 2):

| Number | A     | B   | C   |
| ------ | ----- | --- | --- |
| 1      | Red   | 5   | Birds    |
| 3      | Blue  | 5   | Dogs    |
| 7      | Green | 500 | Green Birds    |

This would mean that a word's [Co-occurrence](Co-occurrence.md) with different contexts both where table means sense 1 and other where it means sense 2. So in a way it does capture the fact that table means 2 things, but this is not great because it means that the table vector will be related with both waiter and cells. But of course in real life we only mean one for instance of sense 2. So it conflates to two meanings. 

Ultimately this leads to lower [similarity](Similarity.md) scores because the part of the vector which is high because of sense 1 will lower the similarity of sense 2. Both cancel each other out and lower the similarity for the other sense.  

So these models don't deal well with [ambiguity](../Languages/Ambiguity.md). Or maybe they deal too well with it? 

[Transformers](../Prediction/Transformers.md) are able to deal with this well. The idea is to compute the embeddings on the fly. Instead of all beforehand.   

