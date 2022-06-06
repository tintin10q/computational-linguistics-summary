# Explanation / Analysis  Questions 
Practice open questions were provided. 

>These are the Answers are by Marieke.

## 8 pts - 100 words: EXPLANATION/ANALYSIS QUESTIONS

### Explain the steps involved in computing PPMI  and what role PPMI plays in the pipeline used to derive a count-based DSM (distributional semantic network).

PPMI ([Positive Point wise mutual information](../Semantic-Similarity/Point%20wise%20mutual%20information%20(PMI).md)) is a measure of how informative a word and context combination is by finding the ratio of the word occurring in the context divided by the occurrence of the word and the context on their own (count based probabilities). All negative values are set to 0 to have a sense of interpretability of the informativeness. The PPMI is then used as weights when computing cosine similarity between vector embeddings to give more importance to more informative data points. These weighted cosine similarities can then be leveraged to find semantic groupings. (95 words)


### Break down the working of the CKY algorithm focusing on the three nested loops used to fill out the parse table

The [CKY](../Languages/CKY.md) algorithm is used to determine whether a sentence is valid given a grammar by applying a nested looping algorithm. It first determines for each item in the sentence which forms it may take given the grammar, rewriting each item that appears as RHS of a rule as the LHS. Then each further cell of the table is filled; take all combinations of subsets of sentence items up to that point, note the LHS’s of the rules for which the subsets make up a RHS. If the top right cell contains the ‘S’ symbol, the sentence is valid. (99 words)

### Consider Bayes rule and PoS tagging using HMMs (hidden Markov models). Explain how transition and emission probabilities relate to prior and likelihood.

In [Bayes rule](../Classification/Native%20baiyes/Bayes%20rule.md), the prior represents the expectations the algorithm is given regarding how often the class will appear. This is the ratio of how often the class occurs and the size of the document. In HMMs, the transition probabilities capture this idea by representing how often each state follows another state. The likelihood in Bayes’ rule says how likely an item is to occur given that its class is known. This relates to emission probabilities in HMMs because the emission probability also shows the ratios of each word occurring given a tag. (93 words)

## 12 pts – 200 words. EVALUATION QUESTIONS

### Compare and contrast a Markov Chain and an LSTM for language modeling. Highlight similarities and differences in training data, assumptions, goals, architecture (the design of the algorithm) and evaluation

Both MC’s and LTSMs take some form of history into account, but the MC does it based on the Markov assumption (probability of a word given total history can be approximated with local history) whereas the LTSM instead learns to consider some history and forget other parts. MC’s also require smoothing, while LSTM’s don’t. MC are evaluated with perplexity, and LSTMs are evaluated by calculating loss between the prediction and expectation. (71 words)

### Compare lexical-semantic representations in thesauri (a synonym dictionary) and in DSMs, focusing on how they are derived; mention one advantage of DSMs over thesauri and one advantage of thesauri over DSMs; finally, compare how word-similarities are computed in both approaches.

[Thesauri](../Data/Thesaurus.md) are created by people, in an intentional way. The people making thesauri leverage world knowledge and their linguistic reasoning and understanding to express an agreed upon definition of the semantic meaning of a word. This has the advantage that there is transparency of how the representations came to be. Word similarities can be determined in thesauri by calculating edit distances, finding Lesk similarity (gloss overlap), or in the case the thesaurus holds synsets or a tree structure, also with path-length similarity or Resnik similarity. Another advantage is that the information in a thesaurus is easier for human interpretation. 

DMSMs on the other hand use statistical methods to learn semantic distributions in an unsupervised way. Each word type gets a vector embedding based on a chosen metric, such as co-occurrence counts. These vectors can then be weighted by their information content ((P)PMI) and the weighted cosine between these vectors then indicates something about the similarity between words. This has the advantage that no linguistic experts are needed to index the language, only one or a few computational linguists and their computers, which makes it cheaper and faster. It may also reveal latent information about the structure of language and semantics. (200 words)

## 20 pts - 300 words. SYNTHESIS QUESTION

### People read more predictable words given the preceding context faster. Discuss how you would extrinsically evaluate two language models, an n-gram model and an LSTM, using a dataset which provides the average time it took to people to read each word in a sentence as measured with an eye-tracker. What information would you extract from each model? How do you expect it relates to reading times? What data would you use to train the language models for them to be good at predicting reading times? Justify your choice.

The extrinsic evaluation of each model can be done by comparing the reading times to the probability output of each model for certain words (correlation). From the [N-grams](../Languages/N-grams.md) model, we would take the perplexity for each word and expect it to be a good predictor for reading time, with lower perplexity correlating with shorter reading time and vice versa. In the LSTM the expectation would be that a higher probability for a word given a context leads to shorter reading times and vice versa. The data for training the models should be representative for the goal, so in this case it should be text that is usually read by people, such as Wikipedia articles or subtitles. This should ideally be related to or match with the dataset that was used to generate the reading times. (135 words)