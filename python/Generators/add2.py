def count(m):
    yield m

a = count(10)
try:
    print(next(a))
    print(next(a))
except Exception as e:
    print(e)
