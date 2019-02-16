#!/bin/bash
shopt -s extglob
file=+([1-9])*.py
echo python3 $file
sed -ie 's/test = False/test = True/' $file
python3 $file
