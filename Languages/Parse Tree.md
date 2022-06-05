# Parse Tree

A parse tree is a proof that you can parse a sentence of a language under a certain [grammar](Grammar.md). If the sequence is properly formed according to the productions of a certain grammar, then you can create the parse tree to show how you can [parse](Parsing.md) it. Parse trees are basically the proof of a parse while also being a useful data structure. Parse trees are useful because one you have them, computers can iterate over them while being able to make assumptions the grammar gives them. 

You make a parse tree by using the [grammar](Grammar.md) rules to make a path from the input sequence to non-terminals to terminals. Then you can then visualize these paths with a parse tree.

![Pasted image 20211127140252](Pasted%20image%2020211127140252.webp)

When multiple parse trees exist under a grammar for the same input, you have a grammar with [ambiguity](Ambiguity.md). One way to resolve this ambiguity is by using a [Probabilistic Context Free Grammar](Probabilistic%20Context%20Free%20Grammar.md).