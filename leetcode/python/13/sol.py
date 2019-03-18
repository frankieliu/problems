
Share python code

https://leetcode.com/problems/roman-to-integer/discuss/6900

* Lang:    python3
* Author:  hellofuture
* Votes:   7

<br>The main problem is to deal with the special numbers "IV","IX","XL","XC","CD","CM",for in these numbers "I","X","C" have the unusual meaning(subtract not plus).
<br>If given a Roman without numbers mentioned above,we can easily get the result by plusing all the numbers from right to left .
<br>So we need to find out what "I","X","C" mean when they appear(mean plus or subtract).
<br>"I" for example,the symbol "I" only appear in following circumstances:<br>"I","II","III","VI",VII","VIII","IV","IX","XI"\xb7\xb7\xb7\xb7(omitting "IIII" for it is special) .
<br>We can figure out that when we plus the symbols from left to right. If sum>=5,then the "I" we get can only mean "-1".Otherwise,it means "+1".The same is true with "X" and "C".

Code:

    class Solution:
        # @return an integer
        def romanToInt(self, s):
            result=0
            dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
            for i in s[-1::-1]:
                symbol=1
                if (i in ['I','X','C']) and result>=5*dic[i]:
                    symbol=-1
                result+=dic[i]*symbol
            return result
