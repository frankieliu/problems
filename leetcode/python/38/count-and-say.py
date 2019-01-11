"""38. Count and Say
Easy

608

4292

Favorite

Share

The count-and-say sequence is the sequence of integers with the first
five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the
count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a
string.

Example 1:

Input: 1
Output: "1"

Example 2:

Input: 4
Output: "1211"

Accepted
243,600
Submissions
627,855

"""
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        if n == 3:
            return "21"
        if n == 4:
            return "1211"
        if n == 5:
            return "111221"
        if n == 6:
            return "312211"
        prev = self.countAndSay(n-1)

        out = ""
        curr = prev[0]
        count = 1

        for i in range(1, len(prev)):
            if prev[i] == curr:
                count += 1
            else:
                out += "{}{}".format(count, curr)
                curr = prev[i]
                count = 1
        out += "{}{}".format(count, curr)
        return out
