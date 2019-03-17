
Python 59ms with Regex, Fractions and LCM

https://leetcode.com/problems/fraction-addition-and-subtraction/discuss/103397

* Lang:    python3
* Author:  rtom09
* Votes:   0

```
from fractions import gcd
from fractions import Fraction
import re

class Solution(object):
    def fractionAddition(self, expression):
        def lcm(x, y):
            lcm = (x*y)//gcd(x,y)
            return lcm

        def lcmm(*args):
            return reduce(lcm, args)
        
        num = []
        denom = []
        
        m = re.findall("(([+|-]?\\d+)/(\\d+))", expression)
        for tup in m:
            num.append(int(tup[1].replace("+", "")))
            denom.append(int(tup[2]))
            
        mult = lcmm(*denom)
        sm = 0
        
        for i in xrange(len(denom)):
            num[i] *= mult / denom[i]
            sm += num[i]
        frc = str(Fraction(sm, mult))
        try:
            frc.index("/")
        except:
            frc += "/1"
        return frc
```
