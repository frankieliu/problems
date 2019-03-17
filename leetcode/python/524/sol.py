
Python O(mn) Time, O(n) space, pointer based solution,122ms, beats 98%

https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/discuss/99589

* Lang:    python3
* Author:  s_coder
* Votes:   5

Record positions of how many characters in each word occurred. 
Use a map of lists from a-z to keep track of which words are waiting for what character.
When a pointer moves to end of a word, compare with current maximum.

```
class Solution(object):
    def findLongestWord(self, s, d):
        waiting = {}
        for c in 'abcdefghijklmnopqrstuvwxyz':
            waiting[c] = []
            
        for word in d:
            # add pointor to beginning of each word
            waiting[word[0]].append((word, 0))
        
        max_len = (0, "")
        for c in s:
            words = waiting[c]
            waiting[c] = [] # clean waiting words for that character
            for word, idx in words:
                if idx+1 >= len(word):
                    # finished word
                    # use min and negative length to get maximum length then min word
                    max_len = min(max_len, (-len(word), word)) 
                else:
                    # move pointer to next word
                    next_c = word[idx+1]
                    waiting[next_c].append((word, idx+1))
        return max_len[1]
```
