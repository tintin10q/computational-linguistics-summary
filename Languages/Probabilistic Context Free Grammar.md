# Probabilistic Context Free Grammar 

A Probabilistic Context Free Grammar is a [Context free grammar](Context%20free%20grammars.md) which also has probabilities assigned to every production rule which indicates how likely the right hand side (RHS) of the rule is given the left hand side (LHS).  So each rule looks like this:

$$X \rightarrow YZ[p(YZ|X)]$$ or another example:
$$X \rightarrow y[p(y|X)]$$
So you can see the second part (p(y|X)) means the chance of y given X. Or the chance of YZ given X. 



## Getting the probability of a parse tree
With a PCFG it is possible to calculate the probability of a whole [parse tree](Parse%20Tree.md). So how is this done? With this formula: $$P(T, s) = \prod^{|T|}_{i=1}{p(RHS_i|LHS_i)}$$
> T = the parse tree 
> s = a sentence 
> p(T,s) = the joint probability of the parse and the sentence
> $\prod$ = multiply together just like $\sum\limits$

The left hand side is asking what is the probability of this parse tree on this sentence?

Then you just multiply the probability of each rule to expand the non-terminals in the parse tree T. Here we make the assumption that one grammar rule appearing is independent of another grammar rule appearing. This allows us the multiply the probabilities of the grammar rules together. So you basically go trough the parse tree and at every step you multiply the probabilities of all the production rules you used to parse the sentence.

With an [ambiguous](Ambiguity.md) sentence there will be more then one parse tree possible. So in that case you just use the above formula to calculate the probability of each possible parse tree and you pick the one with the highest probability. This the maximum probability tree is then called $\hat{T}$. 



Doing the multiply for every parse tree is captured in the |T| above the $\prod$ here you basically say for all possible parse trees that we can derive from this sentence multiply this.  


We call the parse trees of a sentence the parse trees which **yield** s.

----

Calculating the probability this way actually gives you two things. It gives you the probability of the parse tree occurring on this sentence: $p(T,s)$ but it also gives you the probability of the parse tree in general in this PCFG. So why is this?

Basically what we did above is this: $$P(T,s) = p(s|T_{i})p(T_{i})$$
This is just [Bayes rule](../Classification/Native%20baiyes/Bayes%20rule.md). But in this specific case of parse threes we can actually reduce this to $$p(T_{i},s) = p(T_i)$$ because $p(s|T_i)$ is always 1 because we only consider parse trees which can actually parse the sentence. So the probability of the parse tree given the sentence is always 100%. Because of this we can say that we can also get the probability of the parse tree in general. Now this allows us to go backwards with this because an equality goes both ways. We can now say that to get the probability of a parse tree and sentence together we only have to calculate the probability of the parse tree. 

So once you have seen a parse tree before for another sentence you know the probability of it already.

We can use a dynamic programming solution to get all the possible parse trees. 

So we can just multiply production rules. 

---- 

In peoples heads it seems to work similar that they build up parse trees out of constituents of the grammer based on probabilities. When a parse tree then is weird like. The cabin behind the horse race fell. Apparently fell is  not expected there. This confuses humans and requires more processing power. AI which generates language should keep this cost in mind. 


## How to make PCFG?
To do this you need to traverse a parse tree which requires tree banks. 

You can use also have probabilistic [CKY](CKY.md). The changes are that you represent a sentence using a tensor t of the shape n+1 x n+1 x V where n is the length of the sentence and V is the size of the non-terminals. Each cell t[i,j,A] contains the probability of type A to span positions from i to j. So the idea is to add another dimension. There is also this rule change:

![CKY modification](../images/Pasted%20image%2020220526203433.png)

So whenever you update table[i,j,A] because you found a parse from i to j with a higher probability you need to record where you were and were coming from in back[i,j,A] so that if and when you find the state  S in the final cell, you can recompute the best parse by going through the best sub parses. 

## Deriving the probabilities 
You derive the probabilities for the productions by using [Treebanks](../Data/Treebank.md). The idea is to count how many times each expansion of a non-terminal occurs  and normalize by the occurrence of the non terminal. So you basically count how often a certain non terminal goes to non terminal and terminal out of all the options and divide by all the options. Just like the counting [N-grams](N-grams.md) but now with by looking at each LHS going to which RHS.

## Problems of PCFGs 
Two assumptions have to be made.

- **Independence** of productions occurring. 
	- Of course it is not independent. But this kind of a shortcoming of the whole context free grammar and trying to use it for natural languages as the grammar of a natural language is not context free. So independent assumption is caused by the context freedom assumption.  
	- This is needed to be able to calculate easily. 
- (P)CFG **don't know about lexical items** which results into poor solutions to structural ambiguities. Humans seem to have no problems with this and this often solves ambiguity. So it ignores rules which are based on specific lexical items and rules. But of course the meaning has large effects on the probabilities. 
	- For instance The guy looked at the girl with the telescope AND the guy waved at the man with the telescope. Because of the meaning it is clear to humans what is what but the computer won't know because it doesn't know about the meaning. It will always prefer one of them. So either the guy is holding the telescope or the girl. The model will always choose the same and sometimes will be wrong. 


### To try to solve the independence: 

Another problem with the current setup of PCFG is that we never change the probability of a production. This means that if you always take the highest probability that you will also be garandeert to be wrong in the other cases. At least you will be right most of the cases. 

One solution to this is making more productions which are more finely tuned for different types of grammar productions. So you have one where the object is at the start and one were the verb is at the start for instance. This gives you separate distributions. However this requires very fine tuned annotations which don't really exist.  

However you can do **parent annotations** were you annotate text by the parent terminal it came from.  You can also do this for lexical categories which I think makes it more clear. So you can look how often cat was RHS of Noun and how often it was RHS of verb. Then you can assign different productions to each of those so you have cat_verb and cat_noun. However this leads to overfitting because if you split too much the results are not generalizable so you have to pick the right granularity for splits of non terminals and pre terminals or use algorithms that do this for you like split and merge but its not covered.

### To try to solve the no lexical:
You can also try to make productions which also involve the lexical annotations. But this becomes infeasible fast and you overfit fast. 


There are apparently solutions but they are more advanced. 


In order to deal with sentences and complex grammar we have to make an assumption to be able to compute it but this also means we wont get a perfect model because we made the assumptions. 