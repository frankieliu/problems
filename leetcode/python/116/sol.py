
7 lines, iterative, real O(1) space

https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37484

* Lang:    python3
* Author:  StefanPochmann
* Votes:   84

Simply do it level by level, using the `next`-pointers of the current level to go through the current level and set the `next`-pointers of the next level.

I say "real" O(1) space because of the many recursive solutions ignoring that recursion management needs space.

    def connect(self, root):
        while root and root.left:
            next = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next
