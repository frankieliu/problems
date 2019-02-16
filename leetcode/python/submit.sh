#!/bin/bash
shopt -s extglob
file=+([0-9]).*.py
echo leetcode submit $file
sed -ie 's/test = True/test = False/' $file
leetcode submit $file
