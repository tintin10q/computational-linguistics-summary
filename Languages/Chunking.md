# Chunking
Sometimes you don't need the full [parse tree](Parse%20Tree.md) of a sentence, but you only need the main building blocks of a sentence. This is also called shallow or partial [parsing](Parsing.md). 

Chunking stays on the surface level. There is only one layer of non-terminals, and the non-terminals can not be rewritten to other non-terminals. 

The idea of chunking is that you chop a sentence into non-terminals or chunks. These chunks don't overlap, and you are not going to chunk the chunk.

Chunks are not recursive, they never contain smaller phrases of the same type.  

## Example

**The man** - *guarding* - **the door** - *fell asleep* - **and the thieves** -- *managed to enter* -- **the building and run away** - ~~with the diamonds~~.

So here we have verbs and nouns and at the end a prepositional phrase. 

So it boils down to determining the boundaries of the chunks.  For instance, you can keep going until you hit something that is not in the same group as before and if it's not, you put a boundary. So you do **splitting**, but you also **classify** what the chunk is. 

## Evaluation
A correct chunk starts and ends at the right place and has the right token. We use precision, recall and f1 scores to evaluate this. 

**Precision** is the ratio between the correct chunk produced by the system and all the chunks produced by the system. **Recall** weights the correct chunks over the correct chunks in the text. F-measure combines recall and precision. 

### Parseval 

 Parseval is a competition to evaluate chunking algorithms. This measures to what existent the [constituents](Constituency.md) in the hypothesized parses look like the actual constituents, defined by linguists (gold standard [corpus](../Data/Corpus.md) with annotations is required for this)

Performance is assessed at the constituent level because parsers will probably make some mistakes. 



