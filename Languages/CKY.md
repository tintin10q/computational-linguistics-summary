# CKY algorithm 
The CKV algorithm is a dynamic programming solution to parsing [Context free grammars](Context%20free%20grammars.md). 

## Pseudocode

```python
def CKYparser(string, grammar):
	for j in 1:length(string)  
		for all rules A | A→s[j] ∊ℒ  
			table[j-1,j] = table[j-1,j] ⋃A  
		for i in reverse(0:j-2):  
			for k in i+1:j-1  
				for all rules A→BC ∊ ℒ and B ∊ table[i,k] and C ∊ table[k,j]  
					table[i,j] = table[i,j] ⋃A  
	return table
```

## Actual python function

```python
def CKYparser(string: str, grammar: 'Grammar') -> list[list[str]]:
	table = [[for i in range(len(string))] for i in range(len(string))]
	rules = grammar.rules
	for j in range(1, len(string)):
		for rule in rules:
			table[j-1,j] = table[j-1,j] or A
		for i in reverse(range(0,j-2)):
			for k in range(i+1, j-1):
				for rule in rules:
					for B, C in table[i,k], table[k,j]:
						table[i,j] = table[i,j] or A
	return table
```

Don’t reinvent the wheel! Use existing and optimized libraries to do statistical language modelling, for instance like KenLM.
## Tutorial 

### A grammar
This grammar is in [Chomsky Normal Form](Chomsky%20Normal%20Form.md):

- S → AB | BC
- A → BA | a
- B → CC | b
- C → AB | a

Can we get to S from abba? 

Yes!

So we have a table with a row for each input string. So let's take input = abba

|     | a   | b   | b   | a   |
| --- | --- | --- | --- | --- |
| X   |     |     |     |     |
| X   | X   |     |     |     |
| X   | X   | X   |     |     |
| X   | X   | X   | X   |     |
| X   | X   | X   | X   | X   |


What are the rules where a appears on the right side?
This is A and C. So we fill these non-terminals into the table.

|     | a   | b   | b   | a   |
| --- | --- | --- | --- | --- |
| x   | A,C |     |     |     |
| X   | X   |     |     |     |
| X   | X   | X   |     |     |
| X   | X   | X   | X   |     |
| X   | X   | X   | X   | X   |

Now we do the same for b.

|     | a   | b   | b   | a   |
| --- | --- | --- | --- | --- |
| x   | A,C |     |     |     |
| X   | X   | B    |     |     |
| X   | X   | X   |     |     |
| X   | X   | X   | X   |     |
| X   | X   | X   | X   | X   |

Now you want to put in the cell between the cell with A, C and B the rules that contain combinations of those non-terminals on the right-hand side. The possible combinations are: AB and CB. The thing to the left has to come first. Now we basically try to find a constituent of a and b.

The possibilities are S and C so let's fill it in.

|     | a   | b   | b   | a   |
| --- | --- | --- | --- | --- |
| x   | A,C | S,C |     |     |
| x   | x   | b   |     |     |
| x   | x   | x   |     |     |
| x   | x   | x   | x   |     |
| x   | x   | x   | x   | x   |

Now the bottom of the next row is B again just like before. This is the only non-terminal that can come from b. 

|     | a   | b   | b   | a   |
| --- | --- | --- | --- | --- |
| x   | A,C | S,C |     |     |
| x   | x   | b   |     |     |
| x   | x   | x   | b   |     |
| x   | x   | x   | x   |     |
| x   | x   | x   | x   | x   |

But now we have to fill in the things above the b in the row. To do this, we only look at the cell directly 1 up from the last be we did. So we only look at the cell marked K now.  

|     | a    | b   | b   | a   |
| --- | ---- | --- | --- | --- |
| x   | A, C | S,C |     |     |
| x   | x    | B   | K   |     |
| x   | x    | x   | B   |     |
| x   | x    | x   | x   |     |
| x   | x    | x   | x   | x   |

If we do this, we can repeat what we did before and look at sequences of non-terminals in the grammar of BB. If we found this non-terminal, you would fill it in and move one cell up in the row. Do you feel the abstraction building? There is no BB, so we put empty set (∅). 


|     | a    | b    | b   | a   |
| --- | ---- | ---- | --- | --- |
| x   | A, C | S, C |     |     |
| x   | x    | B    | ∅   |     |
| x   | x    | x    | B   |     |
| x   | x    | x    | x   |     |
| x   | x    | x    | x   | x   |

Now we move up again. However, now we have to combine this cell with a lot of other cells because if you look from the right then you do include the whole column. Because basically the lowest cell in the second b row is saying we can rewrite b to B. Then the one above that says can we rewrite BB? No. The one above that should look for SB or CB. Because you try to rewrite what came before. However, SB or CB do not exist in the grammar, so it is empty set again. 

|     | a    | b    | b   | a   |
| --- | ---- | ---- | --- | --- |
| x   | A, C | S, C | ∅   |     |
| x   | x    | B    | ∅   |     |
| x   | x    | x    | B   |     |
| x   | x    | x    | x   |     |
| x   | x    | x    | x   | x   |

Now we can basically fill in the table. The first is simple, how can you write a. We already did this.  

|     | a    | b    | b           | a   |
| --- | ---- | ---- | ----------- | --- |
| x   | A, C | S, C | ∅ |     |
| x   | x    | B    | ∅ |     |
| x   | x    | x    | B           |     |
| x   | x    | x    | x           | A, C | 
| x   | x    | x    | x           | x   |

Then the cell above it looks for BA or BC. BA occurs in A and BC occurs in S. So we write S and A. 

|     | a    | b    | b   | a    |
| --- | ---- | ---- | --- | ---- |
| x   | A, C | S, C | ∅   |      |
| x   | x    | B    | ∅   |      |
| x   | x    | x    | B   | S, A |
| x   | x    | x    | x   | A,C  |
| x   | x    | x    | x   | x    |

For the next one, we check BS and BA. BA occurs in A and BS does not occur.  So we put A. So we looked at marked cells.

|     | a    | b              | b   | a                 |
| --- | ---- | -------------- | --- | ----------------- |
| x   | A, C | S, C           | ∅   |                   |
| x   | x    | <mark>B</mark> | ∅   | A                 |
| x   | x    | x              | B   | <mark>S, A</mark> |
| x   | x    | x              | x   | A,C               |
| x   | x    | x              | x   | x                 |

For the last one, we have to check all the cells in the top row with A. 

So we check for AA, CA, SA and CA. All these rules do not occur, so its $\emptyset$

|     | a    | b    | b   | a    |
| --- | ---- | ---- | --- | ---- |
| x   | A, C | S, C | ∅   | ∅    |
| x   | x    | B    | ∅   | A    |
| x   | x    | x    | B   | S, A | 
| x   | x    | x    | x   | A,C  |
| x   | x    | x    | x   | x    |

We conclude that the word is not in the language. 


![Pasted image 20220314195726](../images/Pasted%20image%2020220314195726.webp)
