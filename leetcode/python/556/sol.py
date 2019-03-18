
Python 39ms O(n)

https://leetcode.com/problems/next-greater-element-iii/discuss/101821

* Lang:    python3
* Author:  Ellest
* Votes:   1

same idea as "next permutation." Start from back, find point where the previous digit is less than the current digit, look for the furthest right value that is greater than (which is also the smallest digit that is greater than) the previous digit, swap the two, then reverse the array from the current digit to the end. 

```
    def nextGreaterElement(self, n):
        if not n: return -1
        s = str(n)
        arr = [c for c in s]
        i = len(arr)-1
        while i > 0:
            prev = int(arr[i-1])
            if int(arr[i]) > prev:
                j = i
                # looking for right position to swap
                while j < len(arr) and int(arr[j]) > prev:
                    j += 1
                arr[i-1], arr[j-1], j = arr[j-1], arr[i-1], len(arr)-1
                # reverse array from pivot point til end
                while i < j:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1; j -= 1
                res = int(''.join(arr))
                # check 32 bit constraint
                return -1 if res > 2147483647 else res
            i -= 1
        return -1
```
