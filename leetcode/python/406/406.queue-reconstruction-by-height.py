#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#
# https://leetcode.com/problems/queue-reconstruction-by-height/description/
#
# algorithms
# Medium (58.59%)
# Total Accepted:    68.7K
# Total Submissions: 117.3K
# Testcase Example:  '[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]'
#
# Suppose you have a random list of people standing in a queue. Each person is
# described by a pair of integers (h, k), where h is the height of the person
# and k is the number of people in front of this person who have a height
# greater than or equal to h. Write an algorithm to reconstruct the queue.
#
#
# Note:
# The number of people is less than 1,100.
#
#
#
#
# Example
#
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
#
#
#
class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # have height greater
        people = sorted(people)
        out = [None] * len(people)
        count = 0
        open = 0
        for el in people:
            out[el[1]-count] = el
            while out[open] is not None:
                open += 1
            count += 1
            print(out)
        return out


test = True
if test:
    s = Solution()
    Input = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2], [4,0]]

    # Output:
    # [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

    print(s.reconstructQueue(Input))

    # [[4, 4], [5, 0], [5, 2], [6, 1], [7, 0], [7, 1]]
    #                                  These two can be anywhere
    #                          This one must be after [7,0]
    #                  This one must be after [5,0] and [7,0]
    #          This one must be closer to the front but wrt 4
    # This one should be after 5,5,6,7
    #  no, it depends on the order of the others
    # - - - - 4
    # 5 - - - 4
    # 5 - 5 - 4
    # 5 - 5 6 4
    # 5 7 5 6 4
    # 5 7 5 6 4 7
