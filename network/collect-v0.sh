#!/bin/bash

# client files
d=$(date -r c-5021.txt '+%Y-%m-%d-%H-%M-%S')
outfile=client-${d}.log
sumfile=client-summary-${d}.log
sumfile2=client-summary-2-${d}.log
cat $(ls c-*.txt | sort)  > $outfile
grep 0.00-10. $outfile > $sumfile

echo lost total loss/total > $sumfile2
cat $sumfile | awk '{print $11;}' | ./sum-lost-total.py >> $sumfile2

# snmp part
snmp_log_file=snmp1.log
outpkts=$(cat ${snmp_log_file} | grep ifHCOutUcastPkts.38 | ./diff-lines.py 2 1)
inpkts=$(cat ${snmp_log_file} | grep ifHCInUcastPkts.2 | ./diff-lines.py 2 1)
outdiscs=$(cat ${snmp_log_file} | grep ifOutDiscards.38 | ./diff-lines.py 2 1)
indiscs=$(cat ${snmp_log_file} | grep ifInDiscards.2 | ./diff-lines.py 2 1)

echo InPkts $inpkts OutPkts $outpkts InPtks-OutPkts $(($inpkts-$outpkts)) >> $sumfile2
echo InDiscards $indiscs OutDiscards $outdiscs >> $sumfile2

cat $sumfile
cat $sumfile2
