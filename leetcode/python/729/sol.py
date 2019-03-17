
Binary Search Python with Explanations

https://leetcode.com/problems/my-calendar-i/discuss/109477

* Lang:    python3
* Author:  flamesofmoon
* Votes:   4

My `self.intervals` is a sorted list of real numbers in which I store the following intervals:

`[self.intervals[0], self.intervals[1])`, `[self.intervals[2], self.intervals[3])`, etc.

So I do a binary search to check if I can insert and insert when possible. Meanwhile, I hope the list insertion is optimized through some sort of linked list ideas (on which I have zero knowledge).

If anyone knows how this part of  `list` is implemented in Python, please let me know! I appreciate it!

Btw, it would be theoretically optimal to use some sort of self-balancing binary search tree, like red-black tree. But since `list` object is so optimized, I don't think red-black tree can outrun this code unless the data is really really HUGE.

```
    def __init__(self):
        self.intervals = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if end <= start:
            return False
        
        i = bisect.bisect_right(self.intervals, start)
        if i % 2:            # start is in some stored interval
            return False
        
        j = bisect.bisect_left(self.intervals, end)
        if i != j:
            return False
        
        self.intervals[i:i] = [start, end]
        return True
```
