#!/bin/bash
for x in $(seq 1 988); do
    if grep -q ERROR $x/sol.py; then
        echo $x/sol.py
    fi
done
