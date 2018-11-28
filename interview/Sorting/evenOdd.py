
def solve(a):
    ep = 0
    op = len(a) - 1
    cp = 0

    while cp < op:
        print(a, ep, op, cp)
        if a[cp] % 2 == 0:
            a[cp], a[ep] = a[ep], a[cp]
            cp += 1
            ep += 1
        else:
            a[cp], a[op] = a[op], a[cp]
            op -= 1
    return a

a= [8, 4, 9, 5, 2, 9, 5, 7, 10]
# a = list(range(0,5))
solve(a)
print(a)
