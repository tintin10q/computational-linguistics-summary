# Co-occurrence

Co-occurrence is a simple way of comparing the meaning of words in a corpus without the need for annotation or a [thesaurus](../Data/Thesaurus.md).  The idea is to create a co-occurrence sets for the two words from the [context](Context.md) they appear in. 

You do this by specifying the length of your context, for instance a sentence, and then you just add all words to a set which co-occur in that context around the target word.  
 
After you have these sets, you can use the [Jaccard's distance](Jaccard's%20distance.md) to derive at a similarity measure. If you want, you can also visualize this as a [vector](Vector%20semantics.md) instead of a set where every value in the vector is either 0 or 1 to indicate if the word appeared in the context of the target word or not. 

|       | Cat | Food | Music | Beans |
| ----- | --- | ---- | ----- | ----- |
| Cat   | 1   | 1    | 0     | 0     |
| Food  | 1   | 1    | 1     | 1     |
| Music | 0   | 1    | 1     | 0     |
| Beans | 0   | 1    | 0     | 1     |

This method is very flat and coarse. There is no information about co-occurrence frequency or about context similarity,, and it is prone to chance co-occurrences. Basically every item only exist once in a set, so there is no frequency taken into account. To do that, you need to look at co-occurrence counts.  

# Co-occurrence counts 
To improve upon co-occurrence, you can also count how often a word appears in the context of a target word. Instead of just adding words which appear in a context of a target word to a set. 

I would do this like this:

```python
from collections import defaultdict

# Get the corpus data
with open('corpus.txt') as corpus_file:
	corpus = corpus_file.read()

# A word will have the default value of a default dict with 0 as default value
co_occurence_counts = defaultdict(lambda : defaultdict(lambda : 0))

words_in_corpus = set(corpus.split(' '))

sentences = set(corpus.split('.'))

for target_word in words_in_corpus: # Make the count for every word 
	for sentence in sentences:  # Sentence is the context here
		sentence = sentence.split(' ')
		if target_word in sentence:
			sentence.remove(target_word) # Don't co occure with yourself
			for word in sentence:
				co_occurrence_counts[target_word][word] += 1

# Now you have a dict with all the words and the counts of the words in their context

# Because of the default dict all other words will be 0 if accessed.

# Hopefully you can see how the dict relates/can be easily transformed to a matrix/vector space 
```

This then gives you a matrix something like this (but then bigger):

|       | Cat | Food | Music | Beans |
| ----- | --- | ---- | ----- | ----- |
| Cat   | 20   | 16   | 2     | 6     |
| Food  | 16  | 4    | 1     | 70    |
| Music | 2   | 1    | 40     | 0     |
| Beans | 6   | 70   | 0     | 100     |

This matrix represents the **vector space**. Then you can compare rows of this vector space (which are the embeddings) by computing the [Cosine](Cosine.md) angle between two rows (vectors). 


## Hyperparameters 
Both these methods have hyperparameters which can vary. For instance, you can pick different context sizes, leave out the x most frequent words in the corpus. Assign different occurrence counts the further a word is from the target words, and on and on. You can also use [N-grams](../Languages/N-grams.md) instead of words, for instance.

# Problems with count based embeddings
We are just assigning the same number to each word which occurs in the context. However, some words in the context might provide more information than others. This method currently does not take advantage of that. Basically, the raw frequency counts don't take into account the information provided by the context. 

The vectors are **very space** (because of the [Zipfian Distribution](../Languages/Zipfian%20Distribution.md) of language) as the vectors are the same size as every distinct word in the corpus, often like 40,000 in size. The most of the vector will just be 0. These things could be solved somewhat by tweaking the hyperparameters described above. You want to apply [dimensionality reduction](Dimensionality%20reduction.md) to make the embeddings more usable. 

## Association measure
To solve the not taking into account of information problem is to weight each count collected for each word which appeared in the context by an **[association measure](Association%20measure.md)** before you compute the cosine angle between two vectors. 

