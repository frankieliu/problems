#!/usr/bin/env python
import sys


class Node:
    def __init__(self, key, index, val):
        self.key = key
        self.index = index
        self.val = val

    def __str__(self):
        return "A[{}][{}]={}".format(self.key,
                                     self.index,
                                     self.val)


def lte_rel(a, b):
    return a.val <= b.val


def gt_rel(a, b):
    return a.val > b.val


def heapify(A, i, rel):
    left = 2*i + 1
    right = 2*i + 2
    largest = i
    if left < len(A) and rel(A[left], A[largest]):
        largest = left
    if right < len(A) and rel(A[right], A[largest]):
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, largest, rel)


def build_heap(A, rel):
    h = len(A) // 2
    for i in range(h, -1, -1):
        heapify(A, i, rel)


def print_heap(A, i=0, sp=0):
    left = 2*i + 1
    right = 2*i + 2
    lenx = len(A)
    print("{}{}".format(" "*sp, A[i].val))
    if left < lenx:
        print_heap(A, i=left, sp=sp+1)
    if right < lenx:
        print_heap(A, i=right, sp=sp+1)


def remove_min(A):
    return A[0]


def insert_root(A, val, rel):
    lenA = len(A)
    if val is None:
        if lenA >= 1:
            A[0] = A[lenA-1]
        else:
            pass
    else:
        A[0] = val
    heapify(A, 0, rel)


def find_order(arr):
    ''' check the first and last element of each least
    figure out order : will take o(k)
    '''
    for a in arr:
        if a[0] > a[-1]:
            return -1
        elif a[0] < a[-1]:
            return 1


def mergeArrays(arr):

    if find_order(arr) == 1:
        rel = lte_rel
    else:
        rel = gt_rel

    # create Node array
    A = []
    for i, a in enumerate(arr):
        A.append([Node(i, j, x) for j, x in enumerate(a)])

    out = []
    heap = [x[0] for x in A]    # get the first set of data from each list
    build_heap(heap, rel)
    while len(heap) >= 1:
        # print(",".join([str(x.val) for x in heap]))
        m = remove_min(heap)
        out.append(m.val)
        if m.index + 1 > len(A[m.key]) - 1:  # no more items to insert
            heap[0], heap[-1] = heap[-1], heap[0]
            heap = heap[0:-1]
            heapify(heap, 0, rel)
        else:
            insert_root(heap, A[m.key][m.index + 1], rel)

    return out


arr = [[1, 3, 5, 7],
       [2, 4, 6, 8],
       [0, 9, 10, 11]]
res = mergeArrays(arr)

print(res)
