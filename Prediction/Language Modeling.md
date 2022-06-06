# Language modelling

Language modelling is the activity of creating a computer model which automatically [learns](../Other/Learning.md) one or more things about [language(s)](../Languages/Languages.md) and can then make [predictions](Prediction.md) for a certain task. 

Can we even do this? Yes we can. Language is a sequence of things, and that sequence is not random.  What comes before affects what comes next. This is the heuristic which is used to make good language models.  

## Probabilities 
A language model makes it predictions using a large probability matrix which encode probabilities about the language which are useful for the specific task which the language model is trying to solve.

To get these probabilities, a language model is first trained on a bunch of correct text of a language from a [corpus](../Data/Corpus.md). This gives the model a **large probability distribution of sequences in the language**. When the model receives a new (unfinished sequence) it can assign a probability to sequences of symbols that might come next in the sequence.  

There are multiple ways of deriving the probability matrix. Two ways discussed in the course are counting and neural networks. 

These probability distributions can also give a probability of how likely an entire sentence is to appear in a language. This way, the model might say that: “The sun rotates around the earth” is less likely than “The earth rotates around the sun”. Or, the sentence “A house is bigger than a person” is more likely than “A person is bigger than a house”.

## Uses of language models 

Language models are usually a means to an end, rarely the goal. They are useful for:

- Scoring sentences before choosing the best one
- Scoring machine generated language.
- Investigate language processing in humans to inform the development of bots.
- Speech/handwriting recognition. In disambiguation, if you have a piece of unclear text could be multiple things, you could pick the one the language model says is more likely. 
- Spelling correction if more alternatives have the same [edit distance](../Languages/Edit%20distance.md).
- Scoring machine translation models or translation options. 
- Which sequences are part of a [language](../Languages/Languages.md) and which are not?
- How should a certain sequence be continued?
- What words should be filled in to a blank spot. 
- Translation
- ....

## Generating language

If the model knows the probability distribution of a language, then you could give it an unfinished sequence of [symbols](../Data/Symbol.md) and the model can tell you which next sequence of symbols most likely to be next. The model does this by picking the continuation with the highest probability to appear next in the sequence when following the probability distribution (what we already know or what happened before). So language models can actually predict what is the most likely to come next. Instead of taking the most likely continuation, you can also sample according to the probability matrix. 

You could then take the sequence of symbols that was the most likely and add it to the sequence you had to further the sequence. Now after you have done this once you can of course do another prediction on the new sequence and there you go now you're generating language. Language models, which generate language, we call **generative models**. 

### Always the same sentence
In a model as described above when we give the same sequence and always take the most likely continuation, the model will always give the same results because the probability distribution is static. This can cause you to hit loops if you only consider the last x number of symbols in a sequence. 

## Evaluating language models 
How do you know whether a language model is good? In this case, good is that the model encodes probabilities well and assigns high probability to real, correct sentences and low probabilities to wrong sentences. The best language models can mimic human performance. 

### Extrinsic evaluation
With extrinsic evaluation, you evaluate how much impact a model has on a **downstream task**. For instance, how many new customers did we get after we bought that translation software? How large was the decrease in calls to our support center after we installed that chatbot. 

### Intrinsic evaluation

 With intrinsic evaluation, you evaluate the model itself, often according to some scoring metric from the literature. If you see an improvement in the intrinsic evaluation, you can say that you may expect an improvement of the downstream task, but you can not be sure. 
 
 So how do we do intrinsic evaluation? You feed the model new data and check how well it predicts each token in the sentences and how well it scores sentence probabilities. 
 
 A good language model will **fit the new data well**. This means it will usually predict the correct word type or assign a high probability to the sequences in the new data. This type of evaluation is called [perplexity](Perplexity.md). 

### Bidirectional models 
A bidirectional model is a language model which analysis text from both left to right and right to left. It could also mean analysing the text that came before what you try to predict and analysing what comes after what you try to predict given that is available.

## Techniques for NLP

Techniques for language modelling discussed include [Naïve Bayes](../Classification/Native%20baiyes/Naïve%20Bayes%20Classifier.md) (doesn't really take preceding words into account), [Markov chain models](Markov%20models.md) (we do take preceding words into account with n-grams), [Probabilistic Context Free Grammar](../Languages/Probabilistic%20Context%20Free%20Grammar.md) (using production rules to expand non terminals to terminals to generate language) and [Feed forward neural networks (FFNN)](Feed%20forward%20neural%20networks%20(FFNN).md) and [Recurrent neural network (RNN)](Recurrent%20neural%20network%20(RNN).md) and [Transformers](Transformers.md). 


![Language modeling progression](../images/Pasted%20image%2020220605011349.png)