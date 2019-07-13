class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def postorder_stack(root):
    s = []
    v = {}  # pushed once

    # Not a good solution because
    # it uses extra storage v
    # and the key to v may not be unique

    s.append(root)
    while s:
        t = s.pop()
        if t.val in v:
            print(t.val)
        else:
            v[t.val] = True
            s.append(t)
            if t.right:
                s.append(t.right)
            if t.left:
                s.append(t.left)


def postorder_stack_2(root):
    s = []

    # A better solution but uses twice the
    # stack space, but probably good enough

    s.append((root, False))
    while s:
        t, v = s.pop()
        if v:
            print(t.val)
        else:
            s.append((t, True))
            if t.right:
                s.append((t.right, False))
            if t.left:
                s.append((t.left, False))


def postorder_stack_3(root):
    s = []

    # Add a marker to indicate if
    # next element (below it in the stack)
    # should remain in the stack (it should
    # if it is the first time visiting it)

    s.append(root)
    s.append(True)
    while s:
        t = s.pop()
        if t is True:
            cur = s[-1]
            if cur.right:
                s.append(cur.right)
                s.append(True)
            if cur.left:
                s.append(cur.left)
                s.append(True)
        else:
            print(t.val)


def morrisPostorderTraversal(root):

    dummyRoot = TreeNode(0)
    dummyRoot.left = root

    # think of p as the current node
    p = dummyRoot
    while p:

        print("visiting", p.val)

        if p.left is None:

            pout = p.right.val if p.right else None
            print("No left: setting p to p.right", pout)

            p = p.right


        else:

            # The promise is that we find a way
            # return back to the parent node
            # when we go to the left branch.
            #
            # This is accomplished by adding
            # a link from the predecessor node
            # (the last node to be visited in
            # the left branch) to the parent node.
            #
            # So after visiting the predecessor
            # node, it will return to the parent
            # node, but this time when you try
            # to add a linkage, you will find that
            # it is already there.
            #
            # At that point, the point in which
            # we find an existing linkage we print
            # back the path to the parent.
            #
            # Here is an illustration
            #
            #          -
            #    -           -
            #  -    -      -    -
            # - -  - -    - -  - -
            #
            # we see that the post order traversal
            # consists of printing, diagonal NW passes
            # through the nodes
            #
            #          8
            #    4           8
            #  2    4      6    8
            # 1 2  3 4    5 6  7 8

            print("Left exists")

            # there p.left, therefore must have a pred
            # find the predecessor
            pred = p.left
            while pred.right and pred.right != p:
                pred = pred.right

            print("Found pred", pred.val)

            # first time
            # create linkage
            # between predecessor and p
            if pred.right is None:

                print("First pred visit")
                print("Creating linkage pred.right", p.val)
                pred.right = p

                print("Going left", p.left.val)
                p = p.left

            else:

                print("Second pred visit: reverse links")

                # second time
                # reverse right refs
                first = p
                middle = p.left
                while middle != p:
                    last = middle.right
                    middle.right = first
                    first = middle
                    middle = last

                #    First
                #  Mid
                #    Last

                # visit nodes from pred to p
                first = p
                middle = pred
                while middle != p:
                    print(middle.val)
                    last = middle.right
                    middle.right = first
                    first = middle
                    middle = last

                # remove the pred to node reference
                # to restore the tree structure

                pout = p.right.val if p.right else None
                print("Remove linkage, go right",p.val,pout)

                pred.right = None
                p = p.right


"""

             1
       2         3

    4(2) 5(1)   6  7


"""

t = []
for i in range(1, 8):
    t.append(TreeNode(i))

for i in range(len(t)):
    left = 2*i+1
    right = 2*i+2
    if left < len(t) and t[left]:
        t[i].left = t[left]
    if right < len(t) and t[right]:
        t[i].right = t[right]

# postorder_stack_3(t[0])
morrisPostorderTraversal(t[0])
