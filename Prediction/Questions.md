# Questions for the third lecture.

- Can you define symbols?

- Can you explain what sparsity is with probability distributions? 
	- This is that you have many things that don't occur often but because there are many things that don't occur often together they still make up a large part of the probability points. This is basically what uncertainty is.  

- Can you explain why there is more then one BoS and EoS?

	- Can you explain again what you mean that you can only comparing the perplexity of different models if you use the same test set? 
		- I think here the idea is that if you don't have the same test set that you get vastly different perplexity scores not matter what and it becomes meaningless. 
		
		  - Why UNK if you also have dictionaries or lexicons. Can you not just use those to have no need for unk or at least reduce it. Because new words can appear that are not in the lexicon. 
		  - What did you mean by probability mass. 


# Probability mass
There is a certain amount of probability that you can assign to a set of items. So if you have 4 words you can assign 0.25 to each of them. 

Predictions if they are right is great, and we can save energy because we were right. If you get something wrong we have to invest energy to make it right. 

You have one of something, and you can chop it up into infinite pieces, and you have to put the pieces into different bins. 

If you put the same amount into every bin you have maximum entropy!

# Sparsity 
Sparsity is that you have a lot of events that have a low probability of occurring. 

