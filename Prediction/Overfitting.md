# Overfitting 

Overfitting is when you make a supervised [learning](../Other/Learning.md) model too focused on the training data that you have. When this happens, your model will be great at predicting your training data, but it will suck at predicting data that you have not seen before, especially if it is close to the decision boundary. 

This can generally be seen in big difference in training scores and test scores, where training scores are high and test scores a low. 

![Overfitting example 1](../images/Pasted%20image%2020220216115427.png)

![Overfitting example 2](../images/Pasted%20image%2020220216115205.png)

When you have overfitted your model can predict the training data extremely wel, but it is not generalizable to new data. 

## Preventing overfitting

You can prevent overfitting by splitting your data into different groups. You take the biggest part of the data as the **training data**. The data that the model actually uses to make predictions. Then you have the **test data or development data**, which you use to access the models' performance during training. When this is done you need to have a third set of data, the **validation set**, to check if you didn't overfit on the test data. 

In the knowledge clip, the 3 sets are called differently. See the image:

![Prevent Overfitting by splitting data in a training set, development set and test set](../images/Pasted%20image%2020220216120004.png)

## K-fold cross validation
Here you split the data into k portions of the same size, then iteratively train on k-1 sub sets and test on the remaining sub-set. Then you average scores of the k runs. K is typically like 5 or 10. 




