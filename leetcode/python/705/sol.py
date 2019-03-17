
[Solution] Python2 with Open Addressing (120ms, faster than 80.11%, 13.1 MB, less than 65.8 %)

https://leetcode.com/problems/design-hashset/discuss/233689

* Lang:    python3
* Author:  idawatibustan
* Votes:   0

Took me a long time to debug my own code and pass all the test. Please give feedback for my implementation :)

Runtime: 120 ms, faster than 80.11% of Python online submissions for Design HashSet.
Memory Usage: 13.1 MB, less than 65.80% of Python online submissions for Design HashSet.

``` python
class MyHashSet(object):

    def __init__(self):
        """
        Initialize list and size
        """
        self.my_list = [None]*10000
        self.size = 0

        
    def hash_key(self, key):
        temp_key = key
        h_key = 0
        while temp_key > 0:
            h_key += temp_key % 10000
            temp_key = temp_key / 10000
        return h_key % 10000

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        h_key = self.hash_key(key)
        while not self.my_list[h_key] is None:
            h_key = (h_key+1) % 10000
        self.my_list[h_key] = key
        self.size += 1


    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        h_key = self.hash_key(key)
        if self.my_list[h_key] is None:
            return
        while not self.my_list[h_key] is None:
            if self.my_list[h_key] != key:
                h_key = (h_key+1) % 10000
            else:
			    # keep searching in case earlier collision was deleted
                self.my_list[h_key] = -1
                self.size -= 1


    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        h_key = self.hash_key(key)
        if self.my_list[h_key] is None:
            return False
        while not self.my_list[h_key] is None:
            if self.my_list[h_key] != key:
                h_key = (h_key+1) % 10000
            else:
                return True
        return False
```

