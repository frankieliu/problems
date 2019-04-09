
Puzzeled with the output

https://leetcode.com/problems/tenth-line/discuss/55540

* Lang:    bash
* Author:  da_pei_ge
* Votes:   0


num=0
for str in `head -10  file.txt`
do
    num=$[num+1]
    if [ $num -eq 10 ]
    then 
          echo $str
    fi
done


----------


result:
\
tenthline , why my output starts with a '\
'? Anyone can help me ?
