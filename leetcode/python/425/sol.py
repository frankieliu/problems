
can anyone tell me why I get time limit exceeded error?

https://leetcode.com/problems/word-squares/discuss/91358

* Lang:    python3
* Author:  physheng
* Votes:   0

Trie + backtracking

```
class TrieNode():
    def __init__(self):
        self.isEnd = False
        self.children = [None]*26

class Trie():
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        cur = self.root
        for c in word:
            idx = ord(c)-ord('a')
            if cur.children[idx]==None:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.isEnd = True
        
    def find_by_prefix(self,cur_node,prefix,cur_string,candidates):
        if cur_node.isEnd:
            candidates.append(cur_string)
            return
        for c in prefix:
            idx = ord(c)-97
            if cur_node.children[idx]==None:
                return 
            cur_node = cur_node.children[idx]
        for i,child in enumerate(cur_node.children):
            if child:
                c = chr(97+i)
                self.find_by_prefix(child,"",cur_string+c,candidates)

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        res = []
        vocab = Trie()
        K = len(words[0])
        for word in words:
            vocab.insert(word)
        self.helper(K,words,vocab,[],res)
        return res
        
    def helper(self,K,words,vocab,cache,res):
        if not words:
            return
        if len(cache)==K:
            res.append([]+cache)
            return
        level = len(cache)
        for word in words:
            cache.append(word)
            prefix = ""
            if level<K-1:
                for s in cache:
                    prefix += s[level+1]
            candidates = []
            vocab.find_by_prefix(vocab.root,prefix,prefix,candidates)    
            self.helper(K,candidates,vocab,cache,res)
            cache.pop()
                
```
