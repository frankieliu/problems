
Two Lines Python Solution With Explanation

https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/discuss/113238

* Lang:    python3
* Author:  fuxuemingzhu
* Votes:   0

You should define a function to verify a number is a prime number or not.
Then use this function to check all numbers between `L` and `R`.

In the `isPrime()` function, I use `1` when the number is prime number and `0` for not prime number. So I can easily use `sum()` to find how many prime numbers  between `L` and `R`.

```python
class Solution(object):
    def countPrimeSetBits(self, L, R):
        isPrime = lambda num : 0 if ((num == 1) or (num % 2 == 0 and num > 2)) else int(all(num % i for i in xrange(3, int(num ** 0.5) + 1, 2)))
        return sum(isPrime(bin(num)[2:].count('1')) for num in xrange(L, R+1))
```
