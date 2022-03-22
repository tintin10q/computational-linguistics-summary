# Finite State Automate

Finite state atomata is to a network with finate states. 

If every state has a transition for each possible input than it is **total**.

They are deterministic when each state has only one path for each state.

![Pasted image 20211212163706](images/Pasted%20image%2020211212163706.webp)

We can express this in a tuple of 5 things.

(X, Q, d, S, F)

- X is an input alphabeth 
- Q is a set of states
- d is a transition function of type Q -> X -> Q
- a start state S $\in$ Q
- A set of final states $F \subset Q$

Now that we have this general we can just make one function to run the atomata!

You can also have multiple start points or multiple connections for the same input these things cause nondetermism. So you have deterministic and non deterministic state machine.   You can resolve this non determinsm by going down all the path. You could then follow the shortest path or something. You can always transform the NFA into one that does have a single start state.  

This way you can parse. If there is atleast one path then you can parse the world.

Double circles are other finate states. 


We call non deterministic finate atomota NFA.
We call deterministic finate atomata DFA.

These are actually equavelant. We can express every DFA as a NFA and otherwise. The idea is to make them as NFA and then compile them to DFA so you can run them without worry.  

![Pasted image 20211212165403](Pasted%20image%2020211212165403.webp)
![Pasted image 20211212165450](Pasted%20image%2020211212165450.webp)
Example:
![Pasted image 20211212165625](Pasted%20image%2020211212165625.webp)

The empty set is like to stop state. 

You can actually simplfy it to:
![Pasted image 20211212165811](Pasted%20image%2020211212165811.webp)

So this means that you can use the alogritm to turn a NFA into a DFA but this won't give you the only one or the smallest one. A better way is to do a simulation this gives you the best. 

Another way to do this is that you add a transition state that always goes. So this way you create new states because you can have these lambda transitions.  This is great because then you can have one start state for your NFA. 

NFA are closed under:
- union
- concatentation
- intersection
- star closure
- complement

Being closed under an operation means that if we take languages defined by NFA we can build another NFA which recognizes the language defined by applying the operation.

# Lookahead 
Sometimes you have finiate state machines that only go forward. In this case you need to have lookahead to decide what you have to choose. This slows everything down. But you can paralize this. But really this is more of a problem with pushdown automata. You can always define a finite state machine that does not need lookahead. Calculating lookahead is not really that simple. 
