
A Python solution - 85ms - O(n)

https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1731

* Lang:    python3
* Author:  Google
* Votes:   179

    class Solution:
        # @return an integer
        def lengthOfLongestSubstring(self, s):
            start = maxLength = 0
            usedChar = {}
            
            for i in range(len(s)):
                if s[i] in usedChar and start <= usedChar[s[i]]:
                    start = usedChar[s[i]] + 1
                else:
                    maxLength = max(maxLength, i - start + 1)
    
                usedChar[s[i]] = i
    
            return maxLength
