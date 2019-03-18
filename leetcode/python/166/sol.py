
Do not use python as cpp, here's a short version python code

https://leetcode.com/problems/fraction-to-recurring-decimal/discuss/51110

* Lang:    python3
* Author:  tusizi
* Votes:   38

Though python is slow, It is easy to write

    class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator*denominator < 0 else ''
        result = [sign+str(n), '.']
        stack = []
        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(remainder*10, abs(denominator))
            result.append(str(n))

        idx = stack.index(remainder)
        result.insert(idx+2, '(')
        result.append(')')
        return ''.join(result).replace('(0)', '').rstrip('.')

and there's no overflow
