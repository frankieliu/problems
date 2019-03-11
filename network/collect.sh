#!/bin/bash
d=$(date -r c-5021.txt '+%Y-%m-%d-%H-%M-%S')
outfile=client-${d}.log
cat $(ls c-*.txt | sort)  > $outfile
grep 0.00-10. $outfile
