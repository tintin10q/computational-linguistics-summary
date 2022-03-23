# Viterbi Algorithm

How do you actually do [Decoding](Decoding.md) in practice? Because there is a large growth in the input. Given a sequence of 4 words and 45 tags there are $45^4$ possible sequences. So it's $O(Q^{|T|})$. This grows fast. This means we can not calculate all the sequences. 

The basic principle is to use recursion to compute the best path that could lead to a certain point given:
- The HMM
- The overvations up till the point you are
- The most probable state sequence to have generated the observations given the HMM.

The idea is just to compute the best path for the first part of the sequence. This is not so hard. But then **we know that the best path of the first part of the sequence is the best path up till that point**. This means that we don't have to recompute the probabilities for that part of the sequence. So if you have word 1 and 2 and 3. You can first compute the maximium likelyhood tag for 1, and then you can use that to calculate the maximum likelyhood for 2 without recomputing 1. 

This means we can start from 3. To calculate the best one we need 2, to calculate the best one we need 1.  Then we hit the base condition, so we calculate 1 and return it. Now that it returned we can use it to calcuate 2 and return that now that 2 returned we can calcualte 3. So basically you leave the work until you finished another problem. 

Using the recursion we get $O(Q^nT)$ where n is the n in [N-grams](../Languages/N-grams.md). This is also called the **order of the model**. So n = 2 is a bigram. So this makes it much better and you need a lot of data to get higher n. 

## In practice 
Create a matrix M with as many rows as there are states $q \in Q$ and as many collums as there are events $o \in T$ to be decoded (so that is the [sentence](../Data/Sentences.md) you want to tag + BoS and EoS). 

The value of each cell $M_{qo}$ is computed as follows: $p(t_{o}|t_{o-n:o-1})p(w_{o}|t_{o})$. So it's the prior multiplied by the likelyhood. This means that each cell contains the posterior probability of findinf each tag given the current word after having observed everything that came before. 

Each posterior in this matrix is depeneded on the **emission and the local transition** at each word $w_t$ with $t \in T$, compute the posteriiors considering  

## Example
For an example we need an already filled A and B matrix. $A_{ij}$ encodes the probability that the tag in column j occurs given that the tag in row i has. $B_{ik}$ encodes the probability that word k is observed given that tag i was. Also rows rum to 1. 

| A    | Det | Adj | Noun | Verb | EOS |
| ---- | --- | --- | ---- | ---- | --- |
| Det  | 0   | 0.2 | 0.8  | 0    | 0   | 
| Adj  | 0   | 0.3 | 0.6  | 0    | 0.1 |
| Noun | 0   | 0   | 0    | 0.5  | 0.5 |
| Verb | 0.5 | 0.1 | 0.2  | 0    | 0.2 |
| BOS  | 0.5 | 0.2 | 0.3  | 0    | 0   |

So for instance if you find and Adj you have a 0.3 chance to find another adjective and a 0.6 chance to find a noun. So given adj (on the side) you have a probability of 0.3 to find another adjective next and 0.6 to find a noun next. So given what's on the side you have probability to find something at the top. That is why collums sum to 1. 

The BOS vector at the bottom is $\pi$. The initial distrobution. Given BoS what is the most likely to follow.

| B    | dog | the | chases | cat | fat |
| ---- | --- | --- | ------ | --- | --- |
| Det  | 1   | 1   | 0      | 0   | 0   |
| Adj  | 0   | 0   | 0      | 0   | 0   |
| Noun | 0.5 | 0   | 0      | 0.4 | 0.1 |
| Verb | 0.1 | 0   | 0.8    | 0.1 | 0   |

The same here. Given a noun the chance is 0.5 that the word is dog. 

Now we can start the algoritm. 

First create the table. |Tag| rows by |words| collums + the BoS and EOS|. This table is called the trelis.

| Trelis | BoS | The | dog | chases | the | fat | cat | EOS |
| ------ | --- | --- | --- | ------ | --- | --- | --- | --- |
| Det    |     |     |     |        |     |     |     |     |
| Adj    |     |     |     |        |     |     |     |     |
| Noun   |     |     |     |        |     |     |     |     |
| Verb   |     |     |     |        |     |     |     |     |

First we can fill in the probabilities for the BoS row by filling in $\pi$ but you don't have Bos and Eos on the side.

| Trelis | BoS | The | dog | chases | the | fat | cat | EOS |
| ------ | --- | --- | --- | ------ | --- | --- | --- | --- |
| Det    | 0.5 |     |     |        |     |     |     |     |
| Adj    | 0.2 |     |     |        |     |     |     |     |
| Noun   | 0.3 |     |     |        |     |     |     |     |
| Verb   | 0   |     |     |        |     |     |     |     |

Now we want to put take the next word "the" and take the "the" collum from the B matrix. This is the emission probability.

| Trelis | BoS | The | dog | chases | the | fat | cat | EOS |
| ------ | --- | --- | --- | ------ | --- | --- | --- | --- |
| Det    | 0.5 | 1   |     |        |     |     |     |     |
| Adj    | 0.2 | 0   |     |        |     |     |     |     |
| Noun   | 0.3 | 0   |     |        |     |     |     |     |
| Verb   | 0   | 0   |     |        |     |     |     |     |

Now you want to multiply the collum we got (emmision probability) with the previous collum (the transition probability). This gives us:  

| Trelis | BoS | The | dog | chases | the | fat | cat | EOS |
| ------ | --- | --- | --- | ------ | --- | --- | --- | --- |
| Det    | 0.5 | 0.5 |     |        |     |     |     |     |
| Adj    | 0.2 | 0   |     |        |     |     |     |     |
| Noun   | 0.3 | 0   |     |        |     |     |     |     |
| Verb   | 0   | 0   |     |        |     |     |     |     |

Now this collum indicates the posterpior probability of the determiner given that the first token is "the". We have now decoded the sequence BoS The. Now we can move on to the next sequence. 

## Trelis 
The trelis represents the probability that the HMM is in state $q \in Q$ after seeing the previous events $o_{1}...o_{t}\in O$ and passing through the most probable sequence of states. The trelis is the name we give to this table we have been building. 

The value of each cell at sucesive states is computed by **multiplying the current transition and emission probabilities by the most probabable sequence** which could lead to that cell. This means we have to find the probable sequence. We do this by taking the max(transition probability * each collum of the A matrix - BOS).

![Pasted image 20220308194114](../images/Pasted%20image%2020220308194114.webp)

Now the max 0.4. Now we can multiply this with the emmision probability of the current word (dog) so we get: 0.4 * [0, 0, 0.5, 0.1] = [0, 0, 0.2, 0.04]. This becomes the new collum in the trelis. 

| Trelis | BoS | The | dog   | chases | the | fat | cat | EOS |
| ------ | --- | --- | ----- | ------ | --- | --- | --- | --- |
| Det    | 0.5 | 0.5 | 0     |        |     |     |     |     |
| Adj    | 0.2 | 0   | 0     |        |     |     |     |     |
| Noun   | 0.3 | 0   | 0.2   |        |     |     |     |     |
| Verb   | 0   | 0   | 0.004 |        |     |     |     |     |

We also want to mark which collum gave the max in the multiplication. In that case it was the first collumn. It is not garenteeth that this is always the highest value from the collum. It depends on A. So now we have the postterior probabilities for The dog. We don't have to recompute for dog. 

| Trelis | BoS | The | dog   | chases | the | fat | cat | EOS |
| ------ | --- | --- | ----- | ------ | --- | --- | --- | --- |
| Det    | 0.5 | **0.5** | 0     |        |     |     |     |     |
| Adj    | 0.2 | 0   | 0     |        |     |     |     |     |
| Noun   | 0.3 | 0   | 0.2   |        |     |     |     |     |
| Verb   | 0   | 0   | 0.004 |        |     |     |     |     |

So as you can see we need 3 pieces of information each time. 

- The posterior probability up to the previous state (the trellis) 
	- This makes it dynamic and saves time
- The transition probabilities from state $q_i$ to state $q_j$ 
	- This is the prior
- The emission probabilities for observation $o_j$ given state $q_j$ 
	- This the likelyhood

So let's continue:

![Pasted image 20220308195301](../images/Pasted%20image%2020220308195301.webp)

We found that 0.1 is the highest after multiplication. Then we multiply it with the emmision which is [0, 0, 0, 0.8] so 0.1 * [0, 0, 0, 0, 0.8] which becomes [0, 0, 0, 0.08]. Now we can fill that in, and we should mark the thirth collum.

| Trelis | BoS | The     | dog     | chases | the | fat | cat | EOS |
| ------ | --- | ------- | ------- | ------ | --- | --- | --- | --- |
| Det    | 0.5 | **0.5**     | 0       | 0      |     |     |     |     |
| Adj    | 0.2 | 0       | 0       | 0      |     |     |     |     |
| Noun   | 0.3 | 0       | **0.2**     | 0      |     |     |     |     |
| Verb   | 0   | 0       | 0.004   | 0.08   |     |     |     |     |

When we have filled the entire trelis you can make the sequence of tags by picking the on the side of the collum that has the marked number in each row. So, so far we get [Det, Noun] which is correct. 

Now we can repeat.

## More context
We can also look at the maximum of the previous transitions from each posterior more than 1 previous column.  So like n = 2 previous collums. However, it increases complexity but also brings sparcity. We don't want 0 transition sto hijack the computation. Because often a transition is not actually impossible just a really small chance.  To somewhat solve this we can use smoothing just like with [Markov models](Markov%20models.md). We can also use interpolation to guess the transition probability which is estimated by linearly interpolating using smaller n-grams. A guessed probability is better than no probability.

You can also use pseudo morphology -> words constst of smaller units which influence their PoS tag. We can look at this to add bias to the probability, or we could compute emission probabilities for part words (suffixes of different lenghts, down till single characters). Whenever you hit an unkown word, use the emmision probability for the suffixes instead. Something is better than nothing.

# Forward Algoritm 
This is similar to the Viterbi algorithm, but used to compute the liklihood of a sequence of observed events given a HMM. So it tries to find the likelyhood of a sequence appearing at all in the set of all possible sequences. We want to find the culmative probability at each step. 

All this does is replacing the max with the sum. You do this because you want to take into account the probability of all possible paths trough the hidden states, not find the likeliest path. Also you don't need backpointers because we don't try to find a tag. 