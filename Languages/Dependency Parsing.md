# Dependency parsing
With dependency parsing you start at the root and then you jump from token to token based on grammatical binary relationships.   

You start with the root which then goes into the main verb of the sentence. Then you go to the subject of that verb. Then you get the argument of the verb. Then you get modifiers of the argument. For instance morning. 

![Dependency parsing 1](../images/Pasted%20image%2020220526224636.png)

![](../images/Pasted%20image%2020220526224656.png)

![](../images/Pasted%20image%2020220526224725.png)

So there is no hierarchy you just describe the sentence based on the relationships which exists between the tokens. It is mostly based on structure and not on meaning but you can also base on meaning. 

## What is this for
Dependency parsing explicitly and directly encode information about relationships across  tokens which are often quite buried and hard to see in constituent based trees like a context free grammar.

**Dependency parsing also deals very well with morphological complex languages with free word order** (which is not like English) without needing to have super specific grammar. For instance an affix could mark the subject. For these types of languages [Chunking](Chunking.md) or [Constituency](Constituency.md) based parsing works worse. So its like a set of words connected together by grammar binary relationships. 

The main content words in the sentence are called heads and the relations are based on the heads. 

## Types of relations 
### Clauses 
Syntactic roles like subject object. Like the verb 

### Modifier
There are modifiers of heads like blue sky where blue is a modifier of the head sky.  

## Data structure 
After you have analysed a sentence you can store it as a graph and you can store a graph as a set of tuples with two items. $\set{(a,b), (b,c), (c,d)}$. So in this sentence there would be an arc from $a$ to $b$, $b$ to $c$ and $c$ to $d$. 

We call this here $G$ with $G = (V,A)$ where $V$ is a set of vertices (tokens in the vocabulary or stems and affixes) so like the sentence or what you can connect. $A$ is a labelled ordered pais of vertices (the arcs). This includes the type of the binary relationship as well.   

$V$ is what you can connect and $A$ is how it is connected.

## Dependency tree

A dependency tree is a **directed graph** where 

- There is one root node with no incoming arc.
- Every other vertex has exactly one incoming arc. 
- There is only one path from the root to each vertex in V. 

These conditions are necessary to have the dependency tree in the way we care about.

## How to get these models?
Using special [Treebanks](../Data/Treebank.md). Dependency treebanks. Linguists have created [Corpora](../Data/Corpus.md) with annotated typed binary directed decency relations that are used to  train dependency parsers. 

If you don't have a dependency treebank you can also use deterministic approaches with a constituent based treebank but this does not work very well. A trained linguist can do better. 

## Evaluation

### Label score
This checks if it went to the correct label. So its ok if you come from the good head as long as where the relationship goes is the correct label. 

### Unlabelled score
This does not checks if it went to the correct label. So its ok if you come from the correct head as long as where the relationship goes is the correct head. 

### Label detached score

This combines the labelled and unlabelled scores. 

This scores how many estimated dependencies have the same head and dependent as the gold standard and also the correct type. 