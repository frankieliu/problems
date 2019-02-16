#!/bin/bash
for x in $(seq 1 988); do
         echo mkdir -p $x
         echo leetcode show -gx -o $x/ $x
         mkdir -p $x
         leetcode show -gx -o $x/ $x
done
