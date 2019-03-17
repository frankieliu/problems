
Python, simple to understand solution

https://leetcode.com/problems/monotone-increasing-digits/discuss/109787

* Lang:    python3
* Author:  bg1992
* Votes:   0

```
class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        num = str(N)
        if len(num) == 1: return N
        temp_num = num[0]
        last_increasing = 0
        for i in range(len(num)-1):
            if int(num[i]) < int(num[i+1]):
                last_increasing = i+1
                temp_num += num[i+1]
            elif int(num[i]) == int(num[i+1]):
                temp_num += num[i+1]
            else:
                return int(temp_num[:last_increasing] + str(int(temp_num[last_increasing])-1) + '9' * (len(num) - last_increasing - 1))
        return int(num)
```
We go through digits of the number, keeping in memory what is an index of last (most recent) increasing digit (last_increasing variable) - for instance, if we have input number: 2234455, then going through digits of this number, we receive indices = 2, 3, 5; respectively, for which digit at this index is greater than the previous one. If there are no such digits, last_increasing is assigned to 0.

If a digit is greater or equal than previous one, we add this digit to our string containing all digits till the moment.

In the opposite case, we return number, which is a conjunction of digits located left of last_increasing index, digit at the last_increasing index and 9s to the end of the length of the number. Let us explain the logic on the following number:

22333488677

As we can see, the answer returned by the code should be 22333479999. Due to fact behind the last 8 digit we have smaller number than 8, at the index of the first 8 we cannot put 8 to the returned number. We also cannot put greater digit, so it must be a digit reduced by one = 7. After we put 7 at this place, we feel free to fill out rest places with 9s.
