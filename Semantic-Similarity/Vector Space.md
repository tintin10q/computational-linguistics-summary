# Vector Space
When you have computed [Embeddings](Embeddings.md), basically represented a bunch of words into vectors. Usually these vectors are the same length because you check all the [context](Context.md) for with all the target words. This means you can put all the embeddings on top of each other because they have the same columns if you wil.  

This then represents the vector space. The n-dimensional space in which all word embeddings reside.  

 A vector space is essentially a matrix created by putting all the vectors on top of each other. Rows are targets, columns are contexts. Targets and contexts can be anything. You can imagine the vector space as a large n-dimensional space in which all the vectors have a location. 

Tree examples below. The first one is with [Co-occurrence](Co-occurrence.md) of words in context around targets words. The second one counts how often words occur in certain document contexts. You can also derive them using neural networks, which leads to less interpretable vector spaces. The last example is a vector space plotted in 3d space to give an idea how you can imagine the vectors having a position in a high dimensional space. 

The cat cell I think means that around the target word cat, cat appeared again. 

|       | Cat | Food | Music | Beans |
| ----- | --- | ---- | ----- | ----- |
| Cat   | 5   | 16   | 2     | 6     |
| Food  | 16  | 10   | 1     | 70    |
| Music | 2   | 1    | 40    | 0     |
| Beans | 6   | 70   | 0     | 4     | 


|       | Document 1 | Document 2 | Document 3 | Document 4 |
| ----- | ---------- | ---------- | ---------- | ---------- |
| Cat   | 20          | 16         | 2          | 6          |
| Food  | 16         | 3          | 1          | 70         |
| Music | 2          | 1          | 15          | 0          |
| Beans | 6          | 70         | 0          | 60          |


![Vector space example](../images/Pasted%20image%2020220606221314.png)