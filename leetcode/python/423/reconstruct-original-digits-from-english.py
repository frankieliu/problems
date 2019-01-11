"""423. Reconstruct Original Digits from English

Given a non-empty string containing an out-of-order English
representation of digits 0-9, output the digits in ascending order.

Note:

Input contains only lowercase English letters.

Input is guaranteed to be valid and can be transformed to its original
digits. That means invalid inputs such as "abc" or "zerone" are not
permitted.

Input length is less than 50,000.

Example 1:
Input: "owoztneoer"
Output: "012"

Example 2:
Input: "fviefuro"
Output: "45"
"""


class Solution:

    def __init__(self):
        self.digits = [
            ("six", "x", 6),
            ("two", "w", 2),
            ("zero", "z", 0),
            ("eight", "g", 8),
            ("four", "u", 4),
            ("one", "o", 1),    # no o's below this
            ("five", "f", 5),   # no f's below this
            ("three", "h", 3),  # no h's below this
            ("seven", "s", 7),  # no s's below this
            ("nine", "n", 9)]

        self.count = {}
        for ch in range(ord('a'), ord('z') + 1):
            self.count[chr(ch)] = 0

    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        for a in s:
            self.count[a] += 1
        out = ""
        for word, letter, number in self.digits:
            acount = self.count[letter]
            out += str(number) * acount
            for w in word:
                self.count[w] -= acount
        return "".join(sorted(list(out)))


if __name__ == "__main__":
    s = Solution()
    ainput = "owoztneoer"
    print(s.originalDigits(ainput))
    ainput = "fviefuro"
    print(s.originalDigits(ainput))
