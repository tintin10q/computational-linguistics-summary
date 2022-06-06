# Recurrent neural networks (RNN)
A recurrent neural network is a neural network which uses [recurrence](Recurrence.md) to take into account previous states. Instead of relying on n-grams and the [Markov assumption,](Prediction/Markov%20assumption.md) there is a **chain of recurrence**. The idea is to update some hidden layers in the neural network based on values of other (later) hidden layers. 

Instead of parsing the input into [N-grams](Languages/N-grams.md) and giving those as input, you select an input sequence and give the network one token of the sequence at a time. Each time, the hidden layers will update and update the previous layers based on the further layers. This causes previous words to influence the current prediction through recurrence. The words you feed into the model before you make the prediction are called the **chain of recurrence**. The chain of recurrence usually (almost) goes back to the beginning of a sequence, which is typically a sentence. We say almost because the most recent words affect the current state more than the words further away.

## Advantages of RNN
The chain of recurrence allows avoiding the [Markov assumption](Prediction/Markov%20assumption.md) as the hidden layers encodes information from all states (more about the more recent ones) that you give it. So with RNN you can use sequences of arbitrary length instead of a fixed n because the RNN don't rely on n-grams existing in the corpus. It works because you feed parts of the sequence and the model just updates and updates until you want to make a prediction. However, if you make the sequences too long, you run into the [vanishing gradient problem](Vanishing%20gradient%20problem.md).  

This is great because then you can also use different lengths of input once you have a model. 

You don't have to do smoothing with RNN because you can represent the input words to an RNN as [embeddings](Semantic-Similarity/Embeddings.md) which project words into a [continues space](Semantic-Similarity/Vector%20Space.md) where we can leverage [similarity](Semantic-Similarity/Similarity.md) relations to guess how our new n-gram should behave in case you did not see it yet. Also, because you input one token at the time, the chance of finding words you have not seen yet is smaller. So is it not RNN themselves which avoid the smoothing, but the combination of RNN and embeddings. 

## A new set of weights 
To make recurrent neural networks a new type of weights is needed. A RNN normally consists out of 3 sets of weights. 
- The weights which connect the input to the hidden layer (W) 
- The weights **between the previous hidden state and the current hidden state** (U).
- The weights between the current hidden state and the output (V) 

The W and V are the same as with [FFNN](Feed%20forward%20neural%20networks%20(FFNN).md) and the U weights are added. 

There is also a fourth set of weights **of the embedding layer (E)** which connects the input to the embedding layer, which are then connected to the hidden layer through the set of weights W. The embedding layer is optional but almost always added. 

The rest is the same as with FFNN with a loss function, gradient descent and back propagation. However, the back propagation is a bit different, it is back propagation through time. 

![RNN](images/RNN.png)

## Making predictions 
So the output (the production) depends on two things:
- The embeddings of the current input word 
- The hidden layer as influenced by the previous step(s) 

This is the [Bayes rule](Classification/Native%20baiyes/Bayes%20rule.md) intuition, where with the current evidence and the previous evidence you make up your mind about the future. 

This information is coming from the current input (embedding) and the hidden layer is summed to obtain a new hidden layer which is transformed using the [softmax](Feed%20forward%20neural%20networks%20(FFNN).md). This then gives you probabilities for different classes. This could either be a probability for each word in the language indicating how likely it is to be next or for instance a [Parts of Speech tag](Languages/Parts%20of%20Speech.md) or any other label.  These probabilities change every time you input another embedding (you say they change at every time step). When predicting words, you at some point stop giving input, and you take the class with the highest probability. Of course, if you sum these probabilities, you get 1.

When predicting tags or labels, you will need to have the correct label for training, as the loss function needs to know what the correct answer is. This requires annotation, which is expensive. With language prediction you don't need annotation because you can just use an existing text to have a correct answer. This kind of prediction can also be done with [ FFNN](Feed%20forward%20neural%20networks%20(FFNN).md) however they don't remember the context.

## Stacking layers.
We can stack as many recurrent hidden layers as we want (but the more, the slower the training). You can also stack the neural networks themselves, just like with [Logistic Regression](Classification/Logistic%20Regression.md). In this case, you could use the entire sequence of outputs from one RNN as the input to a next RNN or different type of neural network. The Neural networks are mostly **self-contained modules** which can be combined in an infinite number of ways, however you should motivate layer choices because the bigger the NN the more expensive running it gets. 

In essence stacking computes a slightly more abstract version of the input than the last version. This is especially useful if you have noisy data. We would like the network to learn how to use the abstract feature bundles from the input. The lower layers are tuned towards something closer to the signal, while the higher layers are tuned to more and more abstract features.  This is also how your brain does it, with vision and sound going through multiple layers. 

### Bidirectional 
RNN do not only go forward (left to right) but they can also go in the reverse. You can decide in which order you process the input sequence. You can go left to right or right to left. You could even have read middle out if you want. This will result in different dependencies. 

Nothing prevents us from having **two RNNs which read the input sequence in different directions and then combine their higher hidden layer** to encode a single representation of a sequence. This combines reading left to right and right to left, for instance, into a single representation.  There are many ways to combine the representation of hidden layers. For instance, concatenation or element wise sum/multiplication. RNN that do this called **bidirectional**.

## Back propagation through time 
A different back propagation is needed as to make a prediction we have to run the model multiple times. Normally with backpropagation it happens after you have just run the model once.

It works by in the forward pass, going through the whole sequence and keeping track of the loss. Only at the end of the input sequence do you start the backwards pass and **go all the way back, processing the sequence in reverse**. At every step, you compute the required error terms gradients (with derivatives) and save the error to compute the gradients at the next (which is the previous) step. 

So it sort of like a step up from normal back propagation because you have to include make an improvement while the model ran multiple times. 

## Vanishing gradient
One problem with RNN is the [vanishing gradient problem](Vanishing%20gradient%20problem.md). If the sequence which is processed by the model step for step is very long, the gradients in backpropagation through time are multiplied several times (as many times as words in the sequence) and may end up being zero. The smaller the gradients, the smaller the change in the weights. **If the gradients hit zero, the changes to the weights to stop**. 

There are variants of RNN like LSTMs and GRUs which modify the recurrent layers to handle the vanishing gradient by **forgetting** some information, which won't be carried on to the later input steps (and hence doesn't influence gradient computation). By forgetting, this information doesn't have to be carried to later input steps, and this reduces the vanishing gradient issue to some extent. 

There is another good further explanation found by Ethel of LSTM [here](https://colah.github.io/posts/2015-08-Understanding-LSTMs/).

## Applications of RNN

Apparently in 2017 bidirectional LSTM (with attention) were the state of the art for almost every task in NLP. They are still very much used, but now the state of the art is [transformers](Prediction/Transformers.md). 

### Probability of the sequence 
You can get the probability of the input sequence itself. You do this by making the model predict the next word for every token of the sequence you give to the model. Then you take the predicted probability for the class of the correct next token and store it, calculated with softmax. You know the correct next token because you have the sequence. Do this for the entire sequence, and then you multiply the probabilities or sum the logs to get the probability of the entire sentence under the trained language model. 

So the **product (or sum of log) of the probabilities of each correct continuation under the softmax** is the probability of the whole sequence under the trained language model. 

### Autoregressive 

When a model is autoregressive it means it can generate new language. 

This is done in the following way:

- Take the embedding of the beginning of sequence tag (BOS) as input to the RNN. Take the word with the highest softmax probability, or sample from the top x words. 
- Take the embedding of the generated word, run the network on it, and again take the word with the highest probability (or sample the top x) in the softmax. 
- Repeat till EOS (end of sequence symbol)

When doing this you **only need 1** beginning of sequence symbol and not multiple like with [Hidden Markov Models](Prediction/Hidden%20Markov%20Models.md). This is because the hidden layers will 'remember' that it has seen a beginning of sequence symbol. 


### Predicting Pos tags

Like said above, you can use RNN to predict labels. You can also use them for predicting [Parts of Speech](Languages/Parts%20of%20Speech.md) tags. However, the performance is not much better than with [Hidden Markov Models](Prediction/Hidden%20Markov%20Models.md).

### Named entity recogntion and labeleing
This task is about finding and appropriately labelling words which denote entities (countries, people, organizations .... ). So, for instance, you get the sentence "New York is a big city". The model should find out that New York is both a named entity and also the same named entity and also a city. 

### Structure prediction 
This task is about, given an input, producing the correct set of actions to achieve the desired output. Think of Alexa or Google assistants. RNN are useful for this because of the longer histories which can be used. 

### Sequence to label 
You can use RNNs to classify whole sequences as something. These models are called Seq2Label).  

To do this you run the model through a whole sequence and add the end **the hidden layer will encode a representation of the whole sequence** (more from the end). So like deriving an embedding for an entire sequence basically. You can then put simple [Logistic Regression](Classification/Logistic%20Regression.md) on top and train it to correctly classify these representations. The loss now refers to the class of the whole sequence. This is not a generative model, but a discriminative model. 

### Sequence to Sequence

Sequence to Sequence (seq2seq) is **a model that takes a sequence of items and outputs another sequence of items**.  Rather than emitting a label at the final step, you give out another sequence. 



You try to predict a sequence from another sequence without necessarily having a one to one mapping between units in both sequences. I think these are the most interesting problems, like translation or summarizing text. 

These types of models are usually made out of two connected subnetworks. The first **encodes the source** sequence (input) in a hidden state which yields an embedding. The second **[decodes](Decoding.md) the representation** from the hidden state into the target sequence. Training happens by jointly updating the weights of the encoder and the decoder in such a way that the decoded output resembles the target output as closely as possible. 

You might see this as a model taking in the label from a seq2label model and then predicting a sequence from that.

Nowadays, the underlying neural network architecture of these has changed, but the idea is still the same. 