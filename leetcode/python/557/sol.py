
My 6-liner python solution

https://leetcode.com/problems/reverse-words-in-a-string-iii/discuss/101952

* Lang:    python3
* Author:  yang_fan
* Votes:   0

```
def reverseWords(self, s):
        s=s.split(' ')
        result=[]
        for word in s:
            word=word[::-1]
            result.append(word+' ')
        return ''.join(result)[:-1]
```
