
def doc():
    """
    invariant: bigger than your nephews
    t.right.s >= t.left.left.s, t.left.right.s
    t.left.s >= t.right.left.s, t.right.left.s
    """
    pass


def maintain(t, flag):
    if flag is False:
        if t.left.left.s > t.right.s:
            t = cw(t)
        elif t.left.right.s > t.right.s:
            t.left = ccw(t.left)
            t = cw(t)
        else:
            return
    else:
        if t.right.right.s > t.left.s:
            t = ccw(t)
        elif t.right.left.s > t.left.s:
            t.right = cw(t.right)
            t = ccw(t)
        else:
            return
    # need to check left's left
    t.left = maintain(t.left, False)
    t.right = maintain(t.right, True)
    t = maintain(maintain(t, False), True)


def simple_insert(t, v):
    if t is None:
        t = Node(v)
    else:
        t.s = t.s + 1
        if v < t.key:
            t.left = simple_insert(t.left, v)
        else:
            t.right = simple_insert(t.right, v)


def insert(t, v):
    """ insert v into bst with root t) """
    if t is None:
        t = Node(v)
    else:
        t.s += 1
        if v < t.key:
            t = simple_insert(t.left, v)
        else:
            t = simple_insert(t.right, v)
        t = maintain(t, v > t.key)


def delete(t, v):
    t.s -= 1
    if ((v == t.key) or
        (v < t.key and t.left is None) or
        (v > t.key and t.right is None)):
        d = t.key
        if t.left is None or t.right is None:
            if t.left:
                t = t.left
            else:
                t = t.right
        else:
            t.key = delete(l.left, t.v + 1)
    else:
        if v < t.key:
            delete(t.left. v)
        else:
            delete(t.right, v)





def find(t, v):
    pass


def rank(t, v):
    """
    1 + number of keys less than v
    """
    pass


def select(t, k):
    """ select kth position
    include get-max and get-min
    get-min is equivalent to select(t,1)
    get-max is equivalent to select(t,t.s)
    """
    pass


def pred(t, v):
    """
    node with max key < v
    """
    pass


def succ(t, v):
    """
    node with min key > v
    """
    pass

def cw(y):
    '''
       y            x
     x   c  ->    a    y
    a b               b c
    '''
    x = y.left
    y.left = x.right
    x.right = y

    x.s = y.s    # makes sense: x in y's position
    y.s = y.left.s + y.right.s + 1   # new weights for y
    return x


def ccw(x):
    y = x.right
    x.right = y.left
    y.left = x
    y.s = x.s
    x.s = x.left.s + x.right.s + 1
    return y
