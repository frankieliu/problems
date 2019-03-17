
My accepted python code via while loop

https://leetcode.com/problems/remove-duplicates-from-sorted-array/discuss/12123

* Lang:    python3
* Author:  liyun1988
* Votes:   6

    class Solution:
    # @param a list of integers
    # @return an integer
    
    def removeDuplicates(self, A):
        if not A:
            return 0
        else:
            ii,jj=1,1
            while jj<len(A):
                if A[ii-1]!=A[jj]:
                    A[ii]=A[jj]
                    ii+=1
                jj+=1
            return ii

the code use a while loop with two indexes ii and jj. jj went through all elements in A and ii is used to record non-duplicated elements in A. Any comments would be appreciated
