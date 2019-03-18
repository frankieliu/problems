
Python concise solution with dictionary.

https://leetcode.com/problems/contains-duplicate-ii/discuss/61375

* Lang:    python3
* Author:  caikehe
* Votes:   70

        
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False
