
Python Solution -- Perfect?

https://leetcode.com/problems/friend-circles/discuss/232239

* Lang:    python3
* Author:  anonymous36
* Votes:   0

How can I improve upon my imperfect solution? Thanks in advance?

```
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        
        def findFriendCircle(index, M, visited):
            if index not in visited:
                visited.append(index)
                
            friends = []
            
            for idx in xrange(len(M[index])):
                if idx != index:
                    if M[index][idx] == 1:
                        friends.append(idx)
                        M[index][idx] = 0
                        M[idx][index] = 0
                        
            for i in friends:
                findFriendCircle(i, M, visited)
            
        
        numCircles = 0
        visited = []
        
        for person in xrange(len(M)):
            if person not in visited:
                findFriendCircle(person, M, visited)
                numCircles += 1
        return numCircles
```

Time-Complexity: O(n^2) where n is the number of friends.
Space-Complexity: O(n) where n is the number of friends.
