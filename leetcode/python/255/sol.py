
AC Python O(n) time O(1) extra space

https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/discuss/68197

* Lang:    python3
* Author:  dietpepsi
* Votes:   20

 A easy solution is O(n) time and O(n) space using a stack

    def verifyPreorder(self, preorder):
        stack = []
        lower = -1 << 31
        for x in preorder:
            if x < lower:
                return False
            while stack and x > stack[-1]:
                lower = stack.pop()
            stack.append(x)
        return True


    # 59 / 59 test cases passed.
    # Status: Accepted
    # Runtime: 100 ms
    # 95.31%

Then we realize that the preorder array can be reused as the stack thus achieve O(1) extra space, since the scanned items of preorder array is always more than or equal to the length of the stack.

    def verifyPreorder(self, preorder):
        # stack = preorder[:i], reuse preorder as stack
        lower = -1 << 31
        i = 0
        for x in preorder:
            if x < lower:
                return False
            while i > 0 and x > preorder[i - 1]:
                lower = preorder[i - 1]
                i -= 1
            preorder[i] = x
            i += 1
        return True


    # 59 / 59 test cases passed.
    # Status: Accepted
    # Runtime: 112 ms
    # 70.31%
