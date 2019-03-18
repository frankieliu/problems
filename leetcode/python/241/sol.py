
1-11 lines Python, 9 lines C++

https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/66350

* Lang:    python3
* Author:  StefanPochmann
* Votes:   103

Just doing it...

---

**Solution 1** ... 48 ms

    def diffWaysToCompute(self, input):
       tokens = re.split('(\\D)', input)
       nums = map(int, tokens[::2])
       ops = map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2])
       def build(lo, hi):
           if lo == hi:
               return [nums[lo]]
           return [ops[i](a, b)
                   for i in xrange(lo, hi)
                   for a in build(lo, i)
                   for b in build(i + 1, hi)]
       return build(0, len(nums) - 1)

---

**Solution 2** ... 168 ms

One-liner inspired by [Soba](https://leetcode.com/discuss/48410/python-solution-52ms-with-simple-interpretation?show=48432#a48432).

    def diffWaysToCompute(self, input):
        return [eval(`a`+c+`b`)
                for i, c in enumerate(input) if c in '+-*'
                for a in self.diffWaysToCompute(input[:i])
                for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]

---

**Solution 3** ... 64 ms

Faster version of solution 2.

    def diffWaysToCompute(self, input):
        return [a+b if c == '+' else a-b if c == '-' else a*b
                for i, c in enumerate(input) if c in '+-*'
                for a in self.diffWaysToCompute(input[:i])
                for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]

---

**Solution 4** ... 188 ms

A code golf version of solution 2.

    diffWaysToCompute=d=lambda s,t:[eval(`a`+c+`b`)for i,c in enumerate(t)if
    c<'0'for a in s.d(t[:i])for b in s.d(t[i+1:])]or[int(t)]

---

**C++** ... 8 ms

C++ version of solution 3.

    vector<int> diffWaysToCompute(string input) {
        vector<int> output;
        for (int i=0; i<input.size(); i++) {
            char c = input[i];
            if (ispunct(c))
                for (int a : diffWaysToCompute(input.substr(0, i)))
                    for (int b : diffWaysToCompute(input.substr(i+1)))
                        output.push_back(c=='+' ? a+b : c=='-' ? a-b : a*b);
        }
        return output.size() ? output : vector<int>{stoi(input)};
    }
