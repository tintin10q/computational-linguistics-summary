# Ambiguity 
When something is ambiguous, it means that it can mean multiple things. Additionally, it is also not really clear what the correct meaning should be.

Often humans can deal with things like ambiguous sentences by looking at the context of the sentence or the speaker's face expression and body language but dealing with ambiguity is really hard for computers. Rule based systems can not deal well with ambiguity.  

When something is unambiguous, the meaning is clear and can only mean one thing.

## Structural ambiguity

Structural ambiguity is a kind of ambiguities which occurs when a phrase, clause or sentence can be given two or more different interpretations as a result of the arrangement of words (the structure).

### Example 

An example of structural ambiguity can be seen in this sentence: `I shot an elephant in my pajamas`  

Were you in your pyjamas when you shot the elephant, or did you shoot the elephant into your pyjamas? This ambiguity can only be solved by looking at the meaning. But that is hard for computers, and so you can also try to solve it by looking at what types of **structures** appear more often in a language. Typically the propositional phrase (the in my pyjamas part) modifies the subject. So if you know that bias, then you can try to solve structural ambiguity using a language models based on structures. 

## Coordination Ambiguity
An example of this is `Tasty sandwiches and flowers make my grandma happy`. Do we mean tasty sandwiches and tasty flowers? Or only tasty sandwiches. Both are valid. But we probably don't eat flowers, so just tasty sandwiches. This can be resolved with [Lesk similarity](../Data/Thesaurus.md) or by trying to [represent words as vectors](../Semantic-Similarity/Vector%20semantics.md).

# Resolution
We can show that there is ambiguity with the [CKY](CKY.md) algorithm. However, when we know that a sentence is ambiguous, how do we pick one? We can look at the structure to assign probabilities to different options and pick the one with the highest one. One step deeper, we can assign a probability to every production rule in the [Grammar](Grammar.md).  Then with that you can assign a probability to every possible right-hand side of a production rule [given](../Classification/Native%20baiyes/Bayes%20rule.md) the left-hand side. This allows you to calculate the likelihood of a parse tree given the grammar.  

When we assign probabilities to rules in a [context free grammar](Context%20free%20grammars.md), it becomes a [probabilistic context free grammar](Probabilistic%20Context%20Free%20Grammar.md) (PCFG). So a PCFG is a CFG whose rules are augmented with probabilities. 

