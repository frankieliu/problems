#!/bin/bash
function find_ext () {
    x=$1
    file=$(find $x -maxdepth 1 -regextype posix-extended -regex "$x/$x.*\.(py|sh|sql)" -print -quit)
    if [[ $file == *".sh" ]]; then
        echo bash sol.sh
    elif [[ $file == *".sql" ]]; then
        echo sql sol.sql
    elif [[ $file == *".py" ]]; then
        echo cpp sol.cpp
    fi
    echo ""
}

beg=1
end=1015
for x in $(seq ${beg} ${end}); do
    if [[ $(grep ERROR $x/sol.* | wc -l) == $(ls $x/sol.* | wc -l) ]]; then
        ext=$(find_ext $x)
        if [[ $ext != "" ]]; then
            lang=$(echo $ext | awk '{print $1}')
            fout=$(echo $ext | awk '{print $2}')
            echo leetcode show -l $lang $x --solution '>' $x/$fout
            leetcode show -l $lang $x --solution > $x/$fout 2> >(tee serr.log)
        else
            echo Not found for problem $x
        fi
    fi
done
