class tree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        if self.left is not None:
            self.left.parent = self
        self.right = right
        if self.right is not None:
            self.right.parent = self
        self.parent = parent
    def str(self):
        res = '['
        res += str(self.value)
        if self.left is not None:
            print(self.left.value)
            res += ',' + self.left.str()
        if self.right is not None:
            res += ',' + self.right.str()
        res += ']'
        return res
    def leftmost(self):
        if self.left is not None:
            return self.left.leftmost()
        else:
            return self
    def successor(self):
        if self.right is not None:
            return self.right.leftmost()
        else:
            e = self
            p = e.parent
            # print(e.value, p.value, p.right.value)
            while p is not None:
                if (p.left == e):
                    return p
                else:
                    e = p
                    p = e.parent
        return None

t = tree(
    1,
    tree(
        2,
        tree(3),
        tree(4)),
    tree(
        5,
        tree(6),
        tree(7)))
print(t.str())

t2 = t.left
t3 = t2.left
t4 = t2.right
t5 = t.right
t6 = t5.left
t7 = t5.right
for tmp in [t,t2,t3,t4,t5,t6,t7]:
    if tmp.successor() is None:
        print(tmp.value, None)
    else:
        print(tmp.value, tmp.successor().value)
