#!/usr/bin/env python
import sys
aline = int(sys.argv[1])
bline = int(sys.argv[2])

count = 1
a = b = None
for ll in sys.stdin.readlines():
    if count == aline:
        a = ll.strip().split()
        a = int(a[-1])
    elif count == bline:
        b = ll.strip().split()
        b = int(b[-1])
    count += 1
print(a-b)
