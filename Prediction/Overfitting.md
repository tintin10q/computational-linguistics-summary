# Overfitting 

Overfitting is when you make your supervised [[Learning]] model to focused on the training data that you have. When this happens your model will be great at predicting your training data, but it will suck at predicting data that you have not seen before especially if it is close to the decision boundary. 

This can generally be seen in big difference in training scores and test scores where training scores are high and test scores a low. 

![[Pasted image 20220216115427.webp]]

![[Pasted image 20220216115205.webp]]

## Preventing overfitting
You can prevent overfitting by splitting your data into different groups. You take the biggest part of the data as the **training data**. The data that the model actually uses to make predictions. Then you have the **test data or development data** which you use to access the models' performance during training. When this is done you need to have a third set of data the **validation set** to check if you didn't overfit on the test data. 

In the knowledge clip he calls it differently. See the image. 

![[Pasted image 20220216120004.webp]]

## K-fold cross validation
Here you split the data into k portions of the same size, then iteratively train on k-1 sub sets and test on the remaining sub-set. Then you average scores of the k runs. K is usually like 5 or 10 he says. 




