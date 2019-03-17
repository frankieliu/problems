
Simple Python solution using stack. With Explanation.

https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/78560

* Lang:    python3
* Author:  harshaneel
* Votes:   42

This is very simple problem if you use stacks. The key here is, when you see two consecutive "#" characters on stack, pop both of them and replace the topmost element on the stack with "#". For example,

preorder = 1,2,3,#,#,#,#

Pass 1:  stack = [1]

Pass 2: stack = [1,2]

Pass 3: stack = [1,2,3]

Pass 4: stack = [1,2,3,#]

Pass 5: stack = [1,2,3,#,#] -> two #s on top so pop them and replace top with #. -> stack = [1,2,#]

Pass 6: stack = [1,2,#,#] -> two #s on top so pop them and replace top with #. -> stack = [1,#]

Pass 7: stack = [1,#,#] -> two #s on top so pop them and replace top with #. -> stack = [#]

If there is only one # on stack at the end of the string then return True else return False.

Here is the code for that,

    class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        top = -1
        preorder = preorder.split(',')
        for s in preorder:
            stack.append(s)
            top += 1
            while(self.endsWithTwoHashes(stack,top)):
                h = stack.pop()
                top -= 1
                h = stack.pop()
                top -= 1
                if top < 0:
                    return False
                h = stack.pop()
                stack.append('#')
            #print stack
        if len(stack) == 1:
            if stack[0] == '#':
                return True
        return False
    
    def endsWithTwoHashes(self,stack,top):
        if top<1:
            return False
        if stack[top]=='#' and stack[top-1]=='#':
            return True
        return False
