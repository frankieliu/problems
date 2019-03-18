
Tree solutions, 18-20 lines

https://leetcode.com/problems/add-and-search-word-data-structure-design/discuss/59576

* Lang:    python3
* Author:  StefanPochmann
* Votes:   39

    class WordDictionary:
    
        def __init__(self):
            self.root = {}
        
        def addWord(self, word):
            node = self.root
            for char in word:
                node = node.setdefault(char, {})
            node[None] = None
    
        def search(self, word):
            def find(word, node):
                if not word:
                    return None in node
                char, word = word[0], word[1:]
                if char != '.':
                    return char in node and find(word, node[char])
                return any(find(word, kid) for kid in node.values() if kid)
            return find(word, self.root)

An iterative alternative for the `search` method:

        def search(self, word):
            nodes = [self.root]
            for char in word:
                nodes = [kid
                         for node in nodes
                         for key, kid in node.items()
                         if char in (key, '.') and kid]
            return any(None in node for node in nodes)

And one that's a bit longer but faster:

        def search(self, word):
            nodes = [self.root]
            for char in word:
                nodes = [kid for node in nodes for kid in
                         ([node[char]] if char in node else
                          filter(None, node.values()) if char == '.' else [])]
            return any(None in node for node in nodes)

And a neat version where I append my end-marker to the word to simplify the final check:

    class WordDictionary:
    
        def __init__(self):
            self.root = {}
        
        def addWord(self, word):
            node = self.root
            for char in word:
                node = node.setdefault(char, {})
            node['$'] = None
    
        def search(self, word):
            nodes = [self.root]
            for char in word + '$':
                nodes = [kid for node in nodes for kid in
                         ([node[char]] if char in node else
                          filter(None, node.values()) if char == '.' else [])]
            return bool(nodes)
