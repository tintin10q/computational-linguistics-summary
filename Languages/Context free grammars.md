# Context free grammars
The context free grammars are grammars where you can form rules of the form:

- N = (N $\cup$ $\sum$)*

The left hand side can only be ONE non terminal. The right hand side can be any ordered combination of terminals and non termianls, of any length. 

Context free grammars are much more expressive than [[Languages/regular languages]].

You can [[Languages/parsing|parse]] context free grammars with parser combinators, parser generators or the [[Languages/CKY]] algorithm which might just be a parser combinator.  