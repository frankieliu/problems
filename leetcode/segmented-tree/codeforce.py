def build(t, n):
    for i in range(0, len(n)):
        t[i+len(n)] = n[i]
    for i in range(len(n)-1, 0, -1):
        t[i] = t[i<<1] + t[i<<1|1]

def update1(t, p, val):
    n = len(t)//2
    p += n
    t[p] = val   # put at the value
    while p > 1:
        t[p>>1] = t[p] + t[p^1]
        p >>= 1

def query(t, l, r):  # interval [l, r)
    n = len(t)//2
    res, l, r = 0, l+n, r+n
    while l<r:
        if (l&1):
            res += t[l]
            l += 1
        if (r&1):
            r -= 1
            res += t[r]
        print(l, r, l >> 1, r >> 1)
        l >>= 1
        r >>= 1
        print(res)
    return res

def main():
    # t = map(int, input().split())
    n = range(0,16)
    t = [0] * (len(n) << 1)
    build(t, n)
    print(t)
    update1(t,0,1)
    print(t)
    print(query(t,3,11))

main()
(3+10)*(4)
