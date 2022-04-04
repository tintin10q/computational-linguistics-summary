# Evaluating Classification Models
After you have made your [classification](../Classification.md) system how do you evaluate it against other options?

## Intrinsic Evaluation
Define a metric and check which system does best.

## Extrinsic Evaluation
Embed a tool in a larger system and check how much performance on a downstream task improves given the output of two different versions of your tool. So you have the classifier, but you see how much the performance on something the classifier would be used for improves.  


## Example
Lets say spam detection.

- Intrinsic evaluation would be we have a bag of spam emails and normal emails. Then we could say the classifier was correct 95% of the times and incorrect 5% of the times.
- Extrinsic evaluation would be like we got 66% decrease in people that got scammed that used our tool. 

So extrinsic is not the tool itself you evaluate, but you see in how the tool helps to achieve a goal it was made for and if it helps at all. 

---

We would like a spam filter to be perfect, but this is not going to happen. Either you classify emails as spam when it's not spam, or you miss emails as spam when its is spam. You have to choose which one is worse for your application. 

# Intrinsic evaluation methods

Whenever you get results from your model you get:

- True positives (TP): Correctly classified that it was this class.
- True negatives (TN): Correctly classified that it was not this class.
- False positives (FP): Incorrectly classified that it was this class.
- False negatives (FN): Incorrectly classified that it was not this class.

From these we can come up with intrinsic evaluations.

![Pasted image 20220216130019](../images/Pasted%20image%2020220216130019.webp)

## Acuracy 
Acuracy is the number of correctly classified points. Simple.

## Precision 
The first one is precision. The idea of this is that you divide the true positives by all the data points that where classified as this class. So this means:
$$Precision = \frac{TP}{TP+FP}$$

This can be seen as a percentage of all points that were classed as this class that was correct. So precision really punishes false positives. It doesn't matter if you missed some true positives as long as you don't have a lot of false positives. 

To use this measure you need to classify at least one true positive otherwise you try to divide 0 and then the score is 0. 

## Recall
Recall is the proportion of correctly classified data points out of the data points which belonged to that class. 

$$Recall = \frac{TP}{TP+FN}$$

You can see recall of the number of correctly classified spam emails out of the emails that should have been classified as spam. You don't care about the mistakes, but you care about that you catch everything you have to catch. 

With recall, it doesn't matter how often you wrongly guessed as long as you got all data points which belonged to the class (the true positives). So this punishes false negatives. I think false negatives are the worst. 

There is another [explanation by google here](https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall) about recall and precision. 

## F-Measure
F-Measure combines precision and recall into a new shiny formula. F-Measure is described as the harmonic mean between precision and recall. The harmonic mean is more conservative than the arithmetic mean. 

This is the formula:

$$F~Measure = \frac{(\beta^{2} + 1) \cdot Precision \cdot Recall}{\beta^{2}  \cdot Precision \cdot Recall}$$

The idea of the $\beta$ is a weight that you can use to make either precision or recall more important. If you do $\beta \gt 1$ you make recall more important and $\beta \lt 1$ than you make precision more important.

Often you don't make one more significant than the other, and you just set $\beta = 1$. When you do this you call the F-Measure score the **F1 score**. Setting $\beta$ is mostly based on domain knowledge. If you don't have it then just set it to 1.


### Code 

Here is code to get the scores in python.

```python
def precision(contingency_table, label):
    index = labels2ids[label]
    result = contingency_table.T[index]
    
    tp = result[index]
    
    mask = np.ones(len(result), bool)
    mask[index] = False
    
    fp = sum(result[mask])
    
    return tp / (tp + fp)


def recall(contingency_table, label):
    ct = contingency_table
    index = labels2ids[label]
    
    result = ct.T[index]
    
    tp = result[index]
    
    fn = sum(map(lambda x : x[[len(ct))](ct|True if i == index else False for i in range(len(ct|[len(ct|[len(ct|[len(ct))](ct))]])))]])), ct.T))
    
    return tp / (tp + fn)
    


def F_measure(contingency_table, label, Beta=1):
    P = precision(contingency_table, label)
    R = recall(contingency_table, label)
    return ((Beta**2 + 1) * P*R) / (Beta**2 * P + R)
```


### Macro averaging
When there are more than two classes, we compute the F-measure for all classes separately and then average them assigning equal importance. **This is useful when good performance is necessary in all the classes**, regardless of the frequency in which they appear. Because if you do it like this one class that has bad performance will decrease the averaged F1 score a lot. 

### Micro averaging
With micro averaging you collect all the decisions for all the classes in a single [contingency table](contingency%20table.md) and then compute precision and recall from that table. This is usefull when good performance is more imporatnt for the most frequent classes. 

## Statisical test
You can often not use statistical test like t-test because often classification samples are not normally distrobuted. 

## Bootstrapping
Bootstrapping is when you artificially increase the number of test sets by drawing a lot of samples from a given test set with replacement (use multiple times), perform your task, record the score, factor the performance of the whole test set, then simply check the percentage of runs in which a system beats the other. This is not super important. 

So you pick samples of data points of the whole test set and then run multiple times. You can then see if one system is more better then the other on many samples. 


