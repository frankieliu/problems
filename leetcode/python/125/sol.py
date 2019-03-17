
Python in-place two-pointer solution.

https://leetcode.com/problems/valid-palindrome/discuss/39982

* Lang:    python3
* Author:  caikehe
* Votes:   74

        
    def isPalindrome(self, s):
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l <r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1; r -= 1
        return True
