
Clean Python DFS with comments

https://leetcode.com/problems/expression-add-operators/discuss/71968

* Lang:    python3
* Author:  zhuyinghua1203
* Votes:   36

dfs() parameters:  
num:   remaining num string  
temp:  temporally string with operators added  
cur:     current result of "temp" string  
last:     last multiply-level number in "temp". if next operator is "multiply", "cur" and "last" will be updated  
res:      result to return

    def addOperators(self, num, target):
        res, self.target = [], target
        for i in range(1,len(num)+1):
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res) # this step put first number in the string
        return res

    def dfs(self, num, temp, cur, last, res):
        if not num:
            if cur == self.target:
                res.append(temp)
            return
        for i in range(1, len(num)+1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], temp + "+" + val, cur+int(val), int(val), res)
                self.dfs(num[i:], temp + "-" + val, cur-int(val), -int(val), res)
                self.dfs(num[i:], temp + "*" + val, cur-last+last*int(val), last*int(val), res)
