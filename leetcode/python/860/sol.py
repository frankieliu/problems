
Python easy solution using defaultdict

https://leetcode.com/problems/lemonade-change/discuss/244515

* Lang:    python3
* Author:  darkTianTian
* Votes:   0

```python
def lemonadeChange(self, bills: \'List[int]\') -> \'bool\':
    c = collections.defaultdict(int)
    for bill in bills:
        if bill == 10:
            c[5] -= 1
        elif bill == 20:
            if c[10] >= 1:
                c[10] -= 1
                c[5] -= 1
            else:
                c[5] -= 3
        if c[5] < 0:
            return False
        c[bill] += 1
    return True
```
