
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
