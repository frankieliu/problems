class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.p = None     # parent
        self.s = 1        # size

    def __repr__(self):
        return ("[" + ",".join(
            [str(self.val),
             str(self.left),
             str(self.right)]) +
            "]")

class sbt:
    def __init__():
        self.root = None

def rright(t):
    """
       t        a
      a  b       t
       z        z b
    """
    a = t.left
    t.left = a.right
    a.right = t
    a.p = t.p
    t.p = a
    if t.left:  # if there is a z
        t.left.p = t
    if a.p:
        if a.p.left == t:
            a.p.left = a
        else:
            a.p.right = a
    a.s = t.s
    t.s = ((t.left and t.left.s or 0) +
           (t.right and t.right.s or 0) +
           1)
    return a

def rleft(t):
    """
       t     b
     a  b   t
       z   a z
    """
    b = t.right
    t.right = b.left
    b.left = t
    b.p = t.p
    t.p = b
    if t.right:
        t.right.p = t
    if b.p:
        if b.p.left == t:
            b.p.left = b
        else:
            b.p.right = b
    b.s = t.s
    t.s = ((t.left and t.left.s or 0) +
           (t.right and t.right.s or 0) +
           1)
    return b

def maintain(t, checkLeftNephews):
    """
        t
      l    r
     a b  c d
    """
    print(t, checkLeftNephews)
    tout = None
    if checkLeftNephews:
        a = t.left and t.left.left
        b = t.left and t.left.right
        r = t.right
        asiz = a and a.s or 0
        bsiz = b and b.s or 0
        rsiz = r and r.s or 0
        print("a:{} b:{} r:{} asiz:{} bsiz:{} rsiz:{}".format(
            a,b,r,asiz,bsiz,rsiz))
        if asiz > rsiz:
            tout = rright(t)
        elif bsiz > rsiz:
            rleft(t.left)
            tout = rright(t)
        else:
            return t
    else:
        c = t.right and t.right.left
        d = t.right and t.right.right
        ll = t.left
        csiz = c and c.s or 0
        dsiz = d and d.s or 0
        llsiz = ll and ll.s or 0
        if dsiz > llsize:
            tout = rleft(t)
        elif csiz > llsize:
            rright(t.right)
            tout = rleft(t)
        else:
            return t
    t.left = maintain(t.left, checkLeftNephews=True)
    t.right = maintain(t.right, checkLeftNephews=False)
    tout = maintain(tout, True)
    tout = maintain(tout, False)
    return tout

def insert(t,v):
    t.s += 1
    if v < t.val:
        if t.left is None:
            t.left = Node(v)
            t.left.p = t
        else:
            t.left = insert(t.left, v)
    else:
        if t.right is None:
            t.right = Node(v)
            t.s += 1
        else:
            t.right = insert(t.right, v)

    # must check if t.p is valid
    # also must assume that maintain might be a completely
    # different

    tout = maintain(t, v >= t.val)
    if t.p:
        if t.p.left == t:
            t.p.left = tout
        else:
            t.p.right = tout
    return tout

n = [Node(x) for x in range(0,11)]
d = {0:[1,2,7], 1:[3,4,3], 2:[5,6,3]}
for k,v in d.items():
    n[k].left  = n[v[0]]
    n[k].right = n[v[1]]
    n[v[0]].p = n[k]
    n[v[1]].p = n[k]
    n[k].s = v[2]

t = n[0]
t = insert(t, 10)
t = insert(t, 11)
t = insert(t, 12)
t = insert(t, 13)
t = insert(t, 14)

print(t)
