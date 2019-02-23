class Solution(object):
    def lenLongestFibSubseq(self, A):
        index = {x: i for i, x in enumerate(A)}
        longest = collections.defaultdict(lambda: 2)
        print(longest[0,0])
        ans = 0
        for k, z in enumerate(A):
            for j in xrange(k):
                i = index.get(z - A[j], None)
                if i is not None and i < j:
                    print(i,j,k, [A[x] for x in [i,j,k]])
                    cand = longest[j, k] = longest[i, j] + 1
                    ans = max(ans, cand)
        return ans if ans >= 3 else 0

test = True
if test:
    import collections
    s = Solution()
    print(s.lenLongestFibSubseq([1,4,5,8,13]))
