
Simple Python Solution

https://leetcode.com/problems/peeking-iterator/discuss/72626

* Lang:    python3
* Author:  softray
* Votes:   47

Store the next value outside the iterator.  When next is called return the stored value and populate with next value from iterator.

    class PeekingIterator(object):
        def __init__(self, iterator):
            self.iter = iterator
            self.temp = self.iter.next() if self.iter.hasNext() else None
    
        def peek(self):
            return self.temp
    
        def next(self):
            ret = self.temp
            self.temp = self.iter.next() if self.iter.hasNext() else None
            return ret
    
        def hasNext(self):
            return self.temp is not None
