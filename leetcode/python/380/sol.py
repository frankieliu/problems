
Short code, low memory but slow

https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/85433

* Lang:    python3
* Author:  yorkshire
* Votes:   0

Having seen many solutions use a list and a dictionary I decided to try just using a set.
All works more efficiently apart from the random.sample() method which is incredibly slow in Python compared to using random.randint() to choose an index from a list.
I also tried pop() to get a random item then add it back, but that only chooses an arbitrary item which is not random.
So at least I learned something new. 

```
class RandomizedSet(object):
    def __init__(self):
        self.data = set()

    def insert(self, val):
        if val in self.data:
            return False
        self.data.add(val)
        return True
        
    def remove(self, val):
        if val in self.data:
            self.data.remove(val)
            return True
        return False

    def getRandom(self):
        return random.sample(self.data, 1)[0]
```
