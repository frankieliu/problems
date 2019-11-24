#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (36.85%)
# Total Accepted:    67K
# Total Submissions: 181.8K
# Testcase Example:  '[5,2,6,1]'
#
# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].
#
# Example:
#
#
# Input: [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
#
#
#
class Solution:
    def countSmaller(self, nums):
        pass


def rotate_left(tree):
    """
          t         k
        x   k  -> t
           z       z
    """
    t = tree['t']
    k = t.right
    t.right = k.left
    k.left = t
    k.s = t.s
    t.s = t.left.s + t.right.s + 1
    print(k)
    tree['t'] = k

def rotate_right(self, tp):
    """
            t       k
          k    ->     t
           z         z
    """
    t = tree['t']
    k = t.left
    t.left = k.right
    k.right = t
    k.s = t.s
    t.s = t.left.s + t.right.s + 1
    tree['t'] = k

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.s = 1

    def __repr__(self):
        return ("[" +
                ",".join([str(x)
                          for x in [self.val, self.left, self.right]]) + "]")



    def maintain(self, tp, checkleft):
        t = tp[0]
        if not checkleft:
            if t.right.s > t.left.left.s:
                self.rotate_right([t])
            elif t.right.s > t.left.right.s:
                self.rotate_left([t.left])
                self.rotate_right([t])
            else:
                return
        else:
            if t.left.s > t.right.right.s:
                self.rotate_left([t])
            elif t.left.s > t.right.left.s:
                self.rotate_right([t.right])
                self.rotate_left([t])
            else:
                return
        self.maintain([t.left], checkleft=false)
        self.maintain([t.right], checkleft=true)
        self.maintain([t], checkleft=false)
        self.maintain([t], checkleft=true)


na = [Node(x) for x in range(0, 10)]
na[0].left, na[0].right = (na[1], na[2])
na[1].left, na[1].right = (na[3], na[4])
na[2].left, na[2].right = (na[5], na[6])

tree = {'t': na[0]}
print(tree['t'])
rotate_left(tree)
print(tree['t'])
rotate_right(

test = True
if test:
    sol = Solution()
    case = [False] * 0 + [True] + [False] * 1
    if case[0]:
        # Example:
        Input = [5, 2, 6, 1]
        # Output: [2,1,1,0]
        print(sol.countSmaller(Input))
