# Parsing

Parsing is proving that a sequence is in the language set. 

Parsing can be described by a problem statement.

Given a grammar G and a string s. Does s belong to L(G). Or s∈L(G)

L is a function that returns the [language](app://obsidian.md/language) from a [grammar](app://obsidian.md/grammar).

If the parser thinks this is the case we also want a proof or evidence that this is the case. This usually takes the form of a [parse tree](parsetree.md). So this is a tree to go from the grammar to s!

![[Pasted image 20220314184733.png]]

You can also represent parse trees with brackets. But this is only done because of language limitations. Haskell can represent parse trees without problems. 

Ofcourse a no awnser is also ok.

So this is like definig regualer expression that find something! If they find something then you have a valid language. But using haskell is better because then we could get the parse tree altough I think with regulair expressions you also get that.

# Approaches to parsing

## Parser generator

You give this a grammar and it generates a parser for your grammar.

-   External program
-   Based on a bottom up algorithm, usually LL or LR
-   Complex theory
-   Limited look ahead, usually one token
-   Only build in abstractions (from the program you use)
-   Generated parsers are extremely fast!

## Parser combinators (haskell)

-   Library
-   Based on top down algoritm
-   Underlying theory is simple
-   In principle unlimted look-ahead
-   User definable abstractions
-   Fast as long as certain constructions are not used (like a lot of look ahead)

A combinator is a self contained function in lambda calculus. The formal system that is the basis of Haskell and other functional programming languages. So parser combinators are a set of small library functions that can be used to construct parsers. The idea is that in context free langauges the context can't change the parse of the string. This allows you the write parser combinators for small problems which can then be combined to parse bigger problems. 


Both approaches place certain but different restrictions on the grammar that you can use.

## Handrolling your own parser

-   You can do whatever you want, but this is quite hard.


## Complexity 
![[Pasted image 20220314190559.png]]

If a tree is deep or long then the sentence tends to be more complex. 