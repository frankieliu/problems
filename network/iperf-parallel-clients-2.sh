#!/bin/bash
# from kb-dev-0a

snmp_log_file=snmp2.log
./snmp.sh > $snmp_log_file

# start with a different base address
./iperf-parallel.sh -B 5030 10 c -c 192.168.16.105 -u -b 0

sleep 3
for pid in $(seq 5031 5040); do
    pidfile=c-${pid}.pid
    x=$(cat $pidfile)
    # wait $x
    tail --pid=$x -f /dev/null
    rm $pidfile
done

./snmp.sh >> $snmp_log_file
