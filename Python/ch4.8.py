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

    def sumCheck(self, s, buf, level):
        if self.value is not None:
            tmp = s
            # add the current value
            buf.append(self.value)

            #
            #        v4
            #     v5    v5   --> at this level add your own value
            #    ....  ....      and allow subtraction of it to the sum
            #                    in other words assume that the paths in
            #                    v4 and above have already been taken of
            #                    at the v4 level
            for i in range(level,-1,-1):
                tmp -= buf[i]
                if tmp == 0:
                    print(buf, i, level)

            # descend further into the tree to
            # to consider more potential values
            c1 = buf.copy()
            c2 = buf.copy()
            self.left.sumCheck(s, c1, level + 1)
            self.right.sumCheck(s, c2, level + 1)


t = tree(
    1,
    tree(
        1,
        tree(1,
             tree(1),
             tree(1)),
        tree(1,
             tree(1),
             tree(1,
                  tree(1),
                  tree(1)))))

t.sumCheck(3, [], 0)
