#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#
# https://leetcode.com/problems/fraction-to-recurring-decimal/description/
#
# algorithms
# Medium (19.04%)
# Total Accepted:    81K
# Total Submissions: 425.6K
# Testcase Example:  '1\n2'
#
# Given two integers representing the numerator and denominator of a fraction,
# return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in
# parentheses.
#
# Example 1:
#
#
# Input: numerator = 1, denominator = 2
# Output: "0.5"
#
#
# Example 2:
#
#
# Input: numerator = 2, denominator = 1
# Output: "2"
#
# Example 3:
#
#
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"
#
#
#
class Solution:
    def fractionToDecimal(self, n, d):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        if n == 0:
            return "0"

        if (n > 0 and d < 0) or (n < 0 and d > 0):
            out = "-"
        else:
            out = ""

        n = -n if n < 0 else n
        d = -d if d < 0 else d

        div = n // d
        out += str(div)
        rem = n % d    # remainder
        if rem == 0:
            return out
        out += "."

        h = {}  # linkage back from remainder to dividend
        h[n] = (rem, len(out))

        n = rem
        while True:
            n *= 10
            div = n // d
            rem = n % d
            if n in h:
                break
            else:
                h[n] = (rem, len(out))
                n = rem
            out += str(div)
            if rem == 0:
                return out
            # print(h)

        top = n
        out2 = (out[0:h[top][1]] + "(" +
                out[h[top][1]:] + ")")
        out = out2

        return out

    #        0.0333
    # 300 | 10.0000
    #        1.000
    #          1000


def multiplicative_order(b, n):
    # exponent for b^e % n = 1
    count = 1
    while b % n != 1:
        b *= b
        count += 1
    return count


test = True
if test:
    s = Solution()
    # print(s.fractionToDecimal(2133, 999))
    print(s.fractionToDecimal(4, 333))
