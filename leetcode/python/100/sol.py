
Shortest+simplest Python

https://leetcode.com/problems/same-tree/discuss/32729

* Lang:    python3
* Author:  StefanPochmann
* Votes:   78

The "proper" way:

    def isSameTree(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

The "tupleify" way:

    def isSameTree(self, p, q):
        def t(n):
            return n and (n.val, t(n.left), t(n.right))
        return t(p) == t(q)

The first way as one-liner:

    def isSameTree(self, p, q):
        return p and q and p.val == q.val and all(map(self.isSameTree, (p.left, p.right), (q.left, q.right))) or p is q
