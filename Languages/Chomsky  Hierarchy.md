## Types of grammars 
The Chomsky hierarchy species types of languages. 

- Type 0: unrestricted grammars, recursively enumerable languages. 
	-	Require a Turing machine for acceptance (successful parsing)
	-	As expressive as any other computational formalism 
-	Type 1: Context sensitive grammars and languages 
-	Type 2: [context free grammars](Context%20free%20grammars.md) and languages 
	-	Parsed using a push down automata in polynomial time
-	Type 3: [Regular grammars and languages](Regular%20Languages.md) 
	-	Recognized by a finite state automata
	-	Require only linear time and constant space
	-	Equivalent to [regular expressions](Regular%20expression.md) 