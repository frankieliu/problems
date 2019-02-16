"""387. First Unique Character in a String
Virtual User Accepted: 76
Virtual User Tried: 86
Virtual Total Accepted: 76
Virtual Total Submissions: 86
Difficulty: Easy

Given a string, find the first non-repeating character in it and
return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

"""

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        se = [list(reversed(x)) for x in enumerate(s)]
        k = sorted(se)

        k.append(['$', 0])
        best = len(s)
        j = 0
        while j < len(s):
            # print("comparing", k[j][0], k[j+1][0], best)
            if k[j][0] != k[j+1][0]:
                if k[j][1] < best:
                    best = k[j][1]
            else:
                while k[j][0] == k[j+1][0]:
                    j += 1
            j += 1

        # print(best)
        if best == len(s):
            best = -1
        return best

from collections import defaultdict

s = Solution()
print(s.firstUniqChar("asdfsagdfss"))
