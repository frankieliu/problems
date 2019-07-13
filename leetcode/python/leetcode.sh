#!/bin/bash
shopt -s extglob

function exists_and_nonzero () {
    x="$1"
    echo Checking if '"'$x'"' exists and is nonzero
    [ -e $x ] && [ ! -s $x ]
}

function select_language () {
    x=$1
    local lang
    if grep -q "Not supported language" $x; then
        line=$(grep "Supported languages" $x)
        if echo $line | grep -q "python"; then
            lang=python
        elif echo $line | grep -q "mysql"; then
            lang=mysql
        elif echo $line | grep -q "bash"; then
            lang=bash
        elif echo $line | grep -q "java"; then
            lang=java
        elif echo $line | grep -q "cpp"; then
            lang=cpp
        elif echo $line | grep -q "c"; then
            lang=c
        else
            lang=""
        fi
    fi
    echo $lang
}

function my_sol() {
    x=$1

    # make original directory
    if [ ! -d $x/original ]; then
        echo mkdir -p $x/original             # make the directory
        if [ -z $dryrun ]; then
            mkdir -p $x/original
        fi
    fi

    # put the result in the directory
    file=$(find $x -name "${x}*.(py|sh|sql)" -print -quit)
    if [[ $file == "" ]] || [ ! -s $file ]; then
        echo leetcode show -gx -o $x/ $x
        if [ -z $dryun ]; then
            leetcode show -gx -o $x/ $x > >(tee sout.log) 2> >(tee serr.log)
            lang=$(select_language sout.log)
            if [[ $lang != "" ]]; then
                echo leetcode show -gx -l $lang -o $x/ $x
                leetcode show -gx -l $lang -o $x/ $x > >(tee sout.log) 2> >(tee serr.log)
            fi
        fi
    fi

    # save a copy in original directory
    file=$(find $x/original -name "${x}*.(py|sh|sql)" -print -quit)
    if [[ $file == "" ]] || [ ! -s $file ]; then
        echo leetcode show -gx -o $x/original/ $x
        if [ -z $dryun ]; then
            leetcode show -gx -o $x/original/ $x > >(tee sout.log) 2> >(tee serr.log)
            lang=$(select_language sout.log)
            if [[ $lang != "" ]]; then
                echo leetcode show -gx -l $lang -o $x/original/ $x
                leetcode show -gx -l $lang -o $x/original/ $x > >(tee sout.log) 2> >(tee serr.log)
            fi
        fi
    fi

    # save solution
    if [ $solution -eq 1 ]; then
        file=$(find $x -name "sol.(py|sh|sql)" -print -quit)
        if [[ $file == "" ]] || grep -q ERROR $file; then
            echo leetcode show $x --solution '>' $x/sol.py
            if [ -z $dryrun ]; then
                leetcode show $x --solution > $x/sol.py 2> >(tee serr.log)
                lang=$(select_language $x/sol.py)
                if [[ $lang != "" ]]; then
                    echo leetcode show -l $lang $x --solution '>' $x/sol.py
                    leetcode show -l $lang $x --solution > $x/sol.py 2> >(tee serr.log)
                fi

            fi
        fi
    fi
}

usage() {
    echo "Clear leetcode cache first: leetcode cache -d"
    echo "Usage: $0 [-b <begin>] [-e <end>] [-p <number>] [-n (dryrun)] [-s (skip solution)]" 1>&2; exit 1; }
solution=1
while getopts ":b:e:snp:" o; do
    case "${o}" in
        b)
            b=${OPTARG}
            ;;
        e)
            e=${OPTARG}
            ;;
        p)
            p=${OPTARG}
            ;;
        n)
            dryrun=1
            ;;
        s)
            solution=0
            ;;
        *)
            usage
            ;;
    esac
done
shift $((OPTIND-1))

if [ $b ] && [ $e ]; then
    echo "begin-end = ${b}-${e}"
    for x in $(seq ${b} ${e}); do
        my_sol $x
    done
elif [ $p ]; then
    my_sol $p
fi
