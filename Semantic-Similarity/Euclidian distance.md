# Euclidean distance 
The Euclidian distance calculates the distance between two points by:

1. Calculating the distance between each coordinate of the point and 
2. Multiplying each distance by itself 
3. Summing all the distances from every coordinate 
4. Taking the square root of that. 

If we have the two vectors $\textbf{v}$ and $\textbf{w}$ this can be expressed with math like so: $$d(\textbf{v}, \textbf{w}) = \sqrt{(\textbf{v}_{0}-\textbf{w}_{1})^2+(\textbf{v}_{0}-\textbf{w}_{1})^2+...+(\textbf{v}_{n}-\textbf{w}_{n})^2}$$ 
Here d stands for distance. 

For [embeddings](Embeddings.md) this is **not** a good measure of [similarity](Similarity.md) because it is heavily influenced by absolute large differences. For example, if the distance of only one coordinate is really high, for instance 300 and all the other distances are around 3 then the computer still thinks the two embeddings v and w are far away from each other. 

![Euclidian vs cosine distance](../images/Pasted%20image%2020220606220215.png)