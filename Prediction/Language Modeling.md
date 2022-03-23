# Language modeling
Can we build a model which automatically [learns](Other/Learning.md) which sequences are part of a [langauge](Languages.md) and which are not?  Yes we can. Language is sequence of things and is not random. What comes before affects what comes next. 

The model will try to [predict](Prediction.md) what comes next in the sequence of words. If the model is very wrong about what comes next then maybe it is not in the language. Humans do the same thing we always try to predict what comes next when others speak. You can say that the higher the score of a text the more fluent it is.

## Probabilities 
A language model is first trained on a bunch of correct text of a language. This gives the model a **large probability distribution of sequences in the language**. When the model recieves a new (unfinished sequence) it can assign a probability to sequences of symbols that might come next in the sequence.  

It can also give a probability of how likely an entire sentence is to appear in a language. This way it might say that: "The sun rotates around the earth" is less likely than "The earth rotates around the sun".

## Uses of language models 

Language models are usually a means to an end, rarely the goal. They are usefull for:
- Scoreing sentences before choosing the best one
- Scoring machine generated language.
- Investigae language processing in humans to inform the developent of bots.
- Speech/handwriting recognition. Disambiguation, if you a piece of unclear text could be multiple things you could pick the one the language model says is more likely. 
- Spelling correction if more alternatives have the same [edit distance](Edit%20distance.md).
- Scoring machine translation models or translation options. 

## Generating language
If the model knows the probability distribution of a language then you could also give it an unfinished sequence of [symbols](Symbol.md) and the model could tell you which next sequence of symbols has the higest probability to appear next in the sequence when following the probability distibution (what we already know or what happened before). So language models can actually predict what is the most likely to come next. 

You could then take the sequence of symbols that was the most likely and add it to the sequence you had to further the sequence. Now after you have done this once you can ofcourse do another prediction on the new sequence and there you go now your generating language. Because language models can do this we call them **generative models**. 

### Always the same sentence
In a model as described above when we give the same sequence the model will always give the same results because it uses a probability distrobution. It will always give the sequence which is the most likely which is actually one sequence. This can also cause you to hit loops if you only consider the last x number of symbols in a sequence. 

## Evaluting language models 
How do you know whether a language model is good? In this case good is that the model encodes probabilities well and assigns high probability to real, correct sentences and low probabilites to wrong sentences. The best langauge models can mimic human performance. 

### Extrinsic evaluation
With extrinisc evaluation you evaluate how much impact a model has on a downstream task. For instance how many new custormers did we get to our translation software? 

 ### Intrinsic evalution
 With intrinsic evaluation you evaluate the model itself. If you see an improvement in the intrinsic evaluation you can say that you may expect an improvement of the downstream task, but you can not be sure. 
 
 So how do we do intrisic evaluation? You feed the model new data and check how well it predicts each token in the sentences and how well it scores sentence probabilities. 
 
 A good language model will **fit the new data well**. This means it will usually predict the correct word type or assign a high probabilitiy to the sequences in the new data. This type of evualtion is called [perplexity](perplexity.md). 
 
 # Bi-directional models 
 
 So far this described a model which looks at what came before so on the left. You can also look it what comes at the right. When you start in the middle of the text. 