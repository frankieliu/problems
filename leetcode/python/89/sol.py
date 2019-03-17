
Python Easy Bit Manipulation Solution

https://leetcode.com/problems/gray-code/discuss/30007

* Lang:    python3
* Author:  girikuncoro
* Votes:   6

For n=1: 0 1

For n=2: 00 01 11 10

Notice that the second half (11 and 10) are mirror of the first half (0 1) with additional 1 before it (10 11).
Now we have (00 01 11 10), in order to do n=3 we need to do the same. The 4 elements of n=2 will be our first half, to do the second half we mirror them to get (10 11 01 00) and add additional 1 before it (110 111 101 100). We get:

For n=3: 000 001 011 010 110 111 101 100


    def grayCode(n):
        if not n:
            return [0]
        res = [0,1]
        for i in range(2,n+1):
            for j in range(len(res)-1,-1,-1):
                res.append(res[j] | 1<<i-1)
        return res
