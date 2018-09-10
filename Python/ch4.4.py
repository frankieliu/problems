import json

class Tree():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def str(self):
        if self.value is not None:
            l = ''
            r = ''
            if self.left is not None:
                l = self.left.str()
            if self.right is not None:
                r = self.right.str()

            return '[' + str(self.value) + ',' + l + ',' + r  + ']'
        else:
            return ''
    def listBfs(self):
        l = [[self]]
        level = 0
        while l[level]:
            l1 = []
            for n in l[level]:
                if n is not None:
                    if n.left is not None:
                        l1 += [n.left]
                    if n.right is not None:
                        l1 += [n.right]
            l.append(l1)
            level += 1
        return l[:-1]

t = Tree(1,
         Tree(2,
              Tree(3),
              Tree(31,
                   Tree(4),
                   Tree(41))),
         Tree(21,
              Tree(32),
              Tree(33)))

print(t.str())
for l in t.listBfs():
    for n in l:
        print(n.value,end=',')
    print()
