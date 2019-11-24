"""
About finite-state machine:
https://en.wikipedia.org/wiki/Finite-state_machine

The string pattern matching can be seen as running a FSM. For example,
you can use the following FSM to represent pattern a*c?b.  You always
start at state 0, and take each character of s as a "token". When a
token matches the label on a link, you can transfer from one state to
another via that link. * and ? are special tokens that can match any
token, or in other words, you can always transfer via a * or ? link
regardless of what token is fed from s. At the end, if you reach the
final state, called the accepting state (state 4 in our example), that
means you've got a match.  * and ? are slightly different: ? can match
only 1 character, which means after you transfer via a ? link, you
can't traverse it again, but after you transfer via a * link, you
still have access to it, infinitely. This is why a ? link takes you to
a new state, while a * link takes you back to where it starts, thus
this link can be traversed infinitely.  Due to the behavior of *
links, you may have access to multiple states from a certain
state. E.g. at state 1 below, with a token c you can transfer via the
c link and arrive at 2, or transfer via the * link to arrive back at
state 1. As a result, you can be at multiple states simultenaously
(think of parallel universes). Among all the states you "can be at",
you only need one of them being the accepting state to conclude a
successful match.

[[./fsm.png]]

The first for loop builds up a FSM from p. The states of the machine
are labeled as 0, 1, 2, ... The last state reached during the FSM
building is the accepting state.

The second for loop scans string s and run the FSM, by tracking what
state the machine is at, and what token is read from s. The * and ?
tokens are always available. Because you can be at multiple states at
the same time, in the second loop the state variable is a set of
integers, rather than a single integer.

Finally, if any of the state the FSM has reached matches the accepting
state, we can conclude s and p match, otherwise they don't match.

The first loop (FSM building) takes O(p) time. The second loop (string
scanning) iterates over s once, thus O(s) iterations. Overall there
are O(p+s) iterations. However, more strictly speaking in each
iteration of the for char in s loop, you also iterate through all
states you may be at (for at in state), which can be as many
interations as the number of *'s in p, which is bounded by p. Thus the
overall complexity in worst case is O(p+sp). If you believe the number
of *'s in p can be bounded by a constant, then the overall complexity
can be reduced to O(p+s).

The FSM diagram was drawn with Finite State Machine Designer - by Evan Wallace.
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        transfer = {}
        state = 0

        for char in p:
            if char == '*':
                transfer[state, char] = state
            else:
                transfer[state, char] = state + 1
                state += 1

        accept = state
        state = set([0])

        for char in s:
            state = set([
                transfer.get((at, token)) for at in state
                for token in [char, '*', '?']
            ])

        return accept in state
