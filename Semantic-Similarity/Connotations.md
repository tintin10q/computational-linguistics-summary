# Connotations 
In the fields of computational linguistics, the word connotation means the aspects of a word's meaning related to the writer or reader's emotions. Osgood et al.., 1957 quantified this in 3 dimensions:

- **Valence – The pleasantness of the stimulus 
- **Arousal – The intensity of emotion provoked by the stimulus
- **Dominance – The degree of control exerted by the stimulus. Slave is low in dominance and master is high. 

When words score the same across 2 or 3 of these dimensions, you can maybe assume the words are similar. 

The actual values of the connotations have to be gathered by asking a bunch of humans and then averaging the results. This leads to tables of words like below: 

|  **Word**   | **Valence** | **Arousal** | **Dominance** |
|-------------|-------------|-------------|---------------|
| courageous  | 8.05        | 5.5         | 7.38          |
| music       | 7.67        | 5.57        | 6.5           |
| heartbreak  | 2.45        | 5.65        | 3.58          |
| cub         | 6.71        | 3.95        | 4.24          |

This now allows you to represent all these words as a vector of 3 scalers across 3 dimensions. So cub can be represented as [6.71, 3.95, 4.24].  This is a powerful idea, see [vector semantics](Vector%20semantics.md). One way to compare words when represented as vectors is with the [Cosine](Cosine.md) angle between the two vectors, or the [Jaccard's distance](Jaccard's%20distance.md). However, arriving at these vectors with the connotation's method requires human annotation. 

> Vectors are basically just lists of numbers 
