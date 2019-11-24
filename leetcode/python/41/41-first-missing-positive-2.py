class Solution:
    def firstMissingPositive(self, a: List[int]) -> int:
        n = len(a)
        for i in range(0,n):
            if 0 < a[i] < n+1:
                continue
            a[i] = n+1
        #print(a)
        for i in range(0, n):
            if abs(a[i]) == n+1:
                continue
            if a[abs(a[i])-1] < 0:
                continue
            a[abs(a[i])-1] = -a[abs(a[i])-1]
        #print(a)
        for i in range(0,n):
            if a[i] > 0:
                return i + 1
        return n+1
