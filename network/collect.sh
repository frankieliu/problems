#!/bin/bash
d=$(date -r c-5021.txt '+%Y-%m-%d-%H-%M-%S')
outfile=client-${d}.log
sumfile=client-summary-${d}.log
cat $(ls c-*.txt | sort)  > $outfile
grep 0.00-10. $outfile > $sumfile
cat $sumfile | awk '{print $11;}' | ./sum-lost-total.py
outpkts=$(cat snmp.log | ./diff-lines.py 6 2)
inpkts=$(cat snmp.log | ./diff-lines.py 7 3)
echo $inpkts $outpkts $(($inpkts-$outpkts))
