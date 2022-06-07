## Constituency

You can use [grammar](Grammar.md) rules to make constituents out of terminals. For instance if you have the terminals $\{0,1,2,3,4,5,6,7,8,9\}$ then you could define the constituent N. For instance defined as: 

N = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

The cool thing is that you can now include these constituencies to create more abstract things. For instance, what if we also have:

L = a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z 

Then now you could define the constituent POSTCODE as:

POSTCODE = NNNNLL

This way you can keep abstracting parts of language. 


## Coordination
Constituencies can be put behind each other without problems. You could have a grammar rule PP = POSTCODEPOSTCODE, and it would be fine. This is often used as a test of constituency. If two phrases can be coordinated without violating any rules, then they are constituents.


### Evaluation

Recall (correct in hypothesis over correct in gold standard), precision (correct in hypothesis over hypothesized) and f1 is used.

A constituent is labelled as correct if there is a constituent in the gold standard with the exact same starting point, end point and non-terminal symbol.  