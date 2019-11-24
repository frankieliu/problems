class Solution:
    def minTransfers(self, trans):
        from collections import defaultdict, deque
        debt = defaultdict(int)
        for i, j, k in trans: debt[i] -= k; debt[j] += k
        debt = list(filter(None, debt.values()))
        print("Debt {}".format(debt))

        def SplitDebt():

            cset, Q = set(), deque([([0], debt[0])])

            # this is like a BFS
            print(Q)
            while Q:
                cset, csum = Q.popleft()
                print("cset: {}, csum: {}".format(cset, csum))
                # break at the first one for which csum == 0
                if csum == 0:
                    break
                print("Values: {}".format(list(range(cset[-1] + 1, len(debt)))))

                #
                for j in range(cset[-1] + 1, len(debt)):
                    Q.append((cset + [j], csum + debt[j]))
            if not cset: return False
            debt[:] = [debt[i] for i in set(range(len(debt))) - set(cset)]
            print("Debt: {}".format(debt))
            return True

        res = len(debt)
        while debt and SplitDebt():
            res -= 1
        return res















test = True
if test:
    sol = Solution()
    case = [False] * 0 + [True] + [False] * 2
    if case[0]:
        # Example 1:
        Input = [[0, 1, 10], [2, 0, 5]]
        # Output: 2
        print(sol.minTransfers(Input))
    if case[1]:
        # Example 2:
        Input = [[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]
        # Output: 1
        print(sol.minTransfers(Input))
