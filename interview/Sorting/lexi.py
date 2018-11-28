def solve(arr):
    c = {}
    v = {}
    for A in arr:
        a, b = A.split(" ");
        if a in c:
            c[a] += 1
            if b > v[a]:
                v[a] = b
        else:
            c[a] = 1
            v[a] = b

    out = []
    for a, b in c.items():
        out.append("{}:{},{}".format(a, b, v[a]))
    return out



arr = [
  "key1 abcd",
  "key2 zzz",
  "key1 hello",
  "key3 world",
  "key1 hello"
]
solve(arr)
