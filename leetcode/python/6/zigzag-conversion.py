"""6. ZigZag Conversion
Medium

834

2589

Favorite

Share

The string "PAYPALISHIRING" is written in a zigzag pattern on a given
number of rows like this: (you may want to display this pattern in a
fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
Accepted
268,762
Submissions
899,355

"""

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        slen = len(s)

        if slen <= 1 or numRows == 1:
            return s

        # numRows = n
        midRows = numRows - 2

        # number of distinct spots
        dist = numRows + midRows

        """
        numRows = 4
        P      0 loner
        A   L  1 shares 6
        Y A    2 shares 5
        P      3 loner
        dis

        numRows = 5
        0 loner
        1 shares 7  = 8 - 1
        2 shares 6  = 8 - 2
        3 shares 5  = 8 - 3
        4 loner
        """
        out = ""
        for i in range(0, numRows):

            if i == 0 or i == numRows-1:
                out += s[i::dist]
                # print(i, out)
            else:
                p1 = i
                p2 = dist - i
                # print(p1, s[p1], p2, s[p2])
                tmp = ""
                while True:
                    if p1 <= slen - 1:
                        tmp += s[p1]
                    if p2 <= slen - 1:
                        tmp += s[p2]

                    if p1 >= slen and p2 >= slen:
                        break
                    p1 += dist
                    p2 += dist
                # print(i, tmp)
                out += tmp
        return out


s = Solution()
print(s.convert("ab", 1))
