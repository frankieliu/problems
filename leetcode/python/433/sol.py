
Python Solution using BFS

https://leetcode.com/problems/minimum-genetic-mutation/discuss/91489

* Lang:    python3
* Author:  lee12jin
* Votes:   6

```
import collections

def viableMutation(current_mutation, next_mutation):
    changes = 0
    for i in xrange(len(current_mutation)):
        if current_mutation[i] != next_mutation[i]:
            changes += 1
    return changes == 1

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        queue = collections.deque()
        queue.append([start, start, 0]) # current, previous, num_steps
        while queue:
            current, previous, num_steps = queue.popleft()
            if current == end:  # in BFS, the first instance of current == end will yield the minimum
                return num_steps
            for string in bank:
                if viableMutation(current, string) and string != previous:
                    queue.append([string, current, num_steps+1])
        return -1
```
