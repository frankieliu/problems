
Python AC solution O(n)

https://leetcode.com/problems/detect-capital/discuss/99254

* Lang:    python3
* Author:  lance5566
* Votes:   0

```
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word == word.upper() or word == word.lower():
            return True
        for letter in range(1,len(word)):
            if word[letter] == word[letter].upper():
                return False
        return True
        
```
The main reason why loop starts from 1 is 
because first letter is legal whenever it is uppercase or lowercase,
so we only detect from second letter.
