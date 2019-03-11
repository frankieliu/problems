#!/bin/bash
shopt -s extglob
file=$(ls +([0-9]).*.py)
a=$(tempfile)

echo cp $file save
cp $file save

echo mv $file $a
mv $file $a

echo cp $a $file
cp $a $file

sed -ie 's/test = True/test = False/' $file

echo leetcode submit $file
leetcode submit $file

echo mv $a $file
mv $a $file

echo Done.
