
Concise Python solution with List, Dict and Set

https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/discuss/85611

* Lang:    python3
* Author:  o_sharp
* Votes:   2

This solution assumes there is not ordering requirement for ```remove```. ```remove``` will randomly remove an element among duplicates.

Similar to Problem 380 without duplicates, we use a list to contain all elements and use a dict to keep track of their indices. This time, we use a ```set``` to keep track of all indices for a value.

Just like Problem 380, when we remove a value, we randomly pop an index for that value from the set, swap the value with the last element of the list, and update the indices for the new value.

```
import random
class RandomizedCollection(object):

    def __init__(self):
        self.l, self.d = [], collections.defaultdict(set)

    def insert(self, val):
        self.d[val].add(len(self.l))
        self.l.append(val)
        return len(self.d[val])==1

    def remove(self, val):
        if val not in self.d:
            return False
        i, newVal = self.d[val].pop(), self.l[-1]
        len(self.d[val]) > 0 or self.d.pop(val, None)
        if newVal in self.d:
            self.d[newVal] = (self.d[newVal] | {i}) - {len(self.l)-1}
        self.l[i] = newVal
        self.l.pop()
        return True

    def getRandom(self):
        return random.choice(self.l)
```
Longer but clearer version:

```
import random
class RandomizedCollection(object):
    def __init__(self):
        self.l = []
        self.d = collections.defaultdict(set)

    def insert(self, val):
        b = val not in self.d
        self.d[val].add(len(self.l))
        self.l.append(val)
        return b

    def remove(self, val):
        if val not in self.d:
            return False
        i, newVal = self.d[val].pop(), self.l[-1]
        if len(self.d[val]) == 0:
            del self.d[val]
        self.l[i] = newVal
        if newVal in self.d:
            self.d[newVal].add(i)
            self.d[newVal].discard(len(self.l)-1)
        self.l.pop()
        return True

    def getRandom(self):
        return random.choice(self.l)
```
