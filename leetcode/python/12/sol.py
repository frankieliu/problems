
Share My Python Solution 96ms

https://leetcode.com/problems/integer-to-roman/discuss/6273

* Lang:    python3
* Author:  周园
* Votes:   62

    M = ["", "M", "MM", "MMM"];
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
    return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10];
