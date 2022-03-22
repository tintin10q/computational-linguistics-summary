# Clasification

Classification is when you get a datapoint that you have not seen before, and you have to assign it to a **class**. You do this based on some representation of the datapoint and evidence of how features relate to a class. 

## Types of classification relevant to CL
- Language identification 
- Author profiling 
- Spam filters 
- E-mail routing
- Topic detection
- Sentement analisis → Is a text positive or negative 
- Fake news detection
- ...

## How do we do this (first attempt)?

### Rule systems 
A crude solution is rule based. This means a lot of if elif else rules. This gives you fine grained control on classifaction outcomes, and we always know **why** something happened. 

Rule based is **robust** because you can make rules for even very rare cases which would otherwise be hard to train for. It is also a good way to add **intuitions** and **expert domain knolege** into a system. You also don't need large datasets.

But language is too complex for this and changes too much to do it like this. It is probably **expensive** to write. You have to get the domain knolege and if it is ambigous then you have to write a lot of rules.

## Supervised learning
The oposite of rule based systems is supervised [Learning](learning.md). Here the idea is that you have a large set of datapoints where you already know the correct classification, and you try to build a model that can predict the points you already have. The idea is that the model will learn the rules itself. The hope is then that the model will also do well on new data this depends on bias and [overfitting](Overfitting.md). This is the most important. **We don't want to prove ourself correct we want to make a generalizable model**. This removes the need to write rules but has many other problems.  

## Types of supervised learning classifiers 

### Discriminative clasifiers
Discriminative clasifiers learn which features best predict a certain class. 

VS 

### Generative clasifiers
Generative clasifiers learn a model of how the data are generated and could because of this also generate new data. Classification happens by choosing the class that most likely generated the data. It's like the reverse.

![Pasted image 20220216114704](Pasted%20image%2020220216114704.webp)

### Linear clasifiers
Linear clasifiers can only draw a linear decision boundary. 

### Non-Linear clasifiers
Non-Linear clasifiers can draw a non-linear decision boundary. 

![Pasted image 20220216114812](Pasted%20image%2020220216114812.webp)

----




