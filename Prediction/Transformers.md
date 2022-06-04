# Transformers 

Transformers solve the problems with RNN.

[Recurrent neural network (RNN)](Recurrent%20neural%20network%20(RNN).md) seem to be useful any application in [Natural Language](../Languages/Natural%20languages.md) Processing (NLP). However they suffer from the.  

Transformers get rid of [recurrence](Recurrence.md) while still dropping the [Markov assumption](Markov%20assumption.md). This is done by introducing a **self attention layer**. This layer maps an input sequence $(x_{1}, x_{2}, ..., x_{n})$ to an output sequence ($y_1$, $y_2$, ... $y_n$). These sequences could be anything but this course focusses on sequences of [words](../Data/Words.md) which are [sentences](../Data/Sentences.md). These sequences can be any arbitrary length without compromises. How does the attention layer do this?

## Self attention layer
The self attention layer **compares** an element (word) to a collection of other elements (words) of the context (including the word itself).

### Example
So if you have the sentence. *He is biting the apple*. We then need [embeddings](../Semantic-Similarity/Embeddings.md) for each word like so:

| He      | is      | biting | the   | apple |
| ------- | ------- | ------ | ----- | ----- |
| $\mathbf{x}_{1}$ | $\mathbf{x}_{2}$ | $\mathbf{x}_3$  | $\mathbf{x}_4$ | $\mathbf{x}_5$ |

and lets say the target element is apple then $x_{5}$ is compared to $\mathbf{x}_{1},~\mathbf{x}_{2},~\mathbf{x}_{3},~\mathbf{x}_{4},~\mathbf{x}_{5}$. Each comparison is going to give a score which you call alpha. So the comparison give us $$a_{1.5},~a_{2.5},~a_{3},~a_{1},~a_{5.5}$$
So the first score of $a_{1.5}$ is expressed as $a_{1.5} = \text{score}(\mathbf{x}_{1}, \mathbf{x}_{5})$. **We want each score to tell how relevance the compared word is to predict the target word**. You can imagine apple being left out of the sentence and we want to predict apple in that location. So the scores tell us the relevance of each compared word to predict the target word. This is normally computed with the scaled dot product. Then to get an output of these comparison scores you take the weighted sum of the (normalized) scores. This means taking all the alphas and multiplying with their representations (the $\mathbf{x}$-es) and then taking the sum. So that looks like this: $$y_{5} = \text{sum}(a_{1.5}\mathbf{x}_1,~a_{2.5}\mathbf{x}_{2},~a_{3}\mathbf{x}_{3},~a_{1}\mathbf{x}_{4},~a_{5.5}\mathbf{x}_{5})$$
The alphas are giving us weights which indicate how much we should consider each of the items in the sequence (in this case to predict the word at position 5). Or basically how much attention to give each item in the sequence. So $y$ is the weighted output. 

Then you compute the weighted output for all the target words to get $y_{1},~y_{2},~y_{3},~y_{4},~y_{5}$. 


### Self attention thermology
In the example above each word can play 3 roles. These are given more specific names to which allows us to be more specific. 

So each item in the sequence can be:
- A **query** (q), when it is compared to other items in the sequence. 
- A **key** (k), when it is part of the sequence to compare with. 
	- So the scores are written as $a_{i,j} = \text{score}(\mathbf{k}_{i},\mathbf{q}_{j})$
- A **value** (v) when used to compute the output:
	- $y_{5} = sum(a_{1.5}\mathbf{v_1},~a_{2.5}\mathbf{v_{2}},~a_{3}\mathbf{v_{3}},~a_{1}\mathbf{v_{4}},~a_{5.5}\mathbf{v_{5}})$

In the example $x_{5}$ plays the query role.  $x_{1}$ , $x_{2}$ , $x_3$  , $x_4$  , $x_5$ all play the key role and  $x_{1}$ , $x_{2}$ , $x_3$  , $x_4$  , $x_5$ play the value role. 

As you can see each word can play multiple roles. **The key to self attention is to learn separate weights for each role** This way get separate weights for each role. Then if you want to use an input as a certain role you can just multiply the input with the correct weights. More concrete each input $x_i$ is transformed into its role by multiplying the [embeddings](../Semantic-Similarity/Embeddings.md) with the corresponding weights. Like this:

- $q_{i}=W^Q\mathbf{x}_1$
- $k_{i}=W^K\mathbf{x}_1$
- $v_{i}=W^V\mathbf{x}_1$

These matrixes are obtained trough training. These matrixes give very fine grained information about each item of the sequence (word in the sentence(s)). In practice the representations of the words are different depending on the role the word is playing. 

So this means there are a lot of weights to learn. However it is more efficient than recurrence as: 
- We get rid of the [Vanishing gradient problem](Vanishing%20gradient%20problem.md) 
- All the computations for each score are independent. This allows for large **parallelization**.

These matrixes are called the attention I think. 

## Multi head attention 
You can vary the score function. Different ways of scoring might make more sense for different tasks depending on whether you focus on syntax, semantics, discourse. For all these tasks you can compute different matrixes or attentions for each word when they play a certain role. You can even have attentions for when you want an attention for when both syntax and discourse are important. So each type of relation has its own weights which is its own attention. With this the model size increases but it is not so bad because you can [learn](../Other/Learning.md) the weights in parallel. 

Each set of self-attention layers is called a *head*. So it is called multi head attention because you use multiple types of attention together which is multiple heads.

## Losing word order
So for some reason using attention is good... but it is not clear how or why. 

Anyways getting rid of recurrence seems to solve the vanishing gradients problem by training a matrix for each value in a sequence for different goals. Then if you want to do something with the value you use the attention matrix to get an embedding which is good for that goal? 

However, by removing recurrence you lose the positional information. The transformer architecture doesn't take the order into account anymore. So even though a transformer can deal with sequences of any length which means it doesn't need the [Markov assumption](Markov%20assumption.md). What the model gets is more a bag of words then a sequence. This means that if you do the above example of He is biting the ?? and instead do Is he biting the ?? you would still get apple both times. The exact same output. So by dropping recurrence word order information is lost. For this example it doesn't matter because apple is still right but if you would give a random order of the sentence you would still get apple. This is a problem because the word order of most languages is quite predictable or quite constraint.

So you get position information back?  You just encode the position of the item in the sequence as a continues value that preserves order the information. So basically you **add a feature to the input which encodes the position**. Often this is done with the sine or cosine functions. 

## Applications 
Using the architecture outlined above the most powerfull NLP models in the world have been created. Some of the most popular ones are:
- BERT (Bidirectional Encoder Representations from Transformers) by Google
	- and variants variants like RoBERTam XLNet (bigger) and DistilBERT (smaller)
- GPT (Generative Pre-trained Transformer) by OpenAI (microsoft) 
	- GTP-1 to GTP-3 
	- These are the most popular in the world right now

# Philosophical questions 
These models caused a transformer revolution because they perform so well. This sparks debates about what these models can and can't do, and how close they are to achieve human-like linguistic abilities and even general Artificial Intelligence. 

Open questions:
- How much do transformers really learn about natural language or do they just do well because they are trained on a lot of data?
	- Do transformers learn the same syntactic relations defined in linguistics 
- Do Transformers emulate human linguistic abilities 
	- Do transformers process sentence in a similar way


## The paper
BERT especially has been studied a lot and this was covered in the last lecture. The study of the BERT model is informally refered to as BERTOLOGY.