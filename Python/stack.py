
# 3 stacks with with single array
# requirement for a stacks

class Stack:
    def __init__(self):
        self.size = 1000
        self.s = [False]*self.size
        self.top = -1

    def pop(self):
        if self.top == -1:
            return None
        else:
            ans = self.s[self.top]
            self.top -= 1
            return ans

    def push(self,value):
        self.top += 1
        if self.top > self.size:
            self.top -= 1
            return
        else:
            self.s[self.top] = value


s = Stack()
s.push(1)
s.push(2)
s.push(3)

print(s.pop())
print(s.pop())
print(s.pop())
