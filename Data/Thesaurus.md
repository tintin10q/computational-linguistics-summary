# Thesaurus
A thesaurus is a resource that groups words by how similar their meaning is, from synonimy to antonymy, sometimes enriched with other relations and definitons. The difference between a thesaurus and a dictionary is that a thesaurus also has the relationships between words its like a network instead of a flat list. 

The most famous thesaurus for enlish is wordnet. There are also **glosses** which is an explination of what a word means. There are nouns; verbs and adjectives and adverbs. In wordnet, you have synsets (near-synonym sets) a set of things that are very similar because nothing is actually exactly the same. These synsets are connected by hypernymy-hyponymy (is a) relations. This seems like catogory theory but with one function instead of a functor? So for example a dog is a mammel and a human is also a mammel. 

So you can traverse this tree, and then you can see how long it takes to get to another catogory. This is called the path lenght or maximum similarity. Two words are more similar the shorter the path that connects them.

![Pasted image 20220213185844](../images/Pasted%20image%2020220213185844.png)

So here the path length between vehicle and plant is 3? But don't forget that here the plant is a synset of words that are in the synset plants. 

## Resnic similarity
The resnic similarity is a special similarity. You can look at it as the information-content weighted path lenght: two words are more similar the **higher the information content** of their lowest common subsume. 

> **A common subsume** is a connection that both words have. So a common subsume of tree and flower is plant. Or lion and whale is mammel. Then you look at the closest one?

> **The information** is based on how often something occures. The more often something occures the lower the information content. Just like shannon tells us. The more often something occures the lower the entropy and the lower the information content. You can calculate it with 1/n where n is how frequently it occures. 
> It makes sense. For instance if a sentence starts with "the" then almost anything can follow but if the sentence starts with "Rainbows" then much fewer things can follow that.

So in the example above the resnic similarity of whale and lion is lower than finch and penguin. Because mammel occures more then bird. You would think atleast. 

## Lesk similarity
This type of similarity looks at the lexical overlap of the glosses of words. Two words are more similar the higher the lexical overlap between the glosses.

**Lexical overlap** is just the number of overlapping words in the glosses. So for instance: 

Cat: **Feline** mammal usually having thick soft fur and no ability to roar. 
Lion: Large gregarious predatory **feline** of Africa and India having a tawny coat with a shaggy mane in the male. 
Car: A motor wehicle with four wheels; usually propelled by an internal combusiton engine. 

Cat and lion share a word so their lesk similarity is higher then cat and car. But on first glance cat and car look more similar. Only one letter differnce. 