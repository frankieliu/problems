#!/bin/bash
# from kb-dev-0a
./snmp.sh > snmp.log
./iperf-parallel.sh 10 c -c 192.168.16.105 -u -b 0
sleep 3
for pid in *.pid; do
    x=$(cat $pid)
    # wait $x
    tail --pid=$x -f /dev/null
    rm $pid
done
./snmp.sh >> snmp.log
