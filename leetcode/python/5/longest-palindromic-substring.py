"""5. Longest Palindromic Substring
Medium

2762

268

Favorite

Share

Given a string s, find the longest palindromic substring in s. You may
assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
Accepted
435,975
Submissions
1,680,053

"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        slen  = len(s)

        if slen == 0:
            return ""
        if slen == 1:
            return s

        max_palindrome_len = 0
        lbest = 0
        rbest = 0

        # current index to consider as the seed
        seed = 0

        while True:
            el = s[seed]
            print("Considering index", seed, el)

            lptr = seed
            rptr = seed

            # group similar characters together
            while lptr+1 < slen and s[lptr + 1] == el:
                lptr += 1

            # next seed to consider
            seed = lptr + 1

            cur_len = lptr - rptr + 1
            while (
                    lptr+1 < slen and
                    rptr-1 >= 0 and
                    s[lptr+1] == s[rptr-1]
            ):
                lptr += 1
                rptr -= 1
                cur_len += 2

            print("Palindrome:", rptr, lptr, cur_len)

            if cur_len > max_palindrome_len:
                max_palindrome_len = cur_len
                lbest = lptr
                rbest = rptr

            if (
                    seed == slen or
                    slen - seed <= max_palindrome_len // 2
            ):
                break

        return s[rbest:lbest+1]


s = Solution()
print(s.longestPalindrome("aaaabaaa"))
