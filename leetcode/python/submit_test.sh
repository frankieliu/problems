#!/bin/bash
shopt -s extglob
file=$(ls -t +([0-9]).*.py | head -1)
echo $file
