
Python, generators on a heap

https://leetcode.com/problems/super-ugly-number/discuss/76301

* Lang:    python3
* Author:  StefanPochmann
* Votes:   45

**Solution 1** ... ~550 ms (updated July 2016, originally was ~1570 ms)

Using generators and `heapq.merge`. Too bad there's no `itertools.unique`.

    def nthSuperUglyNumber(self, n, primes):
        uglies = [1]
        def gen(prime):
            for ugly in uglies:
                yield ugly * prime
        merged = heapq.merge(*map(gen, primes))
        while len(uglies) < n:
            ugly = next(merged)
            if ugly != uglies[-1]:
                uglies.append(ugly)
        return uglies[-1]

---

**Solution 2** ... ~500 ms (updated July 2016, originally was ~1400 ms)

Same thing done differently and it's a bit faster.

    def nthSuperUglyNumber(self, n, primes):
        uglies = [1]
        merged = heapq.merge(*map(lambda p: (u*p for u in uglies), primes))
        uniqed = (u for u, _ in itertools.groupby(merged))
        map(uglies.append, itertools.islice(uniqed, n-1))
        return uglies[-1]
