# Counts up
def count(m):
    yield m
    yield from count(m+1)

a = count(10)
try:
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
except Exception as e:
    print(e)
