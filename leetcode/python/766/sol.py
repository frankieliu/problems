
easy way with python

https://leetcode.com/problems/toeplitz-matrix/discuss/113393

* Lang:    python3
* Author:  li5226966
* Votes:   0

check if the i-th line without last element and the i+1-th line without first element are the same for i in length :matrix[0]-1
'''
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(len(matrix)-1):
            if matrix[i][:-1] != matrix[i+1][1:]:
                return False
        return True
'''
the code can be simplier but i think it is clearly to read
