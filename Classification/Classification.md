# Classification

Classification is when you get a data point that you have not seen before, and you have to assign it to a **class**. You do this based on some representation of the data point and evidence of how features relate to a class. 

## Types of classification relevant to CL
- Language identification 
- Author profiling 
- Spam filters 
- E-mail routing
- Topic detection
- Sentiment analysis → Is a text positive or negative 
- Fake news detection
- ...

## How do we do this (first attempt)?

### Rule systems 
A crude solution is rule based. This means a lot of if elseif else rules. This gives you fine-grained control on classification outcomes, and we always know **why** something happened. 

Rule based is **robust** because you can make rules for even very rare cases which would otherwise be hard to train for. It is also a good way to add **intuitions** and **expert domain knowledge** into a system. You also don't need large datasets.

But language is too complex for this and changes too much to do it like this. It is probably **expensive** to write. You have to get the domain knowledge and if it is [ambiguous](../Languages/Ambiguity.md) then you have to write a lot of rules. 

## Supervised learning
The opposite of rule based systems is supervised [learning](../Other/Learning.md). Here the idea is that you have a large set of data points where you already know the correct classification, and you try to build a model that can predict the points you already have. The idea is that the model will learn the rules itself. The hope is then that the model will also do well on new data this depends on bias and [overfitting](../Prediction/Overfitting.md). This is the most important. **We don't want to prove our self correct we want to make a generalizable model**. This removes the need to write rules but has many other problems.  

## Types of supervised learning classifiers 

### Discriminative classifiers
Discriminative classifiers learn which features best predict a certain class. 

VS 

### Generative classifiers
Generative classifiers learn a model of how the data are generated and could because of this also generate new data. Classification happens by choosing the class that most likely generated the data. It's like the reverse.

![Pasted image 20220216114704](../images/Pasted%20image%2020220216114704.webp)

### Linear classifiers
Linear classifiers can only draw a linear decision boundary. 

### Non-Linear classifiers
Non-Linear classifiers can draw a non-linear decision boundary. 

![Pasted image 20220216114812](../images/Pasted%20image%2020220216114812.webp)

----




