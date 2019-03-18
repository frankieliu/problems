
Python. Good solution. Both speed and memory

https://leetcode.com/problems/powerful-integers/discuss/246276

* Lang:    python3
* Author:  ali95
* Votes:   -1

I do not understand why they go through some unnecessary numbers until 18 in official solution. When we can just count and use the necessary amount of powers for both x and y. You will get it if you see my solution. Hope it helps!
```
class Solution:
    def powerfulIntegers(self, x, y, bound):
        answer = []
        cnt1 = 0
        cnt2 = 0
        while x**(cnt1+1) <= bound:
            if x == 1:
                break
            cnt1 += 1
        while y**(cnt2+1) <= bound:
            if y == 1:
                break
            cnt2 += 1
        for i in range(cnt1+1):
            for j in range(cnt2+1):
                if x**(i) +y**(j) <= bound:
                    answer.append((x**(i) +y**(j)))
        answer = set(answer)
        answer = list(answer)
        return (answer)



x = 1
y = 2
bound = 100
Solution().powerfulIntegers(x,y, bound)
```
