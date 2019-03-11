#
# @lc app=leetcode id=194 lang=bash
#
# [194] Transpose File
#
# https://leetcode.com/problems/transpose-file/description/
#
# shell
# Medium (22.13%)
# Total Accepted:    8.6K
# Total Submissions: 39K
# Testcase Example:  'a'
#
# Given a text file file.txt, transpose its content.
#
# You may assume that each row has the same number of columns and each field is
# separated by the ' ' character.
#
# Example:
#
# If file.txt has the following content:
#
#
# name age
# alice 21
# ryan 30
#
#
# Output the following:
#
#
# name alice ryan
# age 21 30
#
#
#
#
#
# Read from the file file.txt and print its transposed content to stdout.

while read -a line; do
    for ((i=0; i < "${#line[@]}"; i++)); do
        a[$i]="${a[$i]} ${line[$i]}"
    done
done < file.txt
for ((i=0; i < ${#a[@]}; i++)); do
    echo ${a[i]}
done
