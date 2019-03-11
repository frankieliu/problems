#!/usr/bin/env python
import sys
suma = sumb = 0
for ll in sys.stdin.readlines():
    x = ll.strip()
    a, b = [int(y) for y in x.split('/')]
    suma += a
    sumb += b
print(suma, sumb, suma/sumb)
