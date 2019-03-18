
One line python code using Map/Reduce

https://leetcode.com/problems/excel-sheet-column-number/discuss/52087

* Lang:    python3
* Author:  miaobupt
* Votes:   16

    def titleToNumber(self, s):
        return reduce(lambda x,y:x*26+y,map(lambda x:ord(x)-ord('A')+1,s))
