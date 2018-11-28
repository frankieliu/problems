def remove_min(heap):
    return heap[0]


def insert_root(heap, elem):
    heap[0] = elem
    heapify(heap, 0)


def heapify(h, i):
    left = 2*i + 1
    right = 2*i + 2
    lh = len(h)
    smallest = i
    if left < lh and h[left] < h[i]:
        smallest = left
    if right < lh and h[right] < h[smallest]:
        smallest = right
    if smallest != i:
        h[i], h[smallest] = h[smallest], h[i]
        heapify(h, smallest)


def build_heap(a):
    la = len(a)//2
    for i in range(la, -1, -1):
        heapify(a, i)


def topK(arr, k):
    la = len(arr)

    if la <= k:
        h = arr
    else:
        h = arr[0:k]

    build_heap(h)

    for i in range(k, la):
        min = remove_min(h)
        if min < arr[i]:
            insert_root(h, arr[i])

    out = []
    lh = len(h)
    last = None
    while lh > 0:
        m = remove_min(h)
        if last == m:
            pass
        else:
            out.append(m)
            last = m
        print(h, out)
        if lh == 1:
            break
        bot = h[lh - 1]
        h = h[0:-1]
        insert_root(h, bot)
        lh -= 1

    return out


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
