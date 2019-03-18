
simply python solution with 中文解释

https://leetcode.com/problems/interval-list-intersections/discuss/232866

* Lang:    python3
* Author:  le0192
* Votes:   1

```
class Solution(object):
    def intervalIntersection(self, A, B):
        """
        \u601D\u8DEF\uFF1A
        S\u8868\u793Astart\uFF0C E\u8868\u793Aend
        1. \u5EFA\u7ACB\u4E00\u4E2A\u6808s
        2. \u9047\u5230S\uFF0C\u5C06s\u5165\u6808\uFF0C\u9047\u5230E\uFF0Cs\u6700\u4E0A\u5C42pop\u51FA\u6765
        3. \u90A3\u4E48s\u6808\u5185\u5B58\u5728\u4E09\u79CD\u60C5\u51B5\uFF1A\u7A7A\uFF0C\u4E00\u4E2AS\uFF0C\u4E24\u4E2AS\uFF0C\u4E0D\u4F1A\u51FA\u73B0\u4E09\u4E2A\uFF08\u56E0\u4E3A\u63A5\u4E0B\u6765\u5FC5\u4F1A\u9047\u5230E\uFF09
        4. \u5982\u679Cs\u6808\u5185\u6709\u4E24\u4E2AS\uFF0C\u90A3\u4E48[S,E]\u662F\u4EA4\u96C6\uFF0C\u5982\u679C\u53EA\u4E00\u4E2AS\uFF0C\u90A3\u4E48\u4E0D\u662F\u4EA4\u96C6\uFF0C\u76F4\u63A5\u6254\u6389
        """
        if not A or not B:
            return []
        a = []
        b = []
        s = []
        ret = []
        # \u4E3A\u4E86\u4F7F\u7528\u6808\u7ED3\u6784\uFF0C\u53CD\u5411
        A.reverse()
        B.reverse()
        while (A or a) and (B or b):
            if not a:
                a = A.pop()
                # \u4E3A\u4E86\u4F7F\u7528\u6808\u7ED3\u6784\uFF0C\u5148start \u540Eend
                a = [a.end, a.start]
            if not b:
                b = B.pop()
                # \u4E3A\u4E86\u4F7F\u7528\u6808\u7ED3\u6784\uFF0C\u5148start \u540Eend
                b = [b.end, b.start]
            c = a 
            if a[-1] < b[-1]:
                c = a
            elif a[-1] > b[-1]:
                c = b
            else:
                # \u5982\u679C\u503C\u76F8\u7B49\u7684\u8BDD\uFF0C\u4F18\u5148\u4F7F\u7528start\uFF0C\u4E5F\u5C31\u662Flen()==2
                c = a if len(a)==2 else b
            if len(c)==2:
                s.append(c.pop())
            else:
                num = s.pop()
                num_end = c.pop()
                if len(s):
                    ret.append([num, num_end])
                else\uFF1A
                    # \u975E\u4EA4\u96C6\uFF0C\u6254\u6389
                    pass
        return ret
```
