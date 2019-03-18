
9-line Python solution, easy to understand

https://leetcode.com/problems/simplify-path/discuss/25779

* Lang:    python3
* Author:  kitt
* Votes:   12

    def simplifyPath(self, path):
        stack = []
        for token in path.split('/'):
            if token in ('', '.'):
                pass
            elif token == '..':
                if stack: stack.pop()
            else:
                stack.append(token)
        return '/' + '/'.join(stack)
