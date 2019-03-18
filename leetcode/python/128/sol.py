
Python O(n) solution using sets

https://leetcode.com/problems/longest-consecutive-sequence/discuss/41202

* Lang:    python3
* Author:  yawnzheng
* Votes:   18

    class Solution:
        # @param num, a list of integer
        # @return an integer
        def longestConsecutive(self, num):
            num=set(num)
            maxLen=0
            while num:
                n=num.pop()
                i=n+1
                l1=0
                l2=0
                while i in num:
                    num.remove(i)
                    i+=1
                    l1+=1
                i=n-1
                while i in num:
                    num.remove(i)
                    i-=1
                    l2+=1
                maxLen=max(maxLen,l1+l2+1)
            return maxLen
