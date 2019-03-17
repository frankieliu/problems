
O(m*n) fast Python3 Solution

https://leetcode.com/problems/count-the-repetitions/discuss/241512

* Lang:    python3
* Author:  CharlotteGenius
* Votes:   1

The first function defined what "contain" is with O(n) complexity.
The second part is to find maximum m.
We first compute the quotient of two lengths and count down from this number.

For example:
if the length of S1 is 12, and S2\'s length is 3, the largest m could be 4, 
if 4*S2 can\'t satisfy the condition, then let m be 3, and check again.
This way, we only check 4 times at worst.

```
def Contain(L1,L2):
    for i in range(len(L2)):
        if L2[i] in L1:
            L1 = L1[L1.index(L2[i]):]
        else:
            return False
    return True

def getMaxRepetitions(s1,n1,s2,n2):
    S1 = s1*n1
    S2 = s2*n2
    M = int(len(S1)//len(S2))
    for m in range(M,1,-1):
        if Contain(S1,S2*m):
            return m
        
print(getMaxRepetitions(s1,n1,s2,n2))

```

I feel like my solution looks too simple... Did I understand this problem right?
