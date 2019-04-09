
python solution beat 100%  with 中文解释

https://leetcode.com/problems/reach-a-number/discuss/257741

* Lang:    python3
* Author:  le0192
* Votes:   0

```
# \u601D\u8DEF\uFF1A
1. target \u6B63\u8D1F\u53F7\u4E0D\u5F71\u54CD\u7ED3\u679C
2. \u5047\u8BBE\u6240\u6709\u7684step\u90FD\u5411\u53F3\u7684\u548C\u4E3As\uFF0C\u8FD9\u65F6\u8F6C\u6362\u4E00\u4E2A\u6570\u5B57n\u5411\u5DE6\uFF0C\u5373\u51CF\u53BB\u8FD9\u4E2A\u6570\u5B57\u7684\u4E24\u500D\uFF08s - 2 * n\uFF09
3. \u6700\u591A\u53EA\u6709\u4E00\u4E2A\u6570\u5B57\u5411\u5DE6\uFF0C\u5373\u53EF\u8FBE\u5230target
4. \u56E0\u4E3A s \u9700\u8981\u51CF\u53BB\u4E00\u4E2A\u5076\u65702*n\uFF0C\u6240\u4EE5target \u4E0E s \u5FC5\u987B\u540C\u4E3A\u5076\u6570\uFF0C\u6216\u8005\u5947\u6570
5. \u5B8C\u6210
class Solution(object):
    def reachNumber(self, target):
        target = abs(target)
        n = int(math.ceil(math.sqrt(1 + 8 * target)/2 - 0.5))  # \u4E00\u5143\u4E8C\u6B21\u65B9\u7A0B\u7684\u89E3
        while target % 2 != n * ( n + 1 ) / 2 % 2:  # \u540C\u4E3A\u5947\u6570/\u5076\u6570
            n += 1
        return n
```
