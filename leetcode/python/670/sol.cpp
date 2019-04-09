
C++ One Pass O(n) and O(1) space, pure math, no string manipulation, Detailed explanation

https://leetcode.com/problems/maximum-swap/discuss/107098

* Lang:    cpp
* Author:  doutiger
* Votes:   1

```high``` is the bigger digit at the less significant bit to be swapped to a more significant bit.
```highBase``` is the base of the bit corresponding to ```high```.
```low``` is the smaller digit at a more significant bit to be swapped with ```high``` at a less significant bit.
```lowBase``` is the base of the bit corresponding to ```low```.

for example:
```2736```
```high```: 7
```highBase```: 100
```low```: 2
```lowBase```: 1000

the result would be: ```2736 + (7-2) * (1000-100) = 7236```

```
int maximumSwap(int num) {
        int temp = num, base = 1, high = 1, low = 1, lowBase = 1, highBase = 1, maxDigit = 0, maxBase = 1;
        while(temp > 0)
        {
            int current = temp % 10;
            if(current<maxDigit)
            {
                low = maxDigit;
                lowBase = maxBase;
                high = current;
                highBase = base;
            }
            if(current > maxDigit)
            {
                maxDigit = current;
                maxBase = base;
            }
            base *= 10;
            temp /= 10;
        }
        return num + (low-high)*(highBase-lowBase);
    }
```
