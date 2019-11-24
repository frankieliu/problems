class Solution:
    def firstMissingPositive(self, a: List[int]) -> int:
        if len(a) == 0: return 1
        n=len(a)
        for i in range(0, len(a)):
            while 0 < a[i] < n+1 and a[a[i]-1] != a[i]:
                el = a[i]
                a[i], a[el-1] = a[el-1], a[i]
        print(a)
        for i in range(0, len(a)):
            if a[i] != i+1:
                return i+1
        return n+1
