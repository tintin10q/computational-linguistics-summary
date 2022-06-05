# Chomsky Normal Form

A [Grammar](Grammar.md) is in **Chomsky Normal Form** if each production rule has one of the following forms:

-   S → BC
-   B → x

Here A B and C are non-terminals. 

- x is a terminal. 
- S is the start symbol of the grammar.
  
Any non-terminal which is not the start state can not be empty. So **B and C cannot be S**. If it's not the start state, it's not empty.

So what is important is that each non-terminal can only be rewritten to a rule with ends in only one terminal. So you can have Ab, but not Abb. 

These are the bullet points from the slide. A grammar is in CNF if:
- There are no rules generating the empty string
- Rules have either terminals or sequence of two non-terminals as the right-hand side.

You can rewrite any [Context free grammars](Context%20free%20grammars.md) to Chomsky normal form. This means you can also rewrite any [regular grammar](Regular%20Languages.md) to Chomsky normal form.


