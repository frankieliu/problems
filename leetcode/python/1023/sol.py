
[Java/C++/Python] O(S^2)

https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/discuss/260847

* Lang:    python
* Author:  lee215
* Votes:   23

## **Intuition**:

The construction of `S` is a NP problem,
it\'s time consuming to construct a short `S`.
I notice `S.length <= 1000`, which is too small to make a big `N`.

This intuition lead me to the following 1-line python solution,
which can be implemented very fast.
<br>

##**Explanation**:
Check if `S` contains binary format of `N`,
If so, continue to check `N - 1`.
<br>

## **Time Complexity**

1. Prove I, check number of substring

Pick two indices, there are at most `S^2` substrings,
so `S` can contains at most `S^2` integers
Time complexity upper bound `O(S^2)`


2. Prove II, Check the continuous digits
Meanwhile I know the interviewer and my reader won\'t be satisfied,
as they want no more "cheat".

Here I have a brief demonstration to give the time complexity an acceptable upper bound.

Have a look at the number 1001 ~ 2000 and their values in binary.

1001 0b1111101001
1002 0b1111101010
1003 0b1111101011
...
1997 0b11111001101
1998 0b11111001110
1999 0b11111001111
2000 0b11111010000



The number 1001 ~ 2000 have 1000 different continuous 10 digits.
The string of length `S` has at most `S - 9` different continuous 10 digits.
So `S <= 1000`, `N <= 2000`.

So `S * 2` is a upper bound for `N`.
If `N > S * 2`, we can return `false` directly.


It\'s the same to prove with the numbers 512 ~ 1511, or even smaller range.

Time complexity upper bound `O(S)`

<br>

**Java:**
```
    public boolean queryString(String S, int N) {
        for (int i = N; i > N / 2; --i)
            if (!S.contains(Integer.toBinaryString(i)))
                return false;
        return true;
    }
```
**C++**
```
    bool queryString(string S, int N) {
        for (int i = N; i > N / 2;  --i) {
            string b = bitset<32>(i).to_string();
            if (S.find(b.substr(b.find("1"))) == string::npos)
                return false;
        }
        return true;
    }
```
**Python:**
```
    def queryString(self, S, N):
        return all(bin(i)[2:] in S for i in xrange(N, N / 2, -1))
```

