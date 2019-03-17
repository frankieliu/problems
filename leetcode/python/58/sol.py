
My 36 ms Python solution

https://leetcode.com/problems/length-of-last-word/discuss/21961

* Lang:    python3
* Author:  jonneff
* Votes:   12


    def lengthOfLastWord(self, s):
        ls = len(s)
        # slow and fast pointers
        slow = -1
        # iterate over trailing spaces
        while slow >= -ls and s[slow] == ' ':
            slow-=1
        fast = slow
        # iterate over last word
        while fast >= -ls and s[fast] != ' ':
            fast-=1
        return slow - fast
