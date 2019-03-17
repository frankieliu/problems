
Using Set to beat the counter approach

https://leetcode.com/problems/n-repeated-element-in-size-2n-array/discuss/249432

* Lang:    python3
* Author:  Sandip13
* Votes:   0

/* using the Counter approach, running time :80ms */
```
import collections
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        self.A = A
        
        count = collections.Counter(A)
        for k in count:
            if count[k]>1:
                return k
				****
my_obj = Solution()
print (my_obj.repeatedNTimes([10,3,2,4,2]))
```

/* now using set we can improve the running time being 20ms */

```
class Solution(object):
  def repeatedNTimes(self,A):
    self.A = A

    emptySet = set()
    for i in A:
      if i in emptySet:
        return i
      else:
        emptySet.add(i)
        
my_obj = Solution()
print (my_obj.repeatedNTimes([10,3,2,4,2]))
```
