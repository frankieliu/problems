
Simple Python solution (DFS).

https://leetcode.com/problems/permutations/discuss/18296

* Lang:    python3
* Author:  caikehe
* Votes:   116

        
    # DFS
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in xrange(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
