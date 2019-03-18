
4-7 lines Python

https://leetcode.com/problems/generate-parentheses/discuss/10096

* Lang:    python3
* Author:  StefanPochmann
* Votes:   131

`p` is the parenthesis-string built so far, `left` and `right` tell the number of left and right parentheses still to add, and `parens` collects the parentheses.

**Solution 1**

I used a few "tricks"... how many can you find? :-)

    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right:    parens += p,
            return parens
        return generate('', n, n)

**Solution 2**

Here I wrote an actual Python generator. I allow myself to put the `yield q` at the end of the line because it's not that bad and because in "real life" I use Python 3 where I just say `yield from generate(...)`.

    def generateParenthesis(self, n):
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p + '(', left-1, right): yield q
                for q in generate(p + ')', left, right-1): yield q
        return list(generate('', n, n))

**Solution 3**

Improved version of [this](https://leetcode.com/discuss/25725/7-lines-in-python-44-ms). Parameter `open` tells the number of "already opened" parentheses, and I continue the recursion as long as I still have to open parentheses (`n > 0`) and I haven't made a mistake yet (`open >= 0`).

    def generateParenthesis(self, n, open=0):
        if n > 0 <= open:
            return ['(' + p for p in self.generateParenthesis(n-1, open+1)] + \\
                   [')' + p for p in self.generateParenthesis(n, open-1)]
        return [')' * open] * (not n)
