# Word similarity 
Sometimes [words](../Data/Words.md) are [synonyms](../Languages/Synonyms.md) of each other. But they can also be related in other ways. For instance, coffee and cup are related but might not seem related to a computer. 

## Asking humans 
One way is asking humans to say how related they think word pairs are and using those scores. This requires a lot of effort. 

### Semantic fields 
One way of asking humans is by asking them if a word belongs to a semantic field. Words that are in the semantic field *hospital* could be related like surgeon, scalpel, nurse, aesthetic, hospital, operation, disease, recovery and so on. 

**Topic models** use semantic fields to discover abstract semantic fields in documents. A topic model can say which semantic fields are similar. 

Semantic fields and topic models can be used to discover the topical structure of a document using unsupervised [learning](../Other/Learning.md). 

### Semantic Frames
A semantic frame is a set of words which encapsulate perspectives or participants in a particular type of event. For instance, a commercial transaction is an event where one entity trades something (usually money) to another entity in return for something valuable like a service or a some goods. Now verbs like buy, sell or nouns like buyer, seller, goods, money, service encode this event lexically. Frames have semantic roles, and words in the sentence take roles in the event. Knowing about the frame allows paraphrasing a sentence: *Quinten bought the book from Ling* as *Ling sold the book to Quinten,* for example. 

## Using vectors 
You can get a sense of the meaning of words by [assigning vectors to words](Vector%20semantics.md). This approximates meaning. Basically the computer can never grasp the meaning of a word, but it can know if two words are likely to mean the same / are [synonyms](../Languages/Synonyms.md) because the vectors are [similar](Similarity.md). The closeness is dependent on the way you decide to calculate distance, usually this is done with [cosine](Cosine.md). 
