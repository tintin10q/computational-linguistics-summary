# Decoding

Decoding is the task of turning something that is in code form into a non code form.   

In the case of this course decoding has to do with [[Hidden Markov Models]]. It is the task of **determining the sequence of hidden variables given a sequence of observed events.** 

The decoding task takes an estimated HMM $\lambda$(A, B, $\pi$) and a sequence of observations O as input to output the likeliest sequence of states Q to have generated O. 

## Formally
If we want to write this down formally we get: $\hat{t}_{1:n} =\text{argmax}_{t_{1:n}} p(t_{1:n}|W_{1:n})$.

So the apoximated tag sequence is the sequence of words with the highest posterior probabilty. If you actually calculate this with [[Bayes rule]] you get $\hat{t}_{1:n} =\text{argmax}_{t_{1:n}} p(t_{1:n}) \cdot p(W_{1:n})$. 
We plug in the formulas to estimage both terms under the [[Hidden Markov Models|Markov assumption and the output indepedence assumption]]. So for a whole sequence:

$$\hat{t}_{1:n} \approx \text{argmax}_{t_{1:n}} \prod^{n}_{i = 1} p(t_{1:n}) \cdot p(W_{1:n})p(w_{i}|t_{i})$$

You can also do this in log space to avoid overflowing. Here you can also see the output independence. The last p only looks at the i word with the i tag. 

## Transition and emission
The posterior is the product of the **transition probability** PoS tag n-grams to PoS tag and the **emission probability** from the PoS tag to word.

### Transition Probability
Transition probabitlites (A) captures the prior. This is how likely the tag is given the context. Comes from the A matrix stays with the tags and sort of enforces the Markov assumption in the model.

### Emission Probability 
The emission probability is the probability of the word given the word. This enforces the output independence. You only look at the current tag.