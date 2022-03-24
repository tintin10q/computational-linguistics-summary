# Thesaurus
A thesaurus is a resource that groups words by how similar their meaning is, from synonymy to autonomy, sometimes enriched with other relations and definitions. The difference between a thesaurus and a dictionary is that a thesaurus also has the relationships between words its like a network instead of a flat list. 

The most famous thesaurus for English is WordNet. There are also **glosses** which is an explanation of what a word means. There are nouns; verbs and adjectives and adverbs. In WordNet, you have synsets (near-synonym sets) a set of things that are very similar because nothing is actually exactly the same. These synsets are connected by hypernym -hyponym (is a) relations. This seems like category theory but with one function instead of a functor? So for example a dog is a mammal and a human is also a mammal. 

So you can traverse this tree, and then you can see how long it takes to get to another category. This is called the path length or maximum similarity. Two words are more similar the shorter the path that connects them.

![Pasted image 20220213185844.png](Pasted%20image%2020220213185844.png)

So here the path length between vehicle and plant is 3? But don't forget that here the plant is a synset of words that are in the synset plants. 

## Resinic similarity
The Resinic similarity is a special similarity. You can look at it as the information-content weighted path length: two words are more similar the **higher the information content** of their lowest common subsume. 

> **A common subsume** is a connection that both words have. So a common subsume of tree and flower is plant. Or lion and whale is mammal. Then you look at the closest one?

> **The information** is based on how often something occurs. The more often something occurs the lower the information content. Just like Shannon tells us. The more often something occurs the lower the entropy and the lower the information content. You can calculate it with 1/n where n is how frequently it occurs. 
> It makes sense. For instance if a sentence starts with "the" then almost anything can follow but if the sentence starts with "Rainbows" then much fewer things can follow that.

So in the example above the Resnick similarity of whale and lion is lower than finch and penguin. Because mammal occurs more than bird. You would think at least. 

## Lesk similarity
This type of similarity looks at the lexical overlap of the glosses of words. Two words are more similar the higher the lexical overlap between the glosses.

**Lexical overlap** is just the number of overlapping words in the glosses. So for instance: 

Cat: **Feline** mammal usually having thick soft fur and no ability to roar. 
Lion: Large gregarious predatory **feline** of Africa and India having a tawny coat with a shaggy mane in the male. 
Car: A motor vehicle with four wheels; usually propelled by an internal combustion engine. 

Cat and lion share a word so their Lesk similarity is higher than cat and car. But on first glance cat and car look more similar. Only one letter difference. 