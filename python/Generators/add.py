def count(m):
    yield m

a = count(10)
print(a.next)
print(a.next)

# generator object has no attribute 'next'
