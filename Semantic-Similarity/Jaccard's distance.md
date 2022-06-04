# Jaccard's distance
 The Jaccard distance is a simple way to quantify how similar the [context](Context.md) is of two words is. 

The idea is Jaccard's distance is that you divide the intersection of two sets and the union of two context sets. This gives a value between 1 and 0. With 1 being complete overlap and 0 being no overlap. This is a more general method to compute the similarity of two sets. 

This is idea can be expressed with this math: $$\text{Jacc}(\textbf{x},\textbf{y}) = \frac{\textbf{x}~\cap~\textbf{y}}{\textbf{x}~\cup~\textbf{y}}$$

You can use Jaccard distance to calculate the similarity between two [co-occurrence](Co-occurrence.md) sets. 

This method is very flat and coarse. There is no information about co-occurrence frequency or about context similarity,, and it is prone to chance co-occurrences. Basically every item only exist once in a set, so there is no frequency taken into account. To do that, you need to look at  [Co-occurrence counts](Co-occurrence.md).


