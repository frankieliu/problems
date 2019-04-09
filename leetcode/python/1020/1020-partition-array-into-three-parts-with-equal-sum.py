class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        s = sum(A)
        if s % 3 != 0:
            return False
        s3 = s // 3
        acc = 0
        found = 0
        for el in A:
            acc += el
            if acc == s3:
                found += 1
                s3 *= 2
        if found == 2:
            return True


test = True
if test:
    s = Solution()
    Input = [0,2,1,-6,6,-7,9,1,2,0,1]
    Input = [18,12,-18,18,-19,-1,10,10]
    print(s.canThreePartsEqualSum(Input))
