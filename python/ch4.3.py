import json
import math

def addTree(a):
    if len(a) == 1:
        return a[0]
    elif len(a) == 0:
        return []
    else:
        mid = math.floor(len(a)/2)
        # print(a[mid], a[0:mid], a[mid+1:])
        return [a[mid], addTree(a[0:mid]), addTree(a[mid+1:])]

a = [i for i in range(0,10)]
t = addTree(a)
print(json.dumps(t, indent=4))
