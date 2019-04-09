
Python solution

https://leetcode.com/problems/reverse-words-in-a-string-ii/discuss/53832

* Lang:    python3
* Author:  autekwing
* Votes:   29

reverse the whole string and then reverse words by words

    def reverseWords(self, s):
        self.reverse(s, 0, len(s) - 1)
        
        beg = 0
        for i in xrange(len(s)):
            if s[i] == ' ':
                self.reverse(s, beg, i-1)
                beg = i + 1
            elif i == len(s) -1:
                self.reverse(s, beg, i)
    
    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
