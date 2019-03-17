
Python simple solution

https://leetcode.com/problems/keyboard-row/discuss/230863

* Lang:    python3
* Author:  kishoreravi97
* Votes:   0

```
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        word_list=[]
        top_row=set(\'qwertyuiop\')
        mid_row=set(\'asdfghjkl\')
        bottom_row=set(\'zxcvbnm\')
        for word in words:
            if set(word.lower()).issubset(top_row) or set(word.lower()).issubset(mid_row) or set(word.lower()).issubset(bottom_row):
                word_list.append(word)
        return word_list
```
