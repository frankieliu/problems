
Easy to understand python solution

https://leetcode.com/problems/fizz-buzz/discuss/89955

* Lang:    python3
* Author:  yang_fan
* Votes:   0

Check each number in the list, and add the related string into a new list.
```
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ls=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:ls.append("FizzBuzz")
            elif i%3==0:ls.append("Fizz")
            elif i%5==0:ls.append("Buzz")
            else:ls.append(str(i))
        return ls
```
