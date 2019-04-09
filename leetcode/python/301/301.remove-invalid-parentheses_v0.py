#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#
# https://leetcode.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (38.03%)
# Total Accepted:    104.9K
# Total Submissions: 275.8K
# Testcase Example:  '"()())()"'
#
# Remove the minimum number of invalid parentheses in order to make the input
# string valid. Return all possible results.
#
# Note: The input string may contain letters other than the parentheses ( and
# ).
#
# Example 1:
#
#
# Input: "()())()"
# Output: ["()()()", "(())()"]
#
#
# Example 2:
#
#
# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
#
#
# Example 3:
#
#
# Input: ")("
# Output: [""]
#
#
class Solution:

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def prefix_count(a, c):
            for i, k in enumerate(a):
                if k != c:
                    break
            return i-1+1

        def maxlen(a):
            if len(a) > 1:
                ml = max(len(x) for x in a)
                return [x for x in a if len(x) == ml]
            return a

        def highlight(a, i):
            return a[0:i]+"_"+a[i]+"_"+a[i+1:]

        def __init__(self):
            self.mpar = [0]*10
            for i in range(len(self.mpar)):
                self.mpar[i] = [None]*10


        def par(s, i, lc):
            if self.mpar[i][lc]:
                return self.mpar[i][lc]

            if i == len(s):
                if lc == 0:
                    return [('', i)]
                else:
                    return False
            out = []
            el = s[i]
            if el == "(":
                take = par(s, i+1, lc+1)
                # print("1takecon", take, highlight(s, i), lc)
                if take is not False:
                    take = maxlen(take)
                    print("1take", take, highlight(s, i), lc)
                    out.extend([('('+x[0], i) for x in take])
                    # if take is False or ((i+1) < len(s) and s[i+1] != '('):

                    # consider a no take if len of take is small

                    # suppose take contains
                    # 0 "(" then forward to next symbol
                    # 1 "(" then forward past this
                    # 2 "(" then forward one

                    # There may be multiple takes to consider
                    c = prefix_count(take[0][0], "(")
                    print("Consider", take[0][1], highlight(s, take[0][1]-(c>0)*1), lc, c)
                    notake = par(s, take[0][1]-(c>0)*1, lc)
                    if notake:
                        print("Another possibility", notake)
                        if len(notake[0][0]) >= len(take[0][0]):
                            out.extend(notake)

                if take is False:
                    # We only do a no take if take is False
                    # for minimum number of changes
                    notake = par(s, i+1, lc)
                    # print("1notakecon", notake, highlight(s, i), lc)
                    if notake is not False:
                        print("1notakecon", notake, highlight(s, i), lc)
                        notake = maxlen(notake)
                        print("1notake", notake, highlight(s, i), lc)
                        out.extend([(x[0], x[1]) for x in notake])
                    else:
                        return False
            elif el == ")":
                if lc <= 0:
                    notake = par(s, i+1, lc)
                    if notake is not False:
                        notake = maxlen(notake)
                        print("2notake", notake, highlight(s, i), lc)
                        out.extend([(x[0], x[1]) for x in notake])
                    else:
                        return False
                elif lc > 0:
                    take = par(s, i+1, lc-1)
                    print("2takecon", take, highlight(s, i), lc)
                    if take is not False:
                        take = maxlen(take)
                        print("2take", take, highlight(s, i), lc)
                        out.extend([(')'+x[0], i) for x in take])
                    if take is False or ((i+1) < len(s) and s[i+1] != ')'):
                        notake = par(s, i+1, lc)
                        if notake is not False:
                            notake = maxlen(notake)
                            print("3notake", notake, highlight(s, i), lc)
                            out.extend([(x[0], x[1]) for x in notake])
                        else:
                            if take is False:
                                return False
                else:
                    return False
            else:
                rest = par(s, i+1, lc)
                if rest:
                    print("neither", rest, highlight(s, i), lc)
                    out.extend([(el+x[0], i) for x in rest])
                else:
                    return False
            maxl = max(out, key=lambda x: len(x[0]))
            maxll = len(maxl[0][0])
            out = [x for x in out if len(x[0]) == maxll]

            return out

        out1 = par(s, 0, 0)
        return maxlen([x[0] for x in out1]) if out1 is not False else [""]


test = True
if test:
    s = Solution()
    Input = "x("
    Input = "()())()"
    Input = ")()("
    Input = "(((k()(("
    Input = "(())("
    print(s.removeInvalidParentheses(Input))
