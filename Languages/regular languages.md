# Regular languages
A regular language is a [Languages](Languages.md) that can be described by a grammar where all the productions are in the following form:
 
 - S → xB
 - B → b

This defines a langauges of a sequence of x and then one b at the end. 

Where x is a possibly empty **sequence** of terminals and A and B are nonterminals. Every right hand side has at most one non terminal that must occur at the end.

You can see the overlap between [finite state automata](finite%20state%20automata.md). You have one state and you can go to another. 

We call a language regular if it can be described by a regular grammer. Those are grammars like the above.

Regular languages can be described by [regular expression](Regular%20expression.md).

Often the first grammar production is S.
