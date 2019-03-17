
My Python solution with two list using pop() method

https://leetcode.com/problems/implement-queue-using-stacks/discuss/64226

* Lang:    python3
* Author:  Lucifer27
* Votes:   4

    class Queue:
        # initialize your data structure here.
        def __init__(self):
            self.stack1 = []
            self.stack2 = []
    
        # @param x, an integer
        # @return nothing
        def push(self, x):
            self.stack1.append(x)
    
        # @return nothing
        def pop(self):
            if len(self.stack2)!=0:
                self.stack2.pop()
            else:
                while len(self.stack1)!=0:
                    self.stack2.append(self.stack1.pop())
                self.stack2.pop()
    
        # @return an integer
        def peek(self):
            if len(self.stack2)!=0:
                return self.stack2[-1]
            else:
                while len(self.stack1)!=0:
                    self.stack2.append(self.stack1.pop())
                return self.stack2[-1]
    
        # @return an boolean
        def empty(self):
            if len(self.stack1)==0 and len(self.stack2)==0:
                return True
            else:
                return False
