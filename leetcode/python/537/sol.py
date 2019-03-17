
Easy to understand python solution with explaination

https://leetcode.com/problems/complex-number-multiplication/discuss/100444

* Lang:    python3
* Author:  yang_fan
* Votes:   0

I use `partition` to split the string a and b, and then convert them to `int` type and calculate the result.
```
def complexNumberMultiply(self, a, b):
        a1,_,a=a.partition("+")
        a2,_,_=a.partition("i")
        b1,_,b=b.partition("+")
        b2,_,_=b.partition("i")
        a1,a2,b1,b2=int(a1),int(a2),int(b1),int(b2)
        result=[str(a1*b1-a2*b2),'+',str(a1*b2+a2*b1),'i']
        return ''.join(result)
```
