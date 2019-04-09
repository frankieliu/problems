#!/bin/bash

beg=1
end=1015
for x in $(seq ${beg} ${end}); do
    echo leetcode show $x --solution '>' $x/sol.best
    leetcode show $x --solution > $x/sol.best 2> >(tee serr.log)
done
