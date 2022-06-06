# Point wise mutual information (PMI) 
One way to get weighs for an [association measure](Association%20measure.md) to the embeddings with is **point wise mutual information**. This is an intuitive method. The idea is to weight the co-occurrences of words that happen **more often than expected by chance** more, since these co-occurrences capture some linguistically relevant phenome. 

If [language](../Languages/Languages.md) was random (entropy at the max) we would have no association weights, everything would be as likely as everything else. PMI works because language is not random. This means you can know how often something should appear. When things appear more often together then you would expect, then you weigh it more. 

To do this, you can count the frequencies of the words in the entire corpus divided by the total number of [tokens](../Data/Token.md) to get an expected chance. If you then observe co-occurrence counts with higher chance than you calculated, you weight these counts higher, as this might encode the linguistic meaning you are after. You can also weight the counts which are at chance level lower.

Calculating the PMI of a word [embedding](Embeddings.md) $\mathbf{w}$ can be expressed in math as: $$PMI(\textbf{w},\textbf{c}) = \log_2\frac{p(\textbf{w},\textbf{c})}{p(\textbf{w})p(\textbf{c})} = \log_2\frac{\frac{\text{count}(\textbf{w},\textbf{c})}{V}}{\frac{\text{count}(\textbf{w})}{V}*\frac{\text{count}(\textbf{c})}{V}}$$
Up top you have: The probability of the co-occurrence happening.  

At the bottom, you have: You have an independent probability. How likely are the word and the context to occur together. You get this by multiplying the probability of how likely the target word is and how likely the context is when they occur alone. 

Here $V$ is the total number of tokens in the corpus. $\textbf{c}$ is the context, $\textbf{w}$ is the target word.

Now if the PMI is high then the co-occurrence count is probably interesting because it is higher than chance. 

Remember, we calculate PMI to be able to get weight for the association measure. So we multiply the PMI with the embedding. After that, calculate the cosine. This resolves the problem where you don't take into account information from the context. So the PMI is the weight.

Also, you use log to smooth things out when the frequencies get large. 

## Positive PMI (PPMI)
Cosine similarity can take the values between -1 and 1. Where 0 means nothing in common, 1 means same angle. -1 means opposite direction. No one has been able to interpret -1 cosine values, so to avoid negative similarity scores (which we can't interpret) we force all cells in the vector space to be positive. This is done by saying if something co-occurs less often than expected by chance, we just say its PMI is 0 which then weights by 0 which result in 0 instead of a negative number. 

The things that get the highest PMI are things like names, which don't occur often and always appear together. Like NEW YORK. Also, colours like blue and red get a high PMI. So things which are rare which occur together get high PMI.

You could express this in math as $PPMI(x) = \text{abs}(PMI(x))$

## Problems with PMI
Things which co-occur together more expected than chance get a boost and things which co-occur less often than change get dragged down (matter less). But if you have two things which only occur once and also co-occur together will get a PMI score of 1 as in this case its $\frac{1}{1*1}$. 

So if two rare things occur together, they have the highest PMI, which in general favours low-frequency co occurrences generated from low-frequency targets and contexts. 

From this the computer thinks that if the first word appears then the second word also always appears. However, if a word only appears once, then this it could be an error and not really display a pattern in the language.  

### Example 
If the words "entry" and "shell" only occur once in a [corpus](../Data/Corpus.md) and also co-occur the only time they do occur, so like *You enter through the entry shell.* This means that in theory you get all the information of shell by observing entry. This will get a PMI of 1. But really the corpus just lacks more occurrences of entry and shell. You can solve this by adding a bias. There are two examples of bias below.

### Local mutual information 
To deal with this you multiply the result of the PMI formula which is the log frequency of target co-occurrence. This is just taking the log of how often the co-occurrence appears. The log of 1 is 0 so then all things which only occur once disappear. 

Things which often occur still get boosted because the log of the absolute occurrence will still be high. So now to get a high PMI score you need to occur frequently and also often together with something else which is exactly what we want.

### Context exponent
You can also include an exponent when computing the context probability such that it increases the probability of rare events.

## PMI tutorial

How to calculate PMI. Let's say you have a [Vector Space](Vector%20Space.md) like this:

|     | of   | the  | dog | run |
| --- | ---- | ---- | --- | --- |
| of  | 5    | 1000 | 100 | 55  |
| the | 1000 | 400  | 500 | 100 |
| dog | 100  | 500  | 10  | 40  | 
| run | 55   | 100  | 40  | 20  |

And we want to calculate PMI between **dog** and **the**?

We want $PMI(\textbf{dog},\textbf{the})$

We do this by using the formula $PMI(\textbf{dog},\textbf{the}) = \log_2\frac{p(\textbf{dog},\textbf{the})}{p(\textbf{dog})p(\textbf{the})} = \log_2\frac{\frac{\text{count}(\textbf{dog},\textbf{the})}{V}}{\frac{\text{count}(\textbf{dog})}{V}*\frac{\text{count}(\textbf{the})}{V}}$ 
So we start with: 

$$\log_2\frac{\frac{\text{count}(\textbf{dog},\textbf{the})}{V}}{\frac{\text{count}(\textbf{dog})}{V}*\frac{\text{count}(\textbf{the})}{V}}$$
Remember the numerator is the count of the word and the context co-occurring divided by V. **Calculate V at the end if you have to, and it is not given**. The $\text{count} ( \textbf{dog}, \textbf{the} )$ in $\frac{ \text{count} ( \textbf{dog}, \textbf{the} )}{V}$ in the nominator is exactly what the table describes, so it can be directly read from the table (in this case the dog, the cell). This cell is 500 so that gives: $$\log_2\frac{\frac{500}{V}}{\frac{\text{count}(\textbf{dog})}{V}*\frac{\text{count}(\textbf{the})}{V}}$$

To get $\text{count}(\textbf{dog})$ you just sum the **dog** row. So $\text{count}(\textbf{dog}) = 100 + 500 + 10 + 40 = 650$.

For $\text{count}(\textbf{the})$  and you sum the **the** column. You sum the column because **the** in this case is the context. So $\text{count}(\textbf{the}) = 1000 + 400 + 500 + 100 = 2000$. We can now fill that in to the formula:  $$\log_2\frac{\frac{500}{V}}{\frac{650}{V}*\frac{2000}{V}}$$
He said he will ask if you have to take the $\log_2$ or not. He also said that the first word will always be the target word (row) and the second word will always be the context (column).