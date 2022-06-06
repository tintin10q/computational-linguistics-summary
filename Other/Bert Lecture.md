# Computational linguistics class about the BERT paper

BERTology. (Bidirectional Encoder Representations from Transformers). Headings are per section of the paper.

> Thanks to Marike for this file
  
## Advantages of BERT as compared to other (neural net) language models.

BERT is better at dealing with longer sentences (long-range dependencies). This is because it is a transformer model (not a neural net, not exactly deep learning). Problem with recurrent neural nets: [Vanishing gradient problem](../Prediction/Vanishing%20gradient%20problem.md). This means that if you go too far back in the input, it gets multiplied by the 0-1 parameters over and over again and gets smaller and smaller; this makes it so that the model stops learning. The BERT model (transformer) doesn’t have this issue, as it uses a different version of recurrence.

Parallel processing is also efficient in BERT given the right hardware. The model is pre-trained on a huge amount of data, and it is very big; the architecture itself is efficient (more than LSTM) but very big.


## Explain the workflow of BERT.

1.  Pre-training, self-supervised. Train model with a large amount of data (Wikipedia, books, etc). To learn general knowledge about language.
    
    1.  Masked language modelling: given a sentence, mask out a word and train the model to predict the missing word (MLM)
        
    2.  Next sentence prediction: given two sentences, the model predicts whether they are consecutive (NSP)
        
2.  Finetuning (adding one or more layers on top of the pre-trained architecture). Here, the model is trained on a more specific task or dataset, such as sentiment analysis or POS tagging.
    

  

## Which type of syntactic information does BERT seem to learn

_Syntax in language is very symbolic. Finding information in a NN about its syntactic knowledge is hard; is it representing the right thing?_

The model has some representations of hierarchical information (word dependency tree structures). More specifically; part-of-speech and chunks and thematic roles (agent-patient) are embedded in the model. This is impressive as the model learns unsupervised using NSP and MLM. Model is not very good at Negative Polarity Items (between syntax and semantics); it can understand the use of ‘Whether..ever’ but not the correct scope of those or negations. The syntactic information that the model learns is not necessarily similar to annotated linguistic resources.

  

## What is the reason why BERT struggles with world-based reasoning?

My guess: maybe the MLM unsupervised learning leads to this difficulty and the other way around (predict sentence from word) might improve the ability of the model to perform reasoning tasks. Raquel says, ‘idk, but interesting!’.

The model might also improve when training on structure and relationship (tagged) data, rather than pure unsupervised learning. Humans might have a specific reasoning ability that is not built into the model. A lot of knowledge and reasoning and world-awareness is known by people, which is not built into our language. This means the data the model is trained on is not complete with this inferred information; we don’t say ‘I walk into the house because the house is bigger than I am’. When we say ‘I walk into the house’, there is a natural implication and social understanding that the house is indeed bigger than I am. The model does not have this information in the training data and as such cannot (does not) learn the reasoning.

## If you have a BERT model with vectors that reflect semantic relations, then which part of the model represents the semantic similarity space? (Higher layers, intermediate, combinations?)

Semantic information is represented throughout the model’s layers. In later stages, it involves tokens (individual occurrences of words) and in earlier layers, the semantic value of the word more generally speaking. Then there is also the vector space which collapses the semantic information into a sort of ‘cone’ shape in the vector space.

Semantics are learnt from the context in the MLM task. The model gives us a different vector for each token; so every occurrence of a word, even if it’s the same word, gets its own representation vector. These need to be aggregated for getting type information. The BERT model is very deep (word2vec is not deep; only the first layer is used). In BERT you can use different layers’ information depending on your task. Probing can be done to see which layer is more useful, can also do averages or weighted averages. For example, can take the first layer(s) because they are more useful for getting a certain type of information about a sentence.

## How would you change your answer to the previous question after reading the following section, 4.3 BERT Layers, if at all?

Combining information from different layers is the best (only?) way to get the semantic information. This is spread across all layers of the model, independent of the model size. The first layers capture simple word order rules, middle layers syntactic information, and later layers capture task specific information. The semantics are weaved through all layers; this makes intuitive sense too because often the semantic meaning of our real-world language use also changes based on context (task) and social situation (grammar, word order).

In the end, language is used to communicate; semantics (what does it _mean_) is a basic goal of language use. Everything else always interacts and interfaces with semantics.

## Why is overparametrization a problem?

Typically, the more parameters a model has, the more it can learn, though it can also lead to [overfitting](../Prediction/Overfitting.md). However, with BERT the problem is more so that the enormous amount of parameter also leads to intense computational complexity and electricity use. This is an environmental concern, especially as long as the majority of power is not generated in a clean (green) way. It also leads to differences between countries, companies and individuals with more vs less resources (financial, hardware, human). Reproducibility is also a big issue; the bigger the model, the harder it is to reproduce and do science on whether it is really that good or if they be lyin’ to us.