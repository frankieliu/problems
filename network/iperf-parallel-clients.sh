#!/bin/bash
# Run multiple parallel instances of iperf client
# Assumes iperf servers have been started, e.g.
# iperf -s -p PORT
# Examples:
# Run 5 clients for 60 seconds to server 1.1.1.1
#    iperf-multiple-clients 1.1.1.1 5 60 report
# 5 files will be created, report-1.1.1.1-5001-60.txt, ...
#
# Run 7 clients for 20 seconds with UDP 
#    iperf-multipleclients 1.1.1.1 7 20 report-udp -u -b 10M

# Assumes the port numbers used by the servers start at 5001 and increase
# e.g. 5001, 5002, 5003, ...
# If you want something different, then change the following parameter value
# to be: firstport - 1
base_port=5020

# Command line input: server IP address
# E.g. 1.1.1.1
server_ip=$1
shift

# Command line input: number of clients to start
# E.g. 5
num_clients=$1
shift

# Command line input: test duration
# E.g. 60
# test_duration=$1
# shift

# Command line input: base report file name
# E.g. report
report_base=$1
shift

# Optional command line input: other iperf options
# E.g. -u -b 10M
iperf_options="$*"

# Run iperf multiple times
for i in `seq 1 $num_clients`; do

	# Set server port
	server_port=$(($base_port+$i));

	# Report file includes server ip, server port and test duration
	# report_file=${report_base}-${server_ip}-${server_port}-${test_duration}.txt
    report_file=${report_base}-${server_ip}-${server_port}.txt

	# Run iperf
	#iperf -c $server_ip -p $server_port -t $test_duration $iperf_options &> $report_file &
    iperf3 -c $server_ip -p $server_port $iperf_options &> $report_file &

done
