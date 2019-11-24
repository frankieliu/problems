def gen1(n):
    for i in range(0,n):
        yield i

a = gen1(10)
peeked = None

def consume():
    global peeked,a
    try:
        if peeked is not None:
            tmp = peeked
            peeked = None
            return tmp
        else:
            return next(a)
    except StopIteration:
        return None

def peek():
    global peeked,a
    try:
        if peeked is None:
            peeked = next(a)
        return peeked
    except StopIteration:
        return None


for i in range(0,10):
    print("peek",peek())
    print("peek",peek())
    print("consume",consume())
    print("peek",peek())
    print("peek",peek())
