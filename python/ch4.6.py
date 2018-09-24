# common ancestor
# r
# if p on left and q on right of r then r is the common ancestor
# r
# p on left?
# p on r.left?

class tree:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        if self.value is not None:
            if left == None:
                self.left = tree()
            else:
                self.left = left
            if right == None:
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

    def search(self, p, q):
        if self.value is None:
            return [0, None]

        # Found one of them
        if self == p or self == q:
            # look left for the other

            [r, t] = self.left.search(p, q)
            if r == 1:
                # p,q on left
                # common ancestor is self
                return [2, self]
            else:
                # look right for the other
                [r, t] = self.right.search(p, q)
                if r == 1:
                    # other on right
                    # common anscestor is self
                    return [2, self]
                else:
                    # only one found
                    return [1, self]

        else:
            # try searching on the left
            [r, t] = self.left.search(p, q)
            # found one
            if r == 1:
                # look for the other
                [r, t1] = self.right.search(p, q)
                if r == 1:
                    # found the other
                    # current must be common anscestor
                    return [2, self]
                else:
                    # did not find other
                    # return original
                    return [1, t]
            # found both
            elif r == 2:
                # this should already contain the answer
                return [r, t]
            # found none
            else:
                return self.right.search(p, q)

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
    for tmp2 in [t,t2,t3,t4,t5,t6,t7]:
        if tmp.value != tmp2.value:
            print(tmp.value, tmp2.value, t.search(tmp, tmp2)[0], t.search(tmp, tmp2)[1].value)

ans = '''
[1,[2,[3,E,E],[4,E,E]],[5,[6,E,E],[7,E,E]]]
1 2  1
1 3  1
1 4  1
1 5  1
1 6  1
1 7  1
2 1  1
2 3  2
2 4  2
2 5  1
2 6  1
2 7  1
3 1  1
3 2  2
3 4  2
3 5  1
3 6  1
3 7  1
4 1  1
4 2  2
4 3  2
4 5  1
4 6  1
4 7  1
5 1  1
5 2  1
5 3  1
5 4  1
5 6  5
5 7  5
6 1  1
6 2  1
6 3  1
6 4  1
6 5  5
6 7  5
7 1  1
7 2  1
7 3  1
7 4  1
7 5  5
7 6  5
'''
