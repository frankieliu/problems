
8-line Python solution, stack, 40ms

https://leetcode.com/problems/valid-parentheses/discuss/9482

* Lang:    python3
* Author:  kitt
* Votes:   4

    def isValid(self, s):
        stack, match = [], {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in match:
                if not (stack and stack.pop() == match[ch]):
                    return False
            else:
                stack.append(ch)
        return not stack
