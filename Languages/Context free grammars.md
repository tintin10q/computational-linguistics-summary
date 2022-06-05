# Context free grammars

The context free grammars are grammars where you can form rules of the form:

- N = (N $\cup$ $\sum$)*

The left-hand side can only be ONE non-terminal. The right-hand side can be any ordered combination of terminals and non-terminals, of any length. 

Context free grammars are much more expressive than [regular grammars](Regular%20Languages.md).

You can [parse](Parsing.md) context free grammars with parser combinators, parser generators or the [CKY](CKY.md) algorithm. There are a lot more options as well. 

Context free grammars are called context free because there is no [context](../Semantic-Similarity/Context.md) on the right-hand side of the [grammar](Grammar.md) production, as in there is only one non-terminal on the right. Knowing this makes parsing much easier. 

