# Edit distance
When you see a mispelled word for instance snowbakl. Did the writer mean snowball or snowplow? Both are valid but if you as a human look at this your intiution will say snowball. Why is this? This can be quantified with the edit distance. 

If you want to go from snowbakl to snowball you need one step but if you want to go from snowbakl to snowplow you need 4 steps. 

(Also sidenote another reason why snowbakl is more likely is that the k is next to the l on an US keyboard which makes it a likely mistake. )

## Transformations 
The steps are called transformations. You get the edit distance by counting the minimum number of needed transformations from one word to another. How are transformations defined? 

- Insert -> Insert a new character. 
- Delete -> Delete a character. 
- Substitue -> Switch a character for another.  

You could also ban subsitutions (and replace them with delete-insert) which basically means subsitutions count for 2 transformation.

## Examples 

![Pasted image 20220217165311](Pasted%20image%2020220217165311.png)

![Pasted image 20220217165328](Pasted%20image%2020220217165328.png)

## How to find the shortest path
This is expressed in dynamic programming. You identify sub problems and then solve those and then combine the solution you found to solve the bigger problem.

The search space is very large, but caching helps, and also you can keep track of the minimum you have found so far and then discard branches that go further than that. 

The in the lecture he gives an algoritm for it:

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

So if the item in the source is the target then move on if its not find out the shortest distance.  

#### Allignment 
To get the best allignment we have to store **back pointers** in each cell, so we know where we came from when we reached a transformation. 

Then we **trace back** our steps and favor the substitution every time we can. 


## Graphically

![Pasted image 20220217170600](Pasted%20image%2020220217170600.png)

\# is the empty string. Moving over the diagonal is a substitution, so you could count this as 2. You can go fast by first only considering the outer layers. This is the simplest where you just go from the empty string to the other word. Then use this information when making decisions. Then when going further the number only goes up if the letter is not the same. If the number is the same the number goes down.

You have to be able to solve problems like this on the exam:

![Pasted image 20220217171236](Pasted%20image%2020220217171236.png)