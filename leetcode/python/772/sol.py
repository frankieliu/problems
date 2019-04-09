
python3 well-organized solution (infix to postfix)

https://leetcode.com/problems/basic-calculator-iii/discuss/113601

* Lang:    python3
* Author:  willir29
* Votes:   0

```
import operator
from typing import List, Generator, Union


class Operation:
    def __init__(self, op: str):
        if op == '+':
            self._op = operator.add
            self._rank = 1
        elif op == '-':
            self._op = operator.sub
            self._rank = 1
        elif op == '*':
            self._op = operator.mul
            self._rank = 2
        elif op == '/':
            self._op = operator.floordiv
            self._rank = 2
        else:
            raise ValueError("Unknown operation: %s" % (op,))

    def get_rank(self) -> int:
        return self._rank

    def calc(self, arg1: int, arg2: int) -> int:
        return self._op(arg1, arg2)


class Bracket:
    def __init__(self, br: str):
        self._br = br

    def is_close(self) -> bool:
        return self._br == ')'


Token = Union[int, Operation, Bracket]
TokensIt = Generator[Token, None, None]


def lexer(s: str) -> 'TokensIt':
    n = len(s)
    i = 0
    while i < n:
        c = s[i]
        i += 1
        if c.isspace():
            continue
        elif c.isdigit():
            next_tok_i = next((j for j in range(i, n) if not s[j].isdigit()),
                              n)
            yield int(s[i - 1: next_tok_i])
            i = next_tok_i
        elif c in ['(', ')']:
            yield Bracket(c)
        else:
            yield Operation(c)


def infix_to_postfix(tokens: 'TokensIt') -> 'TokensIt':
    st = []  # type: List[Operation]

    def pop_higher_rank(cur_rank: int) -> 'TokensIt':
        while st and st[-1].get_rank() >= cur_rank:
            yield st.pop()

    try:
        while True:
            token = next(tokens)
            if isinstance(token, int):
                yield token
            elif isinstance(token, Operation):
                yield from pop_higher_rank(token.get_rank())
                st.append(token)
            else:
                assert isinstance(token, Bracket)
                if token.is_close():
                    break
                else:
                    yield from infix_to_postfix(tokens)

    except StopIteration:
        pass

    yield from pop_higher_rank(0)


def eval_postfix(tokens: 'TokensIt') -> int:
    st = []  # type: List[int]

    for token in tokens:
        if isinstance(token, int):
            st.append(token)
        else:
            assert isinstance(token, Operation)
            arg2 = st.pop()
            arg1 = st.pop()
            st.append(token.calc(arg1, arg2))

    return st.pop()


class Solution:
    @staticmethod
    def calculate(s: str) -> int:
        infix = lexer(s)
        postfix = infix_to_postfix(infix)
        return eval_postfix(postfix)
```

That solution is more verbose than others, but it is much clearer (from my point of view), and that is how I would probably solve such problem in the real world (Considering I can't use `flex`/`bison` or other parser generators).

Here I use infix to postfix transformation. And then I evaluate postfix. Such transformation is well described in https://discuss.leetcode.com/topic/15761/accepted-java-infix-to-postfix-based-solution-with-explaination-600ms. Though I use explicit recursion to handle brackets since I think it is easier to read and understand.
