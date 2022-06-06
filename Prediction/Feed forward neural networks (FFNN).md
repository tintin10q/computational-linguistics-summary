# Feed forward neural networks 

Feed forward neural networks (FFNN) can be used to overcome the linearity problem with [Logistic Regression](Logistic%20Regression.md). To achieve this we feed the output of one logistic regression multiply-the-weights-vector-with-the-input-vector-step as input into another logistic regression model. We can also just keep doing the multiply vector and weights a lot of times before we do the classification function and making it probabilistic steps. We can also multiply the input vector with multiple weight vectors only then apply a classification function to some of the cells of the result vector to create a new vector of a different size and keep going. It is quite flexible, to see the graphical representation below.  

So stacking logistic regressors will create non-linear classifiers which can learn **arbitrary decision boundaries** for linear classifier. This turns logistic regression into (feedforward) neural networks.

![Graphical representation of feed forward network](../images/Pasted%20image%2020220603203033.png)

So what you see above is taking the input vector and multiply with multiple weight vectors every time also adding a bias. Then you take the sum of these cells and pass it to a function. Typically, a non-linear function to add non-linearity. This then gives you a new vector (the gray dots). This is then called a **hidden layer** because you can not interpret it any more back to the input. It is a more abstract representation of the input. 

We then keep going, multiplying the hidden layer by another weights vector and adding a bias and on and on. However, we want to go to a scaler in the end so to do that you just take one sum from the vector you are at and apply the classification function (for instance sigmoid or softmax) to turn the output to a certain range and into a probability.  

## Matrix representation 

If you would actually make a computer do this it is useful to use matrixes to kind glue the weights vectors together and computers know how to deal with matrixes well and fast. You can visualize the above picture with matrixes like below:

![Feed forward visualized as matrix](../images/Pasted%20image%2020220603203248.png)

## Feed forward  
These types of networks are called feed forward because the output of a lower layer only affect higher layers and do not feed back into the same layer or lower layers. 

These types of networks also sometimes called Multi Layer Perceptrons (MLP) although perceptron's don't use non-linear [activation functions](Logistic%20Regression.md) while FFNN do.

There are also neural network architectures which are not feed forward. For instance, you can take the previous states of the model into account with [recurrence](Recurrence.md). When this happens, the neural network becomes a [recurrent neural network (RNN)](../Prediction/Recurrent%20neural%20network%20(RNN).md).  

## Fully connected 
MLP are typically fully connected (or dense). Each hidden unit computes the weighted sum over **all** the units in the previous layer. There is a direct connection for every pair of hidden units (or neurons) in each pair of adjacent layers (including the input and output layers). So basically in the drawing, there is a line from each circle of one layer to each other circle in the next layer.  If this is not the case, then a network is not fully connected.

## Hidden layers
There can be arbitrary many hidden layers even though one is enough to learn any kind of function (given infinite time, and resources). Stacking hidden layers may help learning. Hidden layers can also change the size of the vector, like seen in the graphical representations with the gray layer. 

## Back propagation
Adjusting the weights with FFNN is more complicated than with logistic regression.  Backpropagation is the algorithm used for this, but this course does not go into further detail about it. You can [read more here](http://neuralnetworksanddeeplearning.com/chap2.html).

The general idea is that you apply the forward pass where you generate the outputs. Then you calculate the loss with the objective function with the correct outputs vs reality. This requires labels. Then you do the **backwards** pass, where you take the error and compute all the derivatives at every layer. This will sort of show which weights caused the largest error, and then you adjust those more in the direction which will cause less error.

## Learning rate 
The learning rate decides the size of the improvement steps taken in back propagation. It basically scales the adjustments which need to be made according to the backpropagation algorithm. The larger steps make the model improve the weights faster, but you can also overshoot and improve into a 'wrong' direction. It captures **how confident we want to be in updating our hypothesis** given the input data you just evaluated and error that caused. You can also start with a higher learning rate and lower it every time you improve the model. The learning rate is one of the hyperparameter of the model. 

## Creating a FFNN 
How do you start of? It seems the best to start all the weights with small random numbers. The weights are the parameters of the model which will be learned.  

FFNNs have parameters which are learned (the weights) and hyperparameters which are set by the modeler (you): how many layers, how many units in each layer, which activation function, which loss, which optimizer, which input representation, the learning rate. It is important to explore several constellations and check on a dev. Finding the hyper parameters can be automated with GridSearch. But hopefully you know what hyper are as it has been 3 years at this point.  

## Applications of FFNN
We can use neural networks to create [word vectors](../Semantic-Similarity/Vector%20semantics.md) also known as [word embeddings](../Semantic-Similarity/Embeddings.md). Instead of just [counting words](../Semantic-Similarity/Co-occurrence.md) we train a model to predict the neighbouring words. This has the advantage of **directly building dense vectors** instead of first making space vectors with the counting based models and then projecting them into lower dimensional space. One popular technique to representation learning is [Word2Vec](../Semantic-Similarity/Word2Vec.md). 

Another application is to [use FFNN for language modelling](../Prediction/Using%20FFNN%20for%20language%20modelling.md). This works better than [Markov models](../Prediction/Markov%20models.md) because you don't have to do smoothing. 



### Side note about this 
It was found by that paper mentioned in the guest lecture [(Levy, O., et all)](https://scholar.google.nl/scholar?q=improving+distributional+similarity+with+lessons+learned+from+word+embeddings&hl=en&as_sdt=0&as_vis=1&oi=scholart) that what logistic regression is doing is very much similar to doing co-occurrence counts with [PMI](../Semantic-Similarity/Point%20wise%20mutual%20information%20(PMI).md) [Association measure](../Semantic-Similarity/Association%20measure.md) as weights. We can explain what it is doing. So that is very intresting. This does not hold up for larger neural networks. 

This is the abstract:

*Recent trends suggest that neural network-inspired word embedding models outperform traditional count-based distributional models on word similarity and analogy detection tasks. We reveal that much of the performance gains of word embeddings are due to certain system design choices and hyperparameter optimizations, rather than the embedding algorithms themselves. Furthermore, we show that these modifications can be transferred to traditional distributional models, yielding similar gains. In contrast to prior reports, we observe mostly local or insignificant performance differences between the methods, with no global advantage to any single approach over the others.*

