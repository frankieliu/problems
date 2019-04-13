
Iterative and Recursive Python

https://leetcode.com/problems/factor-combinations/discuss/68044

* Lang:    python3
* Author:  StefanPochmann
* Votes:   28

**Iterative:**

    def getFactors(self, n):
        todo, combis = [(n, 2, [])], []
        while todo:
            n, i, combi = todo.pop()
            while i * i <= n:
                if n % i == 0:
                    combis += combi + [i, n/i],
                    todo += (n/i, i, combi+[i]),
                i += 1
        return combis

"""
combi = []
find the next divisor, say 2

while loop through all 2 combos
combis += [2, n/2]  (n/2, 2, [2])
combis += [3, n/3]  (n/3, 3, [3])
combis += [5, n/5]  (n/5, 5, [5])

while loop through all 3 combos
combis += [2, 2, n/4]  (n/2, 2, [2, 2])
combis += [2, 3, n/6]  (n/6, 3, [2, 3])
combis += [2, 5, n/10] (n/10, 5, [2, 5])

Keep going until there there is nothing added
"""

**Recursive:**

    def getFactors(self, n):
        def factor(n, i, combi, combis):
            while i * i <= n:
                if n % i == 0:
                    combis += combi + [i, n/i],
                    factor(n/i, i, combi+[i], combis)
                i += 1
            return combis
        return factor(n, 2, [], [])
