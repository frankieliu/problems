
Python solution using deque, beats 94%, for any number of baskets

https://leetcode.com/problems/fruit-into-baskets/discuss/254231

* Lang:    python3
* Author:  Lunluen
* Votes:   0

Hope my code is clear enough.
Pitful: worst case time complexity is O(nm)
n: length of the row
m: number of baskets

```Python
import queue


BASKETS = 2


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        largest = 0  # The largest in history.
        ntotal = 0  # The current amount of total fruits.
        nlast = 0  # The current amount of the last repeated fruits.
        
        dq = queue.deque(maxlen=BASKETS)
        
        for fruit in tree:
            if fruit in dq:
                ntotal += 1
                if fruit != dq[-1]:
                    nlast = 1
                    dq.remove(fruit)
                    dq.append(fruit)
                else:
                    nlast += 1
            else:
                ntotal = nlast + 1
                nlast = 1
                dq.append(fruit)  # dq will popleft if it\'s full.
            
            if ntotal > largest:
                largest = ntotal
        return largest
```
