## Constituency

You can use [Grammar](Grammar.md) rules to make constiuencts out of terminals. For instance if you have the terminals {0,1,2,3,4,5,6,7,8,9} then you could define the constiguent N. For instance defined as: 

N  = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

The cool thing is that you can now include these contituences to create more abstract things. For instance what if we also have:

L = a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z 

Then now you could define POSTCODE as:

POSTCODE = NNNNLL

This way you can keep abscracting parts of language. 


## Coordination
Constiuences can be put behind eachother without problems. You could have a grammar rule PP = POSTCODEPOSTCODE and it would be fine. This is often used as a test of constiunecy. If two phraes can be coordinated without violating any rules, then they are consituents