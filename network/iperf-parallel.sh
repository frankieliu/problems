#!/bin/bash
# Run multiple parallel instances of iperf servers

# Get options
while getopts ":hB:" opt; do
  case ${opt} in
    h ) # process option h
    ;;
    B ) # process option b
        base_port=$OPTARG
        ;;
    : )
        echo "Invalid option: $OPTARG requires an argument" 1>&2
        ;;
    \? ) echo "Usage: cmd [-h] [-t]"
      ;;
  esac
done
shift $((OPTIND -1))

# Assumes the port numbers used by the servers start at 5001 and increase
# e.g. 5001, 5002, 5003, ...
# If you want something different, then change the following parameter value
# to be: firstport - 1
base_port=${base_port:-5020}

# Command line input: number of servers
# E.g. 5
num_servers=$1
shift

# Command line input: base report file name
# E.g. report
report_base=$1
shift

# Optional command line input: other iperf options
# E.g. -u
iperf_options="$@"

echo "     baseport : $base_port"
echo "  num_servers : $num_servers"
echo "  report_base : $report_base"
echo "iperf_options : $iperf_options"

# Create all windows
for i in `seq 1 $num_servers`; do
	server_port=$(($base_port+$i));
    title=P${server_port}
    tmux new-window -n $title
done
tmux select-window -t :0


# Run iperf multiple times
# Send command to each window
for i in `seq 1 $num_servers`; do
	# Set server port
	server_port=$(($base_port+$i));

	# Report file includes server port
	report_file=${report_base}-${server_port}.txt
    pid_file=${report_base}-${server_port}.pid

	# Run iperf
    title=P${server_port}
    cmd="iperf3 -p $server_port $iperf_options"
    echo "$cmd"
    tmux send-keys -t $title 'sh -c '"'"'echo $$ > '"$pid_file"'; exec '"$cmd"' &> '"$report_file""'" C-m
    tmux send-keys -t $title
done
