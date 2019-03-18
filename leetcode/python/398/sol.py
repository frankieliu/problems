
Memoization in python - detailed explanation with video

https://leetcode.com/problems/random-pick-index/discuss/88086

* Lang:    python3
* Author:  3v3rgr33n
* Votes:   0

### VIDEO EXPLANATION
This is deeply explained in [this youtube video](https://youtu.be/xxecnYsyAdo), but you can find the summary below

### Trivial, Broute-force solution
* In `__init__` constructor - do nothing special, just store nums in self.nums
* In `pick()` - do 3 things:
  1. get the `count` of elements which match `target`
  1. find the `random` integer in the `range(count)`, from 0 to `count`, not including `count`
  1. return the index of `random`th occurrence of `target` in the array

### Sightly optimized solution with memoization
if `pick()` is called multiple times with same values of `target`, then we don't need to re-calculate `count` each time. It's better to store it in a hash entry `hash[target]` after we did it first time, and on any following call to `pick()` - just return `hash[target]` if it's present.

### Solution
```
from random import randrange
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.memoCounts = {}
        self.nums = nums

    def getCount(self, target):
        # O(n)
        if target in self.memoCounts:
            return self.memoCounts[target]
            
        count = 0
        for el in self.nums:
            if el == target:
                count += 1
        self.memoCounts[target] = count
        return count
        
    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count = self.getCount(target)
        randIndex = randrange(count) # [0...count)
        targetIndex = 0

        for i in xrange(len(self.nums)):
            if self.nums[i] == target:
                if targetIndex == randIndex:
                    return i
                targetIndex += 1
        
        return "bla"
```

### FINAL THOUGHTS
I hope that [the video](https://youtu.be/xxecnYsyAdo) was not too boring and long, but I made it to explain the whole process of solving this task as if you were coding on a whiteboard. This can be helpful for those who goes to onsite interviews soon. Anyways, please, leave comments here or below the video if you have them - I'll answer and improve! Good luck!
