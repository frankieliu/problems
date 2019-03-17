
Python recursive dfs solution.

https://leetcode.com/problems/n-queens-ii/discuss/20147

* Lang:    python3
* Author:  caikehe
* Votes:   11

The idea here is quite similar to [N-Queens ][1] while we don't need to record the path, and as the return value is a number not a list, it's better to use a global variable to record the result.
       
    def totalNQueens(self, n):
        self.res = 0
        self.dfs([-1]*n, 0)
        return self.res
        
    def dfs(self, nums, index):
        if index == len(nums):
            self.res += 1
            return 
        for i in xrange(len(nums)):
            nums[index] = i
            if self.valid(nums, index):
                self.dfs(nums, index+1)
        
    def valid(self, nums, n):
        for i in xrange(n):
            if nums[i] == nums[n] or abs(nums[n]-nums[i]) == n-i:
                return False
        return True


  [1]: https://leetcode.com/discuss/53764/python-recursive-dfs-solution-with-comments
