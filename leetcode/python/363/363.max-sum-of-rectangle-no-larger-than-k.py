#
# @lc app=leetcode id=363 lang=python3
#
# [363] Max Sum of Rectangle No Larger Than K
#
# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/description/
#
# algorithms
# Hard (34.66%)
# Total Accepted:    25K
# Total Submissions: 72K
# Testcase Example:  '[[1,0,1],[0,-2,3]]\n2'
#
# Given a non-empty 2D matrix matrix and an integer k, find the max sum of a
# rectangle in the matrix such that its sum is no larger than k.
#
# Example:
#
#
# Input: matrix = [[1,0,1],[0,-2,3]], k = 2
# Output: 2
# Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is
# 2,
# and 2 is the max number no larger than k (k = 2).
#
# Note:
#
#
# The rectangle inside the matrix must have an area > 0.
# What if the number of rows is much larger than the number of columns?
#
#

class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class AVLTree():
    def __init__(self, *args):
        self.node = None
        self.height = -1
        self.balance = 0;

        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    def is_leaf(self):
        return (self.height == 0)

    def insert(self, key):
        tree = self.node

        newnode = Node(key)

        if tree == None:
            self.node = newnode
            self.node.left = AVLTree()
            self.node.right = AVLTree()
            # debug("Inserted key [" + str(key) + "]")

        elif key < tree.key:
            self.node.left.insert(key)

        elif key > tree.key:
            self.node.right.insert(key)

        else:
            # debug("Key [" + str(key) + "] already in tree.")
            pass

        self.rebalance()

    def rebalance(self):
        '''
        Rebalance a particular (sub)tree
        '''
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.lrotate() # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rrotate() # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()

    def rrotate(self):
        # Rotate left pivoting on self
        # debug ('Rotating ' + str(self.node.key) + ' right')
        A = self.node
        B = self.node.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T


    def lrotate(self):
        # Rotate left pivoting on self
        # debug ('Rotating ' + str(self.node.key) + ' left')
        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T

    def update_heights(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def delete(self, key):
        # debug("Trying to delete at node: " + str(self.node.key))
        if self.node != None:
            if self.node.key == key:
                # debug("Deleting ... " + str(key))
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None # leaves can be killed at will
                # if only one subtree, take that
                elif self.node.left.node == None:
                    self.node = self.node.right.node
                elif self.node.right.node == None:
                    self.node = self.node.left.node

                # worst-case: both children present. Find logical successor
                else:
                    replacement = self.logical_successor(self.node)
                    if replacement != None: # sanity check
                        # debug("Found replacement for " + str(key) + " -> " + str(replacement.key))
                        self.node.key = replacement.key

                        # replaced. Now delete the key from right child
                        self.node.right.delete(replacement.key)

                self.rebalance()
                return
            elif key < self.node.key:
                self.node.left.delete(key)
            elif key > self.node.key:
                self.node.right.delete(key)

            self.rebalance()
        else:
            return

    def logical_predecessor(self, node):
        '''
        Find the biggest valued node in LEFT child
        '''
        node = node.left.node
        if node != None:
            while node.right != None:
                if node.right.node == None:
                    return node
                else:
                    node = node.right.node
        return node

    def logical_successor(self, node):
        '''
        Find the smallese valued node in RIGHT child
        '''
        node = node.right.node
        if node != None: # just a sanity check

            while node.left != None:
                # debug("LS: traversing: " + str(node.key))
                if node.left.node == None:
                    return node
                else:
                    node = node.left.node
        return node

    def check_balanced(self):
        if self == None or self.node == None:
            return True

        # We always need to make sure we are balanced
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())

    def inorder_traverse(self):
        if self.node == None:
            return []

        inlist = []
        l = self.node.left.inorder_traverse()
        for i in l:
            inlist.append(i)

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l:
            inlist.append(i)

        return inlist

    def display(self, level=0, pref=''):
        '''
        Display the whole tree. Uses recursive def.
        TODO: create a better display using breadth-first search
        '''
        self.update_heights()  # Must update heights before balances
        self.update_balances()
        if(self.node != None):
            print ('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(self.balance) + "]", 'L' if self.is_leaf() else ' '    )
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.left != None:
                self.node.right.display(level + 1, '>')

    def ceiling(self, val):
        cur = self.node
        result = 1<<31
        while cur:
            if cur.key < val:
                cur = cur.right
            else:
                result = min(result, cur.key)
                cur = cur.left
            if cur:
                cur = cur.node
        return result

class Solution:
    def maxSumSubmatrix(self, matrix, k):

        """Group by columns

        Idea for all possible pair of columns, do the 1D projection,
        and find kadane's best subarray sum

        But because it cannot be above k, in the case that kadane is
        above k, we do a binary search:

        For each element in the prefix sum, p[j] we look at the
        previous elements that are more than p[j]-k, because it will
        make the sum strictly less than k, in this case the most
        efficient method is a binary search of the closest element
        bigger than p[j]-k. (ceiling search)


        """
        def bstSearch(A, k):
            _sum = 0
            bst = AVLTree()
            bst.insert(0)
            _max = -(1<<31)
            for a in A:
                _sum += a
                prevSum = bst.ceiling(_sum - k)
                _max = max(_max, _sum - prevSum)
                bst.insert(_sum)
            return _max

        def kadane(A):
            _max = -(1<<31)
            sum = 0
            for a in A:
                sum = max(a, a + sum)
                _max = max(_max, sum)
            return _max

        nrows = len(matrix)
        if nrows == 0: return 0
        ncols = len(matrix[0])
        if ncols == 0: return 0

        _max = -(1<<31)
        for left in range(ncols):
            sum = [0]*nrows
            for right in range(left, ncols):
                for i in range(nrows):
                    sum[i] += matrix[i][right]
                kad = kadane(sum)
                if kad > k: # need to find the closest one
                    _max = max(_max, bstSearch(sum, k))
                else:
                    _max = max(_max, kad)
                if _max == k:
                    return k
        return _max



test = True
if test:
    sol = Solution()
    case = [False]*0 + [True] + [False]*1
    if case[0]:
        # Example:
        matrix = [[1,0,1],[0,-2,3]]
        k = 2
        # Output: 2
        print(sol.maxSumSubmatrix(matrix, k))
