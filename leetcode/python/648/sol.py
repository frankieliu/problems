
Easy Python Solution, 6 Lines

https://leetcode.com/problems/replace-words/discuss/105811

* Lang:    python3
* Author:  oliveoobe
* Votes:   7

Iterate through the dict and then iterate through sentence to see if it starts with the prefix. If it does, replace it.
```
class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        setenceAsList = sentence.split(" ")
        for i in range(len(setenceAsList)):
            for j in dict:
                if setenceAsList[i].startswith(j):
                    setenceAsList[i] = j
        return " ".join(setenceAsList)
```
