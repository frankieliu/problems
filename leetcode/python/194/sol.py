
AC solution using Python3

https://leetcode.com/problems/transpose-file/discuss/55504

* Lang:    python3
* Author:  SmartHypercube
* Votes:   0

just share my simple solution
```
python3 <<EOF
matrix = [line[:-1].split(' ') for line in open('file.txt')]
for column in range(len(matrix[0])):
    print(*(matrix[row][column] for row in range(len(matrix))))
EOF
```
`<<EOF` is really a helpful syntax
