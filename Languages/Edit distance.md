# Edit distance 

When you see a mispeled word, for instance snowbakl. Did the writer mean snowball or snowplow? Both are valid, but if you as a human look at this your intuition will say snowball. Why is this? This can be quantified with the edit distance. 

If you want to go from snowbakl to snowball you need one step, but if you want to go from snowbakl to snowplow you need 4 steps. 

> Another reason why snowbakl is more likely is that the k is next to the l on a US keyboard, which makes it a likely mistake. 

## Transformations 
The steps are called transformations. You get the edit distance by counting the minimum number of needed transformations from one word to another. How are transformations defined? 

- Insert → Insert a new character. 
- Delete → Delete a character. 
- Substitute → Switch a character for another.  

You could also ban substitutions (and replace them with delete-insert) which basically means substitutions count for 2 transformation.

![Edit distance alignment example](../images/Pasted%20image%2020220217165311.png)

![Edit distance example](../images/Pasted%20image%2020220217165328.png)

## How to find the shortest path

This is expressed in dynamic programming. You identify sub problems and then solve those, and then combine the solution you found to solve the bigger problem.

The search space is very large, but caching helps, and also you can keep track of the minimum you have found so far and then discard branches that go further than that. 

The in the lecture he gives an algorithm for it:

```python
def D(source: str, target: str) -> int:
	for i in range(len(source)):
		for j in range(len(target)):
	    	if source[i] != target[j]:
				D(i, j) = 1 + arrgmin( D(i-1), D(i-1, j-1), D(i, j-1))
			else:
				D(i,j) = D(i-1, j-1)
	return D(n,m)
```

So if the item in the source is the target then move on if it's not, find out the shortest distance.  

#### Alignment 
To get the best alignment, we have to store **back pointers** in each cell, so we know where we came from when we reached a transformation. 

Then we **trace back** our steps and favour the substitution every time we can. 


## Graphically

![Edit distance shortest path](../images/Pasted%20image%2020220217170600.png)

The # is the empty string. Moving over the diagonal is a substitution, so you could count this as 2. You can go fast by first only considering the outer layers. This is the simplest, where you just go from the empty string to the other word. Then use this information when making decisions. Then, when going further, the number only goes up if the letter is not the same. If the number is the same, the number goes down.

You have to be able to solve problems like this on the exam:

![Edit distance challenge](../images/Pasted%20image%2020220217171236.png)

## Minimum Edit distance full tutorial:

f3 help: edit distence, editdistance, edit distanse, edit distense, minimum edit distense

We will now calculate the edit distance from Dirt to Flirt.

### Steps

1. Get cost for Insert, Delete, Substitute (given in the question)
2. Make a table with one word on top and one on the left one letter in each cell. Starting with the empty string (#)

|     | #   | D   | I   | R   | T   | 
|-----|-----|-----|-----|-----|-----|
| #   |     |     |     |     |     |
| F   |     |     |     |     |     |
| L   |     |     |     |     |     |
| I   |     |     |     |     |     |
| R   |     |     |     |     |     |
| T   |     |     |     |     |     |

3. Now we have to fill everywhere how many actions it takes. Start with the first row and column. The first is from the empty string, so it starts at 0 (actions to go from # to # is 0) going up by 1. So from # to D is 1, from # to DI is 2 etc.

With Flirt, you are deleting letters. With Dirt, you are inserting letters. So you have to delete 3 letters from FLI to get to #.

| x   | #   | D   | I   | R   | T   | 
|-----|-----|-----|-----|-----|-----|
| #   |  0  | 1   | 2   | 3   | 4   |
| F   |  1  |     |     |     |     |
| L   |  2  |     |     |     |     |
| I   |  3  |     |     |     |     |
| R   |  4  |     |     |     |     |
| T   |  5  |     |     |     |     |

Ok now we do the column with D at the top. Look at the empty cell and ask these questions:

- Are the two letters different? (Yes D != F).
  - If they are different, look at the cell to the left, above left diagonal and above. So that is: [1,0,1] Take the minimum value = 0, add 1. 
  - If the minimum came from above left diagonal it is a substitution, and you add another 1 (This is a choice, cost of substitution, be sure to read the question if it is required).
  - So 0 + 1 + 1 = 2 

| x   | #   | D   | I   | R   | T   | 
|-----|-----|-----|-----|-----|-----|
| #   |  0  | 1   | 2   | 3   | 4   |
| F   |  1  | 2   |     |     |     |
| L   |  2  |     |     |     |     |
| I   |  3  |     |     |     |     |
| R   |  4  |     |     |     |     |
| T   |  5  |     |     |     |     |

Now repeat for next cell down (L,D):
- Are they the same? No
    - If no take minimum of above cell, left cell, up, left diagonal cell = 1
    - Add 1, so 1 + 1 and add another one because the min was the diagonal so 1 + 1 + 1 = 3 

| x   | #   | D   | I   | R   | T   | 
|-----|-----|-----|-----|-----|-----|
| #   |  0  | 1   | 2   | 3   | 4   |
| F   |  1  | 2   |     |     |     |
| L   |  2  | 3   |     |     |     |
| I   |  3  |     |     |     |     |
| R   |  4  |     |     |     |     |
| T   |  5  |     |     |     |     |

Now one more:

Cell: I,D, same? no
- min(3,2,3) = 2
- was min diagonal? 
	- yes?, add 2
    - no?, add 1
- 2 + 2 = 4

| x   | #   | D   | I   | R   | T   | 
|-----|-----|-----|-----|-----|-----|
| #   |  0  | 1   | 2   | 3   | 4   |
| F   |  1  | 2   |     |     |     |
| L   |  2  | 3   |     |     |     |
| I   |  3  | 4   |     |     |     |
| R   |  4  |     |     |     |     |
| T   |  5  |     |     |     |     |

I am going to continue now till we hit a case where the letter is the same:

| x   | #   | d   | i   | r   | t   | 
|-----|-----|-----|-----|-----|-----|
| #   |  0  | 1   | 2   | 3   | 4   |
| f   |  1  | 2   | 3   |     |     |
| l   |  2  | 3   | 4   |     |     |
| i   |  3  | 4   |     |     |     |
| r   |  4  | 5   |     |     |     |
| t   |  5  | 6   |     |     |     |

Now we have I,I these are the same.
In this case, just copy the value from above left diagonal cell!

| x   | #   | d   | i   | r   | t   | 
|-----|-----|-----|-----|-----|-----|
| #   |  0  | 1   | 2   | 3   | 4   |
| f   |  1  | 2   | 3   |     |     |
| l   |  2  | 3   | 4   |     |     |
| i   |  3  | 4   | 3   |     |     |
| r   |  4  | 5   |     |     |     |
| t   |  5  | 6   |     |     |     |

The **minimum edit distance** is the value of the bottom right cell.

To get the best alignment, you need to store where you came from every time. You can also do it by looking at the best path, working back. Basically you can only go to cells up, left, left up diagonal from the bottom right cell if they have a lower value then the current cell. So with this cell I, I you can only go to l,d (to get the best alignment). When working back, you always prioritize diagonal to go back.

Ok next one:

| x   | #   | d   | i   | r   | t   | 
|-----|-----|-----|-----|-----|-----|
| #   |  0  | 1   | 2   | 3   | 4   |
| f   |  1  | 2   | 3   |     |     |
| l   |  2  | 3   | 4   |     |     |
| i   |  3  | 4   | 3   |     |     |
| r   |  4  | 5   |     |     |     |
| t   |  5  | 6   |     |     |     |

- Cell: i,r
- Same? no
- min(5,4,3) = 3
  - was min diagonal? 
    - yes?, add 2
    - no?, add 1
- 3 + 1 = 4 


| x   | #   | d   | i   | r   | t   | 
|-----|-----|-----|-----|-----|-----|
| #   |  0  | 1   | 2   | 3   | 4   |
| f   |  1  | 2   | 3   |     |     |
| l   |  2  | 3   | 4   |     |     |
| i   |  3  | 4   | 3   |     |     |
| r   |  4  | 5   | 4   |     |     |
| t   |  5  | 6   |     |     |     |

Ok now I will fill in the whole thing:

| x   | #   | d   | i   | r   | t   | 
|-----|-----|-----|-----|-----|-----|
| #   |  0  | 1   | 2   | 3   | 4   |
| f   |  1  | 2   | 3   | 4   | 5   |
| l   |  2  | 3   | 4   | 5   | 6   |
| i   |  3  | 4   | 3   | 4   | 5   |
| r   |  4  | 5   | 4   | 3   | 4   |
| t   |  5  | 6   | 5   | 4   | 5   |

See the image above for how to work back. 

Be sure to check the question if substitution has a cost of 2! 

--- 

With Growing and Glowing you get this:

| X   | #   | G   | r   | o   | w   | i   | n   | g   |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| #   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| G   | 1   | 0   | 1   | 2   |     |     |     |     |
| l   | 2   | 1   | 2   | 3   |     |     |     |     |
| o   | 3   | 2   | 3   | 2   |     |     |     |     |
| w   | 4   | 3   | 4   |     |  2  |     |     |     |
| i   | 5   | 4   | 5   |     |     | 2   |     |     |
| n   | 6   | 5   | 6   |     |     |     | 2   |     |
| g   | 7   | 6   | 7   |     |     |     |     | 2   |

Subs count for 2.

You know that it will be 2, and you can skip a lot because the rest of the word matches. Marking matching cells beforehand can help. 
