
Python solution: Paper and pen method

https://leetcode.com/problems/convert-a-number-to-hexadecimal/discuss/89270

* Lang:    python3
* Author:  sumitmcc
* Votes:   0

```
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        tot = ""
        if num == 0: return "0"
        if num<0: num = 0xffffffff+1+num
        while num:
            #adding = num%16
            #num = num/16
            num,adding = divmod(num,16)
            tot+= str(adding if adding<10 else unichr(ord('a')+(adding%10)))
        
        return tot[::-1]
