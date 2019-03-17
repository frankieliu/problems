
Python clear solution with heap and explanation

https://leetcode.com/problems/k-closest-points-to-origin/discuss/255165

* Lang:    python3
* Author:  fortuna911
* Votes:   0

1. The distance from origin is the Euclidean distance that is \'c\' in  `c^2 = x^2 + y^2` (Pythagorean theorem)
2. Create max heap ordered by distance, and fill it with the first K points
3. Loop over the rest of the points and check for each one: if its distance is smaller than max in heap, extract_max() from heap and push this point

RT: O(K + (P - K) * lg K)
K is for creating initial heap
For the remaining (P - K) points, we may do that many calls to extract_Max() (lg K)

Spc: O(K)

```
from math import sqrt
from heapq import heappush, heappop

class HeapElem:
    def __init__(self, dist, point):
        self.dist = dist
        self.point = point
        
    def __lt__(self, other):
        return self.dist < other.dist

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        # Put first K elements into heap.
        for i in range(0, K):
            heappush(heap, HeapElem(-get_dist(points[i]), points[i]))
            
        for i in range(K, len(points)):
            dist = get_dist(points[i])
            # If dist is less than the max we have in heap, replace the max
            # with this smaller distance.
            if dist < -heap[0].dist:
                heappop(heap)
                heappush(heap, HeapElem(-dist, points[i]))
        return [elem.point for elem in heap]
                
def get_dist(p):
    x = p[0]
    y = p[1]
    return sqrt(x**2 + y**2)
```
