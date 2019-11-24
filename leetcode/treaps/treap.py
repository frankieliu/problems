class Node:
    def __init__(self, key, prior):
        self.left = None
        self.right = None
        self.key = key
        self.prior = prior

def split(t, key):
    """
    split(T, X):

    Separates tree T in 2 subtrees L and R trees, so that
    - L contains all elements with key X_L < X, and
    - R contains all elements with key X_R > X.

    This operation has O(logN) complexity and is implemented
    using an obvious recursion.
    """
    if t is None:
        return None, None

    if key < t.key:
        # this step is kind of tricky because
        # you are basically doing surgery on the tree
        ll, rr = split(t.left, key)
        t.left = rr
        rr = t
    else:
        ll, rr = split(t.right, key)
        t.right = ll
        ll = t

    return ll, rr


def insert(t, it):
    """
    Now implementation of Insert (X, Y) becomes obvious. First we descend
    in the tree (as in a regular binary search tree by X), and stop at
    the first node in which the priority value is less than Y. We have
    found the place where we will insert the new element. Next, we
    call Split (T, X) on the subtree starting at the found node, and
    use returned subtrees L and R as left and right children of the
    new node.
    """
    if t is None:
        t = it
        return t
    if it.prior > t.prior:
        it.left, it.right = split(t, it.key)
        t = it
    else:
        if it.key < t.key:
            t.left = insert(t.left, it)
        else:
            t.right = insert(t.right, it)
    return t


def merge(ll, rr):
    """
    Merge (T1, T2)

    combines two subtrees T1 and T2 and returns the new tree.

    This operation also has O(logN) complexity.
    It works under the assumption that T1 and T2 are ordered
    (all keys X in T1 are smaller than keys in T2).

    Thus, we need to combine these trees without violating
    the order of priorities Y. To do this, we choose as the
    root the tree which has higher priority Y in the root node,
    and recursively call Merge for the other tree and
    the corresponding subtree of the selected root node.
    """
    if ll is None or rr is None:
        if ll is not None:
            return ll
        else:
            return rr
    if ll.prior > rr.prior:
        ll.right = merge(ll.right, rr)
        return ll
    else:
        rr.left = merge(ll, rr.left)
        return rr


def erase(t, key):
    """
    Implementation of Erase (X) is also clear. First we descend in the
    tree (as in a regular binary search tree by X), looking for the
    element we want to delete. Once the node is found, we call Merge
    on it children and put the return value of the operation in the
    place of the element we're deleting.
    """
    if t.key == key:
        return merge(t.left, t.right)
    else:
        if key < t.key:
            t.left = erase(t.left, key)
        else:
            t.right = erase(t.right, key)
    return t


def build():
    """
    We implement Build operation with O(NlogN) complexity using N Insert calls.
    """
    pass


def union(ll, rr):
    """
    Union (T1, T2) has theoretical complexity O(Mlog(N/M)), but in
    practice it works very well, probably with a very small hidden
    constant. Let's assume without loss of generality that T1→Y>T2→Y,
    i. e. root of T1 will be the root of the result. To get the
    result, we need to merge trees T1→L, T1→R and T2 in two trees
    which could be children of T1 root. To do this, we call Split (T2,
    T1→X), thus splitting T2 in two parts L and R, which we then
    recursively combine with children of T1: Union (T1→L, L) and Union
    (T1→R, R), thus getting left and right subtrees of the result.
    """
    if ll is None or rr is None:
        if ll is not None:
            return ll
        else:
            return rr
    if ll.prior < rr.prior:
        ll, rr = rr, ll
    lt, rt = split(rr, ll.key)
    ll.left = union(ll.left, lt)
    ll.right = union(ll.right, rt)
    return ll
