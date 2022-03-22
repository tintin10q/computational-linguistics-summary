# Grammers
A grammer is a language for defining [languages](Languages.md).  If you write rules for a language then these rules are also called the grammar. The individual rules you write are called a production. Grammars define the structure of the [sentences](../Data/Sentences.md) in the language.

A grammar consits of multiple productions. Productions can be seen as rewrite rules. If the left side matches you can replace it with the other side. Also if you already have something that is part of the language you can make more things in the language.

Formally you have:
- N - A finite set of non terminals (states)
- $\sum\limits$ - A finite set terminals, disjoint from N 
- P - A finite set of production rules 
- $S \in N$ A distinguished start non terminal state from N. 

The symbol from the alphabeth are also called **terminals**. $\epsilon$ is also a terminal. Rember epsilon is the empty input.

The grammer makes use of auxiliary symbol which is called **nonterminals**. These are not part of the alphabet and hence cannot be part of the final word/sentence. The non terminals are supposed to be replaced with terminals when your parsing. This is called a rewrite rule. Non terminals can be of two types. 

- Pre-terminals like PrN and V are [Parts of Speech](Parts%20of%20Speech.md). Or atomic non-terminals. The production rules indicate which sequences they can generate.
- [Constituents](Constituency.md) (NP and VP) are abstract units which absolve complex syntactic functions. 

![Pasted image 20220314185901](../images/Pasted%20image%2020220314185901.webp)


The grammer rules are kind of defined like inductive rules.

The idea is that you repalce the non terminals with a parse tree or an abstract syntax tree. This abstract syntax you can then evaluate. 


The start state is nice because if you can get from an input to the start state by following the rewrite rules then you know your input is in the language. The start state represents to most abstract place in your language. 

We usually read the rules left to right but you can always go back if you want. 

## Writing down the rules
There are diffent ways to write downs the rules. There are also different formats. Once such format is the  [Chomsky Normal Form](Chomsky%20Normal%20Form.md).

Also remember that the rules in a grammar for a langauage HAS to be finite. Otherwise you would also have to consider another rule. 

You can use non terminals on both sides. This allows for good abstraction. This is done using [Constituency](Constituency.md).


## Example

If you have this grammar:

- A -> aAa
- A -> bAb
- A -> $\epsilon$

Then this word is in the language: abaaba. Because you can parse it like this:
1. abaaba
2. abAba
3. aAa
4. A

Usually the non terminals are capatilized. 




## Examples

## Palendrone example

![Pasted image 20211127131012](../images/Pasted%20image%2020211127131012.webp)

The idea is that it sort of does not matter what P is here. 

When still talking about palendrome. 

![Pasted image 20211127130856](../images/Pasted%20image%2020211127130856.webp)

S is a start. 

So you can define a grammer like this:

![Pasted image 20211127131455](../images/Pasted%20image%2020211127131455.webp)

This is an example of a grammer which only allows strings of a and b.

This is a special grammer where there is only non terminal on the left. This is a **Context Free** grammer. If there are multiple non terminal characters than you have a context sensitive grammer.

In this course we are only looking at context free languages. There are a lot of languages that we can't describe with this. There are also languages that you could never describe with a grammer. There are sadly more languages that you can't describe with grammer. Most programming languages are context free. 

You can also have more grammers for the same language. 

![Pasted image 20211127131955](../images/Pasted%20image%2020211127131955.webp)

This makes sense because the cpu also looked very different for everyone. 

## More exampels with digit
![Pasted image 20211127132201](../images/Pasted%20image%2020211127132201.webp)

Here there is one non terminal Dig that can be rewritten to each digit. 

We can also now define Digs wich is atleast two digits. With this we can define any sequence of numbers. 

![Pasted image 20211127132647](../images/Pasted%20image%2020211127132647.webp)

So we can do Digs -> Dig* to say Digs is 0 or more Dig

What about numbers that don't start with 0?

We can make Dig-0 -> 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
Then with that we can define a sequence of natural numbers like:
Nat -> 0 | Dig-0 | Digs

Then we can define integers by defining a sign:
Sign -> +|-
Int -> Sign Nat | Nat 

This means a Int is a natural number with an optional sign. There is a short hand for this like:

Int -> Sign ? Nat 

This means the sign can be there but does not have to be. 

## Letters
Letters are a lot like digits but we just have more things. 

SLetter -> a|b|....|z
CLetter -> A|B|...|Z

This also means that you before you write down the grammer you have to specify what you can use as non teminal. 

Letter -> SLetter | CLetter

Now we can set up something like an identifier. Like a var name. 

Identifier -> Letter | AphaNum* 
AlphaNum -> Letter | Dig

You can easily exstend this with _ or othe things you want to be in identifiers. Honestly I really like this so far!

The reason we do a letter first is that this way the compiler does not get confused that something is actually a number like a Nat. 

# Fragment of C#

With this we can actually define the whole of C# woah.

Var -> Identifier
Op -> Sign 
Stat -> Var = Expr; 
	| if (Expr) Stat else Stat
	| While (Expr) Stat
Expr -> Integer
	| Var
	| Expr Op Expr


# How in haskell?

Represent the non terminals as data types. 

The concrete syntax is the syntax like above the abstract is how you would define it in haskell with data types. 

![Pasted image 20211127142739](../images/Pasted%20image%2020211127142739.webp)

You can also take the tree and bring it back to the string. 

![Pasted image 20211127142855](../images/Pasted%20image%2020211127142855.webp)