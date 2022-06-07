# Contingency table 
A contingency table shows all the classifications that have been done with the real value. In a contingency table, you can see exactly how things were wrongly classified as what. 

# Example
Here is an example table in a result when classifying languages.

| Language | German | French | Dutch | Italian | English |
| -------- | ------ | ------ | ----- | ------- | ------- |
| German   | 4030.  | 1.     | 2.    | 4.      | 13.     | 
| French   | 3.     | 3385.  | 2.    | 11.     | 7.      |
| Dutch    | 20.    | 2.     | 1230. | 4.      | 24.     |
| Italian  | 0.     | 4.     | 2.    | 10682.  | 4.      |
| English  | 10.    | 20.    | 13.   | 43.     | 16559.  |

So what you can read from this table is that 4030 German words were classified as German 4030 times but also 3 French, 20 Dutch and 10 Italian words were classified as German. 

1 German word was also classified as French.
2 German words were also classified as Dutch.
4 German words were also classified as Italian.
13 German words were also classified as English. 

So that is how you read these tables. 

Here is example code to create the [evaluating classification models](Evaluating%20Classification%20models.md) scores.


```python
def perf_measure(y_actual, y_hat):
    TP = 0
    FP = 0
    TN = 0
    FN = 0

    for i in range(len(y_hat)): 
        if y_actual[i]==y_hat[i]==1:
           TP += 1
        if y_hat[i]==1 and y_actual[i]!=y_hat[i]:
           FP += 1
        if y_actual[i]==y_hat[i]==0:
           TN += 1
        if y_hat[i]==0 and y_actual[i]!=y_hat[i]:
           FN += 1

    return TP, FP, TN, FN

def precision(y_actual, y_hat):
	TP, FP, TN, FN = perf_measure(y_actual, y_hat)
    return TP / (TP + FP)


def recall(contingency_table, label):
	TP, FP, TN, FN = perf_measure(y_actual, y_hat)
    return TP / (TP + FN)

def F_measure(y_actual, y_hat, Beta=1):
    P = precision(y_actual, y_hat)
    R = recall(y_actual, y_hat)
    return ((Beta**2 + 1) * P*R) / (Beta**2 * P + R)
```