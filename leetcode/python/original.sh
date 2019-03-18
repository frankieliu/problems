#!/bin/bash
for x in $(seq 1 988); do
    echo mkdir -p $x/original
    echo mv $x/*.0.py $x/original
    mkdir -p $x/original
    mv $x/*.0.py $x/original
    # leetcode show -gx -o $x/ $x
    # leetcode show $x --solution > $x/sol.py
done
