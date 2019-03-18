
Java/Python easy solution with explanation

https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/56719

* Lang:    python3
* Author:  dietpepsi
* Votes:   72

First let's think what does bitwise AND do to two numbers, for example ( 0b means base 2)

    4 & 7 = 0b100 & 0b111 = 0b100
    5 & 7 = 0b101 & 0b111 = 0b101
    5 & 6 = 0b101 & 0b110 = 0b100

The operator & is keeping those bits which is set in both number.

For several numbers, the operator & is keeping those bits which is 1 in every number.

In other word, a bit is 0 in any number will result in 0 in the answer's corresponding bit.

Now consider a range 

    [m = 0bxyz0acd, n=0bxyz1rst]

here xyzpacdrst all are digits in base 2.

We can find two numbers that are special in the range [m, n]

    (1) m' = 0bxyz0111
    (2) n' = 0bxyz1000

The bitwise AND of all the numbers in range [m, n] is just the bitwise AND of the two special number

    rangeBitwiseAnd(m, n) = m' & n' = 0bxyz0000

This tells us, the bitwise and of the range is keeping the common bits of m and n from left to right until the first bit that they are different, padding zeros for the rest. 

**Java**

    public int rangeBitwiseAnd(int m, int n) {
        int i = 0;
        for (; m != n; ++i) {
            m >>= 1;
            n >>= 1;
        }
        return n << i;
    }

    // 8266 / 8266 test cases passed.
    // Status: Accepted
    // Runtime: 8 ms

**Python**

    def rangeBitwiseAnd(self, m, n):
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i

    # 8266 / 8266 test cases passed.
    # Status: Accepted
    # Runtime: 208 ms
