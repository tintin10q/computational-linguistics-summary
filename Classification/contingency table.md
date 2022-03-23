# Contingency table 
A contingency table shows all the classfications that have been done with the real value. In a contingency table you can see exaclty how things were wrongly classified as what. 

# Example
Here is an example table in a result when classifing languages.

| Language | German | French | Dutch | Italian | English |
| -------- | ------ | ------ | ----- | ------- | ------- |
| German   | 4030.  | 1.     | 2.    | 4.      | 13.     | 
| French   | 3.     | 3385.  | 2.    | 11.     | 7.      |
| Dutch    | 20.    | 2.     | 1230. | 4.      | 24.     |
| Italian  | 0.     | 4.     | 2.    | 10682.  | 4.      |
| English  | 10.    | 20.    | 13.   | 43.     | 16559.  |

So what you can read from this table is that 4030 German words were classified as German 4030 times but also 3 French, 20 Dutch and 10 Itlian words were classified as German. 

1 German word was also classiefied as French.
2 German words were also classiefied as Dutch.
4 German words were also classiefied as Italian.
13 German words were also classiefied as English. 

So that is how you read these tables. 

Here was my code to create the [[Evaluating Classification models]] scores.


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
    
    fn = sum(map(lambda x : x[[True if i == index else False for i in range(len(ct))]], ct.T))
    
    return tp / (tp + fn)
    


def F_measure(contingency_table, label, Beta=1):
    P = precision(contingency_table, label)
    R = recall(contingency_table, label)
    return ((Beta**2 + 1) * P*R) / (Beta**2 * P + R)
```

