
10 lines python solution beats 100%

https://leetcode.com/problems/squirrel-simulation/discuss/102816

* Lang:    python3
* Author:  Mrcommon_zzzzzz
* Votes:   0

Imaging the squirrel is starting at tree position, no matter which nuts to get first, the total distance will be 2 * tree to each nut, which is 'sum' in my code.
Now we need to get the max distance difference between the squirrel to one of the nuts, and that nuts to the tree, where max = Tree_dis - squirrel dis, and total distance = sum - (Tree_dis - squirrel_dis) = sum - Tree_dis + squirrel_dis.

So the important part is to find the max distance difference between the squirrel to one of the nuts, and that nuts to the tree. Height and width are not useful here.

"""

def minDistance(self, height, width, tree, squirrel, nuts):
        maxs = 0
        sums = 0
        for nut in nuts:
            trees = abs(tree[0]-nut[0]) + abs(tree[1]-nut[1])
            sums += 2*trees
            dis = abs(squirrel[0]-nut[0]) + abs(squirrel[1]-nut[1])
            if trees - dis > maxs:
                maxs = trees - dis
        return sums - maxs if maxs else sums + abs(trees-dis)
"""
