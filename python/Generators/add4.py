# figure out the recursion level
# this will give maximum recursion depth exceeded

from inspect import getouterframes, currentframe
# Counts up
def count(m):
    level = len(getouterframes(currentframe()))
    yield (m,level)
    yield from count(m+1)

a = count(3)
try:
    for i in range(10000):
        print(next(a))
except Exception as e:
    print(e)
