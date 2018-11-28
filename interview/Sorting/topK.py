from heapq import heapify, heappop, heappush


def topK(arr, k):
    '''Keep a sorted list
    insert an element into sorted list
    if there is an existing element do not insert
    if length of list is larger than k remove smallest element
    '''
    out = []
    if len(arr) <= 0:
        return out

    s = set()
    h = []

    for a in arr:
        if a in s:
            continue
        if len(h) < k:
            heappush(h, a)
            s.add(a)
        else:
            if a > h[0]:
                heappop(h)
                heappush(h, a)
                s.add(a)
    return(h)


arr = """11
4
8
9
6
6
2
10
2
8
1
2
9
"""
arr = [int(x) for x in arr.splitlines()]
la = arr[0]
k = arr[-1]
arr = arr[1:-1]
res = topK(arr, 9)
print(res)
