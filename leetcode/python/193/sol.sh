
1 Line Solution with Egrep and Regular Expression

https://leetcode.com/problems/valid-phone-numbers/discuss/55490

* Lang:    bash
* Author:  fabrizio3
* Votes:   0

    egrep -o "^(([0-9]{3}\\-)|(\\([0-9]{3}\\) )){1}[0-9]{3}\\-[0-9]{4}$" file.txt

 1. **egrep -o**: output the exact match
 2. **^**: match the beginning of line
 3. **([0-9]{3}\\\\-)**: match exactly 3 digits followed by '-', e.g. *xxx-*.
 4. **(\\\\([0-9]{3}\\\\) )**: match 3 digits between ( and ) followed by a single
    space, e.g. *(xxx)* .
 5. **(([0-9]{3}\\\\-)|(\\\\([0-9]{3}\\\\) )){1}**: combine the two previous matches from point 3 and 4:
    matches or 3 digits followed by '-', e.g. *xxx-*, or 3 digits between ( and )
    followed by a single space, e.g. *(xxx)* , exactly {1} time, because the phone number can be in the format *(xxx) xxx-xxxx* or *xxx-xxx-xxxx*.
 6. **[0-9]{3}\\\\-**: match exactly 3 digits followed by '-'
 7. **[0-9]{4}**: match exactly 4 digits
 8. **$**: match end of line
