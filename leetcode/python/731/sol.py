
Python Binary Search with Explanations

https://leetcode.com/problems/my-calendar-ii/discuss/109538

* Lang:    python3
* Author:  flamesofmoon
* Votes:   2

I notice that @awice already have a somewhat similar post [here](https://discuss.leetcode.com/topic/111220/n-2-python-short-and-elegant). Mine is hopefully optimized among all O(n^2) algorithms. Yeah, it is still O(n^2) (since there are insertions) but faster than looping over the whole list.

As said in the code, `self.two` are intervals that are booked twice. `self.one` are intervals that are booked at least once. They are both increasing lists of real numbers. 

In `self.two` the stored intervals are
`[self.two[0], self.two[1])`, `[self.two[2], self.two[3])`, etc.
The same notation for `self.one`.

With `self.two` in hand, I use `self.is_valid` to check whether it is possible to add the current interval. This part is just copied from Calendar I problem.

Then the rest is to update the current lists using indices from the binary searches. It takes some time to clarify, but once the pattern is found, it is pretty easy. I write this part in a lengthy manner just to articulate the pattern.

Sadly it is hard to generalize this code to k overlapping case. I have an idea for the generalization though, and it only takes O(n^2) and is independent of k. I would be willing to share if there were any interest.

```
class MyCalendarTwo(object):

    def __init__(self):
        self.one = []  # intervals that are booked at least once
        self.two = []  # intervals that are booked twice
        
    def is_valid(self, start, end):
        """
        check if it is valid to insert into self.two
        return -1 or the index of the insertion place
        """
        if end <= start:
            return -1
        
        i = bisect.bisect_right(self.two, start)
        if i % 2:
            return -1
        
        j = bisect.bisect_left(self.two, end)
        if i != j:
            return -1
        
        return i
    
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        t = self.is_valid(start, end)  
        if t == -1:
            return False
        # t will be the insertion position in self.two

        i = bisect.bisect_right(self.one, start)
        j = bisect.bisect_left(self.one, end)
        
        if i % 2: 
            if j % 2:  # when both start and end is inside some intervals in self.one
                self.two[t:t] = [start] + self.one[i:j] + [end]
                self.one[i:j] = []
            else:      # when start is and end is not
                self.two[t:t] = [start] + self.one[i:j]
                self.one[i:j] = [end]
        else:
            if j % 2:  # when start is not and end is
                self.two[t:t] = self.one[i:j] + [end]
                self.one[i:j] = [start]
            else:      # when neither start nor end is
                self.two[t:t] = self.one[i:j]
                self.one[i:j] = [start, end]
                
        return True
```
