
Python Simple Vanilla Trie

https://leetcode.com/problems/design-search-autocomplete-system/discuss/238226

* Lang:    python3
* Author:  leonmak
* Votes:   0

3 variables:
- `trie`: a nested dictionary, with leaf value node storing hot value
- `path`: a list, characters typed so far
- `curr`: a pointer to curr node in trie

move `curr` down a trie, appending characters to `path` and doing dfs for the query, getting hot values and sorting when done. When cannot go down trie anymore, save `curr` as None.

```python
class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.trie = dict()
        for s, t in zip(sentences, times):
            curr = self.trie
            for c in s:
                if c not in curr:
                    curr[c] = dict()
                curr = curr[c]
            curr[\'.\'] = t
            
        self.path = []
        self.curr = self.trie

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        # dfs and search from c as root
        res = []
        path = []
        
        def dfs(root):
            for c in root:
                if c == \'.\':
                    count = root[c]
                    sentence = prefix + \'\'.join(path)
                    res.append((-count, sentence))
                else:
                    path.append(c)
                    dfs(root[c])
                    path.pop()
        
        if c == \'#\':
            root = self.trie
            for char in self.path:
                if char not in root:
                    root[char] = dict()
                root = root[char]
            if \'.\' in root:
                root[\'.\'] += 1
            else:
                root[\'.\'] = 1
            self.path = []
            self.curr = self.trie
            return []
        else:
            self.path.append(c)
            prefix = \'\'.join(self.path)

            if self.curr and c in self.curr:
                dfs(self.curr[c])
                self.curr = self.curr[c]
                res.sort()
                return list(map(lambda (c, s): s, res))[:3]
            else: 
                self.curr = None
                return []
       
```
