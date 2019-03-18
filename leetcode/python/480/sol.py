
python MinHeap allow remove operation

https://leetcode.com/problems/sliding-window-median/discuss/96359

* Lang:    python3
* Author:  yawnzheng
* Votes:   1

We can maintain a dict to store valid items and its count, when we pop or peek an item, if that item is invalid(not in the dict), we just discard it till we get a valid one. When remove an item, we decrease its count. If the count reaches zero, remove the item from the dict.

We could use this data struct to solve this problem.
```
from heapq import *
from collections import defaultdict
class Heap(object):
    def __init__(self):
        self._counter = defaultdict(int)
        self._heap = []
        self._size = 0

    def push(self, x):
        heappush(self._heap, x)
        self._counter[x] += 1
        self._size += 1

    def pop(self):
        while self._heap[0] not in self._counter:
            heappop(self._heap)
        x = heappop(self._heap)
        self._counter[x] -= 1
        if self._counter[x] <= 0:
            del self._counter[x]
        self._size -= 1
        return x

    def peek(self):
        while self._heap[0] not in self._counter:
            heappop(self._heap)
        return self._heap[0]

    def remove(self, x):
        if x in self._counter:
            self._counter[x] -= 1
            self._size -= 1
            if self._counter[x] == 0:
                del self._counter[x]

    def contains(self, x):
        return x in self._counter

    def size(self):
        return self._size
```
