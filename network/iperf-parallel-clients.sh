#!/bin/bash
# from kb-dev-09

snmp_log_file=snmp1TIME.log
./snmp.sh > ${snmp_log_file/TIME/before}

# start with a default base address 5020
./iperf-parallel.sh 10 c -c 192.168.16.105 -u -b 0

sleep 3
for pid in $(seq 5021 5030); do
    pidfile=c-${pid}.pid
    x=$(cat $pidfile)
    # wait $x
    tail --pid=$x -f /dev/null
    rm $pidfile
done

./snmp.sh > ${snmp_log_file/TIME/after}
