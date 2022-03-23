A [[Languages/Grammar.md]] is in **Chomsky Normal Form** if each production rule has one of the following forms:

-   A → BC
-   A → x

Here A B and C are non terminals. x is a terminal. S is the start symbol of the grammar. Also any non terminal which is not the start state can not be empty. So **B and C cannot be S**. If its not the start state its not empty.

So what is important is that each non terminal can only be rewritten to a rule with ends in only one terminal. So you can have Ab but not Abb. 

This are the bullet points from the slide. A grammar is in CNF if:
- There are no rules generating the empty string
- Rules have either terminals or sequence of two non-terminals as the right-hand side.


You can rewrite any [[Languages/Context free grammars.md]] to chomsky normal form. This means you can also rewrite any [[Languages/regular languages.md|regular grammar]] to comsky normal form.