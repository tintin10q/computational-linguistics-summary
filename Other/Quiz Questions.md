# Quiz 1 Resources 


<style type="text/css">
    ol { list-style-type: upper-alpha; }
</style>


## Question 1

In CL we use a lot of statistics and probability theory. Why?

- A: They give us several distributions to characterise how people use language.
- B: Natural languages are ambiguous. 
- C: We need to perform statistical tests to compare models.
- D: They offer a set of efficient algorithms for automating processes.
 
## Question 2

Which of the following features does not apply to natural languages?

- A: Subjected to change
- B: Unambiguous 
- C: Conventional
- D: Context-dependent
 
## Question 3

Which level of linguistic analysis deals with the meaning of morphemes and words?

- A: Lexical semantics 
- B: Syntax
- C: Morphology
- D: Compositional semantics
 
## Question 4

Which of the following is a diachronic corpus?

- A:  CHILDES
- B:  SubtLex
- C:  Corpus of Historical American English 
- D:  TASA
 
## Question 5

Which of the following resources is not a lexicon?

- A:  Words with proportion of native speakers who know the word meaning
- B:  Words with concreteness ratings
- C:  Words with age of acquisition estimates
- D:  Words with their meaning definition 
 
## Question 6

What is a valid hyponym of dog in WordNet?

- A: Dalmatian 
- B: Animal
- C: Canine
- D: Cat

## Correct Answers Quiz 1
1. B: Natural languages are ambiguous. 
2. B: Unambiguous 
3. A: Lexical semantics 
4. C: Corpus of Historical American English 
5. D: Cat


# Quiz 2 Naïve Bayes Classification

## Question 1

Which of the following is not an example of text classification?

- A: Essay grading (pass/fail) 
- B: Text simplification 
- C: Sentiment analysis 
- D: Cyberbullying detection
 
## Question 2

Which of the following is an advantage of rule systems?

- A: Robust to rare events 
- B: Cheap to write 
- C: Cannot incorporate domain knowledge 
- D: Can deal with ambiguity effortlessly 
 
## Question 3

Which of the following statements about discriminative classifiers is wrong?

- A: They can only address binary classification problems 
- B: They learn the hidden process which yielded the data sample 
- C: They can only learn linear boundaries 
- D: They are non-deterministic classifiers 

## Question 4

Which of the following is an example of extrinsic evaluation?

- A: Run a t-test between precision scores in automatic grading 
- B: Compute the difference in accuracy between two classifiers 
- C: Measure the customer satisfaction when interacting with two different bots 
- D: Compare translation quality between two machine translation models 
 
## Question 5

What does the likelihood capture in Bayes Rule?

- A: The probability of the class given the input 
- B: The probability of the input 
- C: The probability of the input given the class 
- D: The probability of the class 
 
## Question 6

What does the conditional independence assumption entail in NBC?

- A: An NBC doesn't track feature co-presence 
- B: An NBC doesn't consider the probability of the document given the class 
- C: An NBC doesn't track sequential information 
- D: An NBC doesn't consider all classes when classifying 
 
## Question 7
Which of the following is not a stop word?

- A: I 
- B: Child 
- C: Do 
- D: Because 
 
## Question 8
In a dataset consisting of 100 tweets, 20 contain instances of cyberbullying. For the sake of argument, we pretend to be dealing with 2 binary features: whether the tweet contains at least a curse word and whether the tweet contain non-alphabetic characters. The likelihood that a tweet containing at least a curse word is an instance of cyberbullying is 0.8 while the likelihood that a tweet containing non-alphabetic characters is not an instance of cyberbullying is 0.7.

What is the prior of the cyberbullying class?

- A: 0.1 
- B: 0.8 
- C: cannot tell 
- D: 0.2 

## Question 9

In a dataset consisting of 100 tweets, 20 contain instances of cyberbullying. For the sake of argument, we pretend to be dealing with 2 binary features: whether the tweet contains at least a curse word and whether the tweet contain non-alphabetic characters. The likelihood that a tweet containing at least a curse word is an instance of cyberbullying is 0.8 while the likelihood that a tweet containing non-alphabetic characters is not an instance of cyberbullying is 0.3.

Consider a test tweet with at least a curse word and only alphabetic characters. What is the probability of the test tweet being an instance of cyberbullying?

- A: 0.8 $*$ 0.8 $*$ 0.3 
- B: 0.8 $*$ 0.2 $*$ 0.7 
- C: 0.2 $*$ 0.8 $*$ 0.3 
- D: 0.2 $*$ 0.2 $*$ 0.7 
 
## Question 10

In a dataset consisting of 100 tweets, 20 contain instances of cyberbullying. For the sake of argument, we pretend to be dealing with 2 binary features: whether the tweet contains at least a curse word and whether the tweet contain non-alphabetic characters. The likelihood that a tweet containing at least a curse word is an instance of cyberbullying is 0.8 while the likelihood that a tweet containing non-alphabetic characters is not an instance of cyberbullying is 0.3.

Consider a test tweet with at least a curse word and only alphabetic characters. Would an NBC using these features classify it as an instance of cyberbullying?

- A: Yes 
- B: Not enough information given 
- C: It'd be a tie 
- D: No 


## Correct Answers Quiz 2
1. B: Text Simplification 
2. A: Robust to rare events
3. B: They learn the hidden process which yielded the data sample 
4. C: Measure the customer satisfaction when interacting with two different bots 
5. C: The probability of the input given the class 
6. A: An NBC doesn't track feature co-presence 
7. B: Child
8. D: 0.2
9. C: 0.2 $*$ 0.8 $*$ 0.3 
10. D: No


# Quiz 3 Pre-processing

## Question 1

How many lemmas are there in the sentence: 

"The children were curious about whether there would be a surprise at home or whether there had been enough surprises already." 

Punctuation doesn't count.

- A: 21 
- B: 19 
- C: 18 
- D: 16 
 
## Question 2

How many affixes are there in the word untrustworthy?

- A: 3 
- B: 2 
- C: 0 
- D: 1 
 
## Question 3

Which of the following words is inflected?

- A: Touchstone 
- B: Colourful 
- C: Children 
- D: Professor 
 
## Question 4

Which normalisation technique would you use before doing language identification?

- A: Lemmatisation 
- B: Case folding 
- C: None of them 
- D: Tokenisation 
 
## Question 5

Consider two regular expression /^[a-zA-Z]{2,6}\b/. What does it match?

- A: alphabetic strings between two and six characters at the beginning of a line followed by a word boundary Correct!
- B: any string but alphabetic strings between two and six characters 
- C: Lines containing alphabetic strings between two and six characters 
- D: any string between three and six characters
 
## Question 6

What is the minimum edit distance between glowing and growling? 

- A: 4 
- B: 1 
- C: 2
- D: 3 

## Correct Answers Quiz 3
1. D: 16
2. B: 2
3. C: Children
4. C: None of them
5. A: alphabetic strings between two and six characters at the beginning of a line followed by a word boundary
6. C: 2

# Quiz 4 Language modelling 

## Question 1

How do we use language modelling in machine translation?

- A: To make sure the translation has the same meaning as the source
- B: To predict the next sentence in the translation
- C: To pick the most fluent candidate translation  
- D: To pick the best word among possible candidate translations for a word in the source

## Question 2

Why do we care about the chain rule of probability?

- A: It tells us how to compute the probability of a sentence 
- B: It deals with the infinite nature of language
- C: It tells us how to use limited context to approximate larger contexts
- D: It tells us how to deal with underflowing problems

## Question 3

How do we get ML estimates for bigram transition probabilities?

- A: Get co-occurrence counts and normalise by row marginals 
- B: Get co-occurrence counts and take the log
- C: Get co-occurrence counts and normalise by column marginals
- D: Get co-occurrence counts and normalise by the matrix total

## Question 4

Which of the following is NOT a component of Markov Chains?

- A: Transition counts
- B: Initial probability distribution
- C: Accepting state 
- D: History states

## Question 5

If we fit a 4-gram language model, how many BoS symbols do we need to prepend to the sentences?

- A: 1
- B: 4
- C: 2
- D: 3 

## Question 6

In linear interpolation, lambdas have to meet a strict requirement. Which one?

- A: Their sum must equal 1 
- B: They must be lower than 1
- C: The highest value matches the largest n-gram available
- D: Their algebraic sum must be 0

## Correct Answers Quiz 4
- C: To pick the most fluent candidate translation
- A: It tells us how to compute the probability of a sentence 
- A: Get co-occurrence counts and normalise by row marginals
- C: Accepting state
- D: 3
- A: Their sum must equal 1

# Quiz 5 PoS Tagging

## Question 1

Which of the following lexical categories is an example of open class words?

- A:  Auxiliaries 
- B:  Possessive pronouns
- C:  Adverbs 
- D:  Conjunctions 
 
## Question 2

In terms of PoS tag ambiguity, types tend to be .... tokens?

- A:  More ambiguous than 
- B:  As unambiguous as 
- C:  Less ambiguous than 
- D:  As ambiguous as 
 
## Question 3

What does the emission probability matrix encode in a bigram HMM?

- A:  The probability of a word given a word 
- B:  The probability of a tag given a word 
- C:  The probability of a tag given a tag 
- D:  The probability of a word given a tag 
 
## Question 4

Which component of the HMM encodes the Markov assumption?

- A: The sequence of observations 
- B: The observation likelihood matrix 
- C: The initial distribution 
- D: The state transition probability matrix 
 
## Question 5

The Viterbi algorithm is an example of?

- A:  A classifier 
- B:  A dynamic programming algorithm 
- C:  A rule-based system 
- D:  A vector space 
 
## Question 6

What is the complexity of the Viterbi algorithm? Q is the set of states, t is the length of the sentence, n is the order of the model, V is the vocabulary size.

- A:  $O(Q^t)$ 
- B:  $O(V^t*n)$
- C:  $O(Q^n*t)$ 
- D:  $O(Q*V)$ 
 
## Question 7

Which of the following quantities does not contribute to the computation of the new posterior probability of observing each tag given the sequence of observed events up to that point?

- A: Transition probabilities from state $q_i$ to state $q_j$ 
- B: Emission probability for observation o_j given state $q_j$ 
- C: Posterior probability up to the previous observed event 
- D: The likelihood of state $q_j$ given observed event $o_j$  

## Question 8
In the Viterbi algorithm, we apply the argmax function. What is the input?

- A: The last column in the trellis 
- B: The product of the last column in the trellis, the transition probability matrix and the emission probability matrix 
- C: The product of the last column in the trellis and the transition probability matrix
- D: The product of the transition and emission probability matrices

## Correct Answers Quiz 5
1. C: Adverbs 
2. D: Less ambiguous than 
3. D: The probability of a word given a tag
4. D: The state transition probability matrix
5. B: A dynamic programming algorithm
6. C: $O(Q^n*t)$
7. D: The likelihood of state $q_j$ given observed event $o_j$
8. C: The product of the last column in the trellis and the transition probability matrix

# Quiz 6 Syntax 

## Question 1 

Which of the following is not a component of a grammar?

- A: a finite set of non-terminal states
- B: a distinguished start state
- C: a finite set of terminal states
- D: an infinite set of production rules 
 
## Question 2

Which of the following rules is in CNF?

- A: S → he ran
- B: S → NP VP NP
- C: S → you VP
- D: S → NP VP 
 
## Question 3

What kind of corpus do we need to estimate a CFG?

- A: Plain corpus
- B: Parallel corpus
- C: Treebank 
- D: Corpus with PoS annotations
 
## Question 4

Which is the defining feature of an S constituent?

- A: Its main verb has all its arguments 
- B: Can only occur as the LHS of rules
- C: Cannot be coordinated with other S constituents
- D: Always contains at least one NP
 
## Question 5

What is the relation between CFGs and dynamic programming?

- A: We can use dynamic programming because context changes our sub-parses
- B: We cannot use dynamic programming because context will change our sub-parses
- C: We can use dynamic programming because context cannot change sub-parses 
- D: They're unrelated
 
## Question 6

In order to initialise the table for the CKY, what do we need to know?
Group of answer choices.

- A: The number of possible rules in the grammar
- B: The number of non-terminals in the grammar
- C: The number of terminals in the grammar
- D: The symbols in the target sentence 
 
## Question 7

How do we use the CKY to know if a string is grammatical?
Group of answer choices.

- A: We check whether the final cell contains the S state 
- B: We check whether the final cell is not empty
- C: We check whether the S state happens anywhere in the table
- D: We check whether all terminals appear as the RHS in at least one rule
 
## Question 8

Which of the following is a pre-terminal symbol?

- A: N 
- B: NP
- C: PP
- D: do


## Correct Answers Quiz 6
1. A: an infinite set of production rules
2. D: S → NP VP
3. C: Treebank 
4. A: Its main verb has all its arguments
5. C: We can use dynamic programming because context cannot change sub-parses
6. D: The symbols in the target sentence
7. A: We check whether the final cell contains the S state
8. A: N