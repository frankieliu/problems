
Python one-line clear solution without loop and ifelse

https://leetcode.com/problems/power-of-four/discuss/80645

* Lang:    python3
* Author:  J.R.Smith
* Votes:   8

    return num>0 and num&(num-1)==0 and len(bin(num)[3:])%2==0
