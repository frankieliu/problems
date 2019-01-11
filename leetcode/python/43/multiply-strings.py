"""43. Multiply Strings
Medium

794

337

Favorite

Share

Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.

You must not use any built-in BigInteger library or convert the inputs
to integer directly.

Accepted
174,986
Submissions
592,249

"""

class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        out = [0] * (len(num1) + len(num2))
        npos = len(out)-1
        for n1 in reversed(num1):
            pos = npos
            for n2 in reversed(num2):
                p = int(n1) * int(n2)
                out[pos] += p
                out[pos-1] += out[pos] // 10
                out[pos] = out[pos] % 10
                # print(out)
                pos -= 1  # shift on num2
            npos -= 1     # shift on num1

        # get rid of leading zeros
        for i in range(0, len(out)):
            if out[i] != 0:
                break

        return ''.join([str(x) for x in out[i::]])

s=Solution()
print(s.multiply('123','456'))
