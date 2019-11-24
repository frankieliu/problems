class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __repr__(self):
        return "(" + ",".join(map(str, [self.val, self.left, self.right])) + ")"

a = list(range(1,10))
n = [Node(x) for x in a]
n[0].left = n[1]
n[0].right = n[2]
n[1].left = n[3]
n[1].right = n[4]
print(n[0])
