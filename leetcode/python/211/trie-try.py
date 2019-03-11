class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node['$'] = None


a = WordDictionary()
a.addWord("apple")
print(a.root)

b = {}
c = b
for char in "apple":
    c = c.setdefault(char, {})
print(b)
