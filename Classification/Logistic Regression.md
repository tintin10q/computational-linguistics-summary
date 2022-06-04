# Logistic Regression 

Logistic regression gives you the probability of a discrete outcome. You can know how sure the model is of predicting something. 

In the case of computational linguistics, we classify our surface level items, let's say words, as discrete units. We can use logistic regression to uncover the probability of a word instead of just [counting words](../Semantic-Similarity/Co-occurrence.md). 

Logistic regression looks like this: $$z = \mathbf{x} \cdot \mathbf{w} + b$$
- $\mathbf{x}$ is the feature representation of one input data point. For instance, a word as an [embedding](Embeddings.md) or a [connotations](Connotations.md) vector.
- $\mathbf{w}$ is a vector of weights assigned to each feature depending on the importance of each feature.
- $b$ is the bias term. This is an offset you start off with. The bais is a scaler you add to all the items of a weight vector. 
- $z$ is the result. The weighted sum of the evidence for a certain class. To get z you take the sum of the resulting vector you get by doing $\mathbf{x} \cdot \mathbf{w} + b$ to get a scaler. 

Logistic regression is a linear [classification](../Classification.md) method. It is also a **discriminative classifier**. This means it doesn't make use of likelihood terms but attempts to directly compute the [posterior](../Classification/Native%20baiyes/Bayes%20rule.md), i.e. $p(c|d)$ No knowledge of how to generate documents of a class is required. 

Logistic regression is also a **probabilistic classifier**. Rather than providing the best guess as the output, a probabilistic classifier gives the probability that the answer is a certain answer. This is great because it keeps options open and  provides more information than just one answer as it could be interesting that the answer is 30 % to be class one and 28 % class 2 while the classes 3-100 are divided over the other 32%. Sometimes, however, there are too many classes to keep the probabilities for every class. In that case, you have to prune the lower probabilities. 

![Probabilistic classifier](../images/Pasted%20image%2020220603190300.png)

To get make a logistic regression, we need 4 components:

## Feature representation 
A **feature representation**: a vector of numeric or symbolic features which encodes each input item. 

## Classification function 
A **classification function** computes the probability of the class given the input. This function you apply after you have calculated $z$. Remember, $z$ was the sum of the vector you get by multiplying the feature vector with the weights vector. This sum can be any value, and we want to bring it to a certain range because we want to interpret it as a probability. We are sort of [normaling](../Data/Normalization.md) the outputs. A good choice is the sigmoid (σ) function: $$y = \sigma(z)=\frac{1}{1+e^{-z}}$$
After applying the classification function (in this case $\sigma$) we want to be able to interpret the output as probabilities. To this end, we need to make sure that the sum of all the outputs of $\sigma$ for every class is 1. For binary problems you can simply do you can do $p(y=1) = \sigma(z)$ and then for the other class you can do $p(y=0) = 1 - p(y=1)$. So you just say the probability of the second class is the probability that it is not the first class.  
Now the probabilities for all classes sum up to one, and we can interpret the output as the probability of a certain class given the input. That is what we want. As the probability of one answer being the correct one is 100%.

### Multi class problems 
For multi class problems like the one below, making the output probabilistic is harder. 

![Multiclass probem](../images/Pasted%20image%2020220603192841.png)

You make probabilistic by using the softmax function with gives you the probability that your output is a certain class given the input. 

This works by estimating different weights and biases for every class rather than a single vector and then you divide every single vector by the sum of all the vectors. When doing this the activation formula becomes like this:  $$p(y=c|\mathbf{x}) = \frac{e^{\mathbf{w}_{c} \cdot \mathbf{x} + b_c}}{\sum\limits^{K}_{k~=~1}e^{\mathbf{w}_{k}~\cdot~x+b_{k}}}$$
This might look daunting, but it becomes more clear if we call it the softmax function and replace with the part where you multiply in input vector with the weights vector + the bias with z. 


$$softmax(z_{i}) = \frac{e^{z_{i}}}{\sum\limits^{K}_{k~=~1}e^{z_{k}}} 1\leq i \geq K$$
The idea is to divide the classification function result of one class ($e^z$) by the sum of all the results, which is just calculating a probability. Doing this will always give you a result between 0 and 1. So you get this:

![From sigmoid to probability](../images/Pasted%20image%2020220603200100.png)

### Graphical representation
So above, you can see that you multiply the feature vector with the weights vector to get the resulting new vector. Then you take the sum of this vector, and you add the bias. Then you apply the **classification function** to bring the outputs to a certain range to be able to then turn the output of that into a probability.

![Logistic](../images/Pasted%20image%2020220603184638.png)

## Objective function
An **objective function** measures how close a model is getting to learning what it is supposed to [learn](../Other/Learning.md) i.e. the loss, error or cost, these are all the same. So you give this function what was predicted and the right answer, and the objective function will give a score which indicates how wrong the model is. You want to minimise this score. The higher the error score, the worse the model. The lower the error score, the better the model is at predicting the data (for which you know the answers).  

Multiple loss functions exist like Mean squared error (MSE) or cross entropy etc. For these functions to work, you need to know what a good result is or what the right answer is. 

For the problem of finding word embeddings, we will use cross entropy. 

### Cross entropy 
The cross entropy score is also known as **negative log likelihood**.  The cross entropy score is the lowest (no error) when the correct class has a 100\% prediction, or basically  when $\sigma(z) = 1$ for the correct class. Then if we want to loss of the whole data set, the idea is to calculate the average cross entropy for each item to obtain the loss for the whole dataset. You can interpret the resulting cross entropy number as the probability of predicting the reality given an input. 

![Cross entropy in practice with a binairy problem](../images/Pasted%20image%2020220603192054.png)

## Optimizer 
An *optimizer* updates the model based on the errors in the decisions it makes. Basically, based on the output of the objective function, it updates the weights. For instance, with gradient descent or an evolutionary approach. For example, you could use the derivative of the loss function to go move the weights into the direction which lowers the loss. 

## Linear boundaries

A major downside of logistic regression that it can only make linear decision boundaries even though the problem could just be not linearly separable, for instance like the picture below: 

![Xor seperation](../images/Pasted%20image%2020220603200910.png)

To overcome this problem, you have to turn to [Feed forward neural networks (FFNN)](../Prediction/Feed%20forward%20neural%20networks%20(FFNN).md). Basically, connecting multiple logistic regression models together. It is called feed forward because the output of a lower layer only affect higher layers and do not feed back into the same layer or lower layers. 

