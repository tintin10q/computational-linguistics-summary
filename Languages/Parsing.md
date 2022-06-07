# Parsing

Parsing is proving that a sequence is in the [language](Languages.md) set. 

Parsing can be described by a problem statement:

Given a grammar G and a string s. Does s belong to L(G). Or $s \in L(G)$$

L is a function that returns the [languages](Languages.md) set from a [grammar](Grammar.md). Many problems can be reduced to parsing problems. 

> 	Having a parser for a language is extremely useful. For instance, if you load a .json file into Python and turn it into a dictionary, this is actually parsing happening. The JSON parser verifies (create a proof with a parse tree) that the content of the file you opened belonged to the JSON language. If this is the case Python can use the resulting parse tree to construct the dict. 
> 	
> 	Standard protocols like https, json or toml or pdf are often just standardized languages which means everyone can use the same parsers.  
> 	
> 	Compiling programming languages are also just parsing problems with a code generation step at the end using the parse tree. This is why programming language input has to be 100% correct. If the computer can't parse your code, no parse tree, and then nothing can happen. 
 
If the parser thinks this is the case, we also want a proof or evidence that this is the case. This usually takes the form of a [parse tree](Parse%20Tree.md). So this is a tree to go from the grammar to s! But it can also make a [Dependency graph](Dependency%20Parsing.md).

![Parse Tree vs Brackets](Pasted%20image%2020220314184733.png)

You can also represent parse trees with brackets. But this is only done because of language limitations. 

Of course, a *no parse* answer is also always possible. It is also possible to prove that a sequence does not belong to a language set, but this is harder. One way to do it is with pumping lemmas. 

An example of a succesvol parsing is like defining [regular expression](Regular%20expression.md) that finds something. If they find something, then you have a valid parse and your sequence belongs to the language. If they don't then you don't have a valid parse and your sequence does not belong to the language set under the given grammar. 

# Approaches to parsing

The [CKY](CKY.md) algorithm is a way to parse [Context free grammars](Context%20free%20grammars.md). More approaches are below:  

## Parser generator

You give this a grammar, and it generates a parser for your grammar.

- External program
- Based on a bottom up algorithm, usually LL or LR
- Can be complex theory
- Limited look ahead, usually one token
- Only build in abstractions (from the program you use)
- Generated parsers are extremely fast!
- An example is [Regular expressions](Regular%20expression.md) you define the grammar and the parser program ([finite state machine](finite%20state%20automata.md)) is generated. 

## Parser Combinators 
- Library
- Based on top down algorithm
- Underlying theory is simple
- In principle unlimited look-ahead
- User definable abstractions
- Fast as long as certain constructions are not used (like a lot of look ahead)

A combinator is a self-contained function in lambda calculus. The formal system that is the basis of Haskell and other functional programming languages. So parser combinators are a set of small (library) functions that can be used to construct parsers for parts of the language. The idea is that in context free languages, the context can't change the parse of the string. This allows you to write parser combinators for small problems, which can then be combined to parse bigger problems, basically writing the [Constituents](Constituency.md) as parser functions and building until you have covered the entire grammar. This results in one function which can parse the entire grammar, starting at the most abstract. 

Both approaches place certain but different restrictions on the grammar that you can use.

## Handrolling your own parser
-   You can also do whatever you want with while and for loops, but this can get quite hard and messy quick.


## Complexity 

![Complexity of a parse tree](Pasted%20image%2020220314190559.png)

If a parse tree is deep or long, then the sentence tends to be more complex. 

