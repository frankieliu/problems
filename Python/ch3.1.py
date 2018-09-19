# 3 stacks with with single array
# requirement for a stacks

from itertools import chain

class Stack:
    def __init__(self):
        self.size = 1000

        # These point to the three stacks
        self.top = [-1,-1,-1]

        # This points to the "free" stack
        self.free = 0
        self.s = [(False, i) for i in chain(range(1,self.size),[-1])]

    def pop(self,sn):  # start number
        if self.top[sn] == -1:
            return None
        else:
            ans = self.s[self.top[sn]]

            # Add popped item to free pool
            self.s[self.top[sn]] = (False, self.free)
            self.free = self.top[sn]

            self.top[sn] = ans[1]   # point to next element
            return ans[0]

    def push(self,sn,value):
        # if there is free space
        if self.s[self.free][1] == -1:
            raise NameError("No free space")

        # Add new element
        prevTop = self.top[sn]
        nextFree = self.s[self.free][1]
        self.top[sn] = self.free
        self.s[self.top[sn]] = (value, prevTop)

        # Remove from free list
        self.free = nextFree
        return nextFree



s = Stack()
if True:
    s.push(0,1)
    s.push(0,1)
    s.push(0,1)
    s.push(1,2)
    s.push(1,2)
    s.push(1,2)
    s.push(2,3)
    s.push(2,3)
    s.push(2,3)

    print(s.pop(0))
    print(s.pop(1))
    print(s.pop(2))
    print("next free", s.push(0,11))
    print("next free", s.push(0,11))
    print(s.pop(0))
    print(s.pop(1))
    print(s.pop(2))
    print(s.pop(0))
    print(s.pop(1))
    print(s.pop(2))
    print(s.pop(0))
    print(s.pop(1))
    print(s.pop(2))
    print(s.pop(0))
    print(s.pop(1))
    print(s.pop(2))
