#
# @lc app=leetcode id=284 lang=python3
#
# [284] Peeking Iterator
#
# https://leetcode.com/problems/peeking-iterator/description/
#
# algorithms
# Medium (38.88%)
# Total Accepted:    69K
# Total Submissions: 177.4K
# Testcase Example:  '["PeekingIterator","next","peek","next","next","hasNext"]\n[[[1,2,3]],[],[],[],[],[]]'
#
# Given an Iterator class interface with methods: next() and hasNext(), design
# and implement a PeekingIterator that support the peek() operation -- it
# essentially peek() at the element that will be returned by the next call to
# next().
#
# Example:
#
#
# Assume that the iterator is initialized to the beginning of the list:
# [1,2,3].
#
# Call next() gets you 1, the first element in the list.
# Now you call peek() and it returns 2, the next element. Calling next() after
# that still return 2.
# You call next() the final time and it returns 3, the last element.
# Calling hasNext() after that should return false.
#
#
# Follow up: How would you extend your design to be generic and work with all
# types, not just integer?
#
#
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peeked = False
        self.pval = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peeked:
            # takes care of consecutive peeked
            pass
        else:
            if self.iterator.hasNext():
                self.peeked = True
                self.pval = self.iterator.next()
            else:
                self.peeked = False
                self.pval = None

        return self.pval

    def next(self):
        """
        :rtype: int
        """
        if self.peeked:
            self.peeked = False
            out = self.pval
            self.pval = None
            return out
        else:
            return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peeked:
            return True
        else:
            return self.iterator.hasNext()


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].


test = True
if test:

    class hn_wrapper(object):
      def __init__(self, it):
        self.it = iter(it)
        self._hasnext = None
      def __iter__(self): return self
      def next(self):
        if self._hasnext:
          result = self._thenext
        else:
          result = next(self.it)
        self._hasnext = None
        return result
      def hasNext(self):
        if self._hasnext is None:
          try: self._thenext = next(self.it)
          except StopIteration: self._hasnext = False
          else: self._hasnext = True
        return self._hasnext

    a = [0,1,2,3,4,5]
    pitr = PeekingIterator(hn_wrapper(iter(a)))
    print(pitr.next())
    print(pitr.peek())
    print(pitr.next())
    print(pitr.peek())
    print(pitr.hasNext())
    print(pitr.next())
    print(pitr.peek())
    print(pitr.hasNext())
    print(pitr.peek())
    print(pitr.next())
    print(pitr.hasNext())
    print(pitr.peek())
    print(pitr.next())
    print(pitr.hasNext())
    print(pitr.peek())
    print(pitr.next())
    print(pitr.hasNext())
    # b = iter(a)
    # print(next(b))
    # print(b.hasNext())
