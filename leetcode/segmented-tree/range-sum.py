# https://leetcode.com/problems/range-sum-query-mutable/discuss/75715/python-solution-segment-tree-with-lazy-propagation

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        length = len(nums)
        self.original_length = length
        if length > 0 and length&(length-1) == 0:
            self.tree_length = 2 * length -1
        else:
            power = 0
            while 2**power < length:
                power += 1
            self.tree_length = 2 * (2**power) -1
        self.tree = [0 for _ in range(self.tree_length)]
        self.lazy = [0 for _ in range(self.tree_length)]
        self.constructTree(nums, 0, self.original_length-1, 0)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        # Note that it's replace instead of delta.
        self.updateTree(val, i, i, 0, self.original_length-1, 0)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.queryRange(i, j, 0, self.original_length-1, 0)

    def constructTree(self, nums, node_low, node_high, pos):
        # Create a node that's responsible for indices node_low to node_high of the original input array nums. And this node is stored at Tree[] position pos.
        if node_low > node_high: return
        if node_low == node_high:
            self.tree[pos] = nums[node_low]
            return
        middle = node_low + (node_high - node_low)/2
        self.constructTree(nums, node_low, middle, pos*2 + 1)
        self.constructTree(nums, middle+1, node_high, pos*2 + 2)
        self.tree[pos] = self.tree[pos*2 + 1] + self.tree[pos*2 + 2] # The merge operation.

    def updateTree(self, new_val, range_start, range_end, node_low, node_high, pos):
        # The 'current node' is defined by node_low, node_high, and pos.
        if node_high < node_low:
            return
        if self.lazy[pos] != 0:
            self.tree[pos] = self.lazy[pos]
            if node_low != node_high:
                self.lazy[pos*2 + 1] = self.lazy[pos]
                self.lazy[pos*2 + 2] = self.lazy[pos]
            self.lazy[pos] = 0 # Up-to-date now.
        if range_start > node_high or range_end < node_low:
            return
        if range_start <= node_low and range_end >= node_high:
            # Complete overlap.
            self.tree[pos] = new_val
            if node_high != node_low:
                self.lazy[pos*2 + 1] = new_val
                self.lazy[pos*2 + 2] = new_val
            return
        # Partial overlap.
        middle = node_low + (node_high - node_low)/2
        self.updateTree(new_val, range_start, range_end, node_low, middle, pos*2 + 1)
        self.updateTree(new_val, range_start, range_end, middle+1, node_high, pos*2 + 2)
        self.tree[pos] = self.tree[pos*2 + 1] + self.tree[pos*2 + 2] # The merge operation.

    def queryRange(self, range_start, range_end, node_low, node_high, pos):
        if node_high < node_low:
            return 0 # Since interested in the sum.
        if self.lazy[pos] != 0:
            self.tree[pos] = self.lazy[pos]
            if node_low != node_high:
                self.lazy[pos* 2 + 1] = self.lazy[pos]
                self.lazy[pos* 2 + 2] = self.lazy[pos]
            self.lazy[pos] = 0
        if node_high < range_start or node_low > range_end:
            return 0
        if range_start <= node_low and range_end >= node_high:
            return self.tree[pos]
        # Partial overlap.
        middle = node_low + (node_high - node_low) /2
        # Get left and right sums, add them together to get the sum over the queried range.
        return self.queryRange(range_start, range_end, node_low, middle, pos * 2 + 1) + \
               self.queryRange(range_start, range_end, middle + 1, node_high, pos*2 + 2)
