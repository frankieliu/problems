from collection import defaultdict


class Solution:

    def numSubmatrixSumTarget(self, m, target: int) -> int:

        def pref(x):
            asum = 0
            p = [0] * len(x)
            for i in range(len(x)):
                asum += x[i]
                p[i] = asum
            return p

        for i, r in enumerate(m):
            m[i] = pref(r)

        res = 0
        for i in range(0, len(m[0])):
            for j in range(i, len(m[0])):
                h = defaultdict(lambda: 0)
                h[0] = 1
                asum = 0
                for k in range(len(m)):
                    asum += (m[k][j] - m[k][i])
                    other = asum - target
                    if other in h:
                        res += h[other]
                    h[asum] += 1
        return res


test = True
if test:
    s = Solution()
    case = [True, False]
    if case[0]:
        print(s.numSubmatrixSumTarget())
    if case[1]:
        print(s.numSubmatrixSumTarget())
