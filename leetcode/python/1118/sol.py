In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1118.number-of-days-in-a-month.algorithms.json

Python easy understand solution

https://leetcode.com/problems/number-of-days-in-a-month/discuss/342427

* Lang:    python
* Author:  formatmemory
* Votes:   1

The key is to determin the target year is leap year or not. For those who are not familliar with the concept of leap year: https://en.wikipedia.org/wiki/Leap_year. 
So there is one more day in February for leap year. 

```
    def numberOfDays(self, Y: int, M: int) -> int:
        up = [1,3,5,7,8,10,12]
        
        if M < 1 or M > 12:
            return 0
        else:
            if M == 2:
                return 29 if self.is_leap_year(Y) else 28
            else:
                return 31 if M in up else 30

    def is_leap_year(self, y):
		"""
        Leap Year:
            1.The year can be evenly divided by 4;
            2.If the year can be evenly divided by 100, it is NOT a leap year, unless;
            3.The year is also evenly divisible by 400. Then it is a leap year.
		"""
        if y%4:
            return False
        elif y%100 != 0:
            return True
        elif y%400 != 0:
            return False
        else:
            return True
```

Analysis: 
	time: O(1), space: O(1)
