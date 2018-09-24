class tree:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        if value is not None:
            if left is None:
                self.left = tree()
            else:
                self.left = left
            if right is None:
                self.right = tree()
            else:
                self.right = right


    def str(self):
        if self.value is None:
            return 'E'
        else:
            res = ('[' +
                   str(self.value) + ',' +
                   self.left.str() + ',' +
                   self.right.str() +
                   ']')
            return res

    def subtree(self, t2):
        if t2.value is None:
            return True
        elif self.value is None:
            return False
        elif self.value != t2.value:
            return self.left.subtree(t2) | self.right.subtree(t2)
        else:
            if self.left.subtree(t2.left) & self.right.subtree(t2.right):
                return True
            else:
                return self.left.subtree(t2) | self.right.subtree(t2)

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

t1 = tree(
    1,
    tree(
        2,
        tree(3),
        tree(4)),
    tree(
        5,
        tree(61),
        tree(7)))

t2 = t.left
t3 = t2.left
t4 = t2.right
t5 = t.right
t6 = t5.left
t7 = t5.right

print('t',t.subtree(t))
print('t2',t.subtree(t2))
print('t3',t.subtree(t3))
print('t4',t.subtree(t4))
print('t5',t.subtree(t5))
print('t6',t.subtree(t6))
print('t7',t.subtree(t7))
print('t1',t.subtree(t1))
