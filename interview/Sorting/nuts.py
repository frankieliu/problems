#!/usr/bin/env python

import sys


def solve_brute_force(A, B):
    c = []
    for a in A:
        for b in B:
            if a == b:
                c.append("{} {}".format(a, a))
    return c


def pivot(A, begin, end):
    return (begin + end) // 2


def partition(B, A, ai, begin, end):
    ''' given an index ai
    use A[ai] to partition B from begin to end
    '''
    elem = A[ai]
    # print("Partition {}".format(elem))
    i = begin     # next available position to exchange

    # in this case it is important to swap the "equivalent"
    # pivot element to the last element of the "left" list
    # since we want to eliminate it after the partition

    m = -1        # matching element
    for j in range(begin, end + 1):
        if B[j] <= elem:    # swap
            B[j], B[i] = B[i], B[j]
            if B[i] == elem:
                # print("Match at {}".format(i))
                m = i
            i += 1
    B[m], B[i - 1] = B[i - 1], B[m]
    # print("Exchanging {} for {}".format(m, i - 1))
    return i - 1


def sortAB(A, B, begin, end):
    if end <= begin:
        return

    ai = pivot(A, begin, end)
    # print('-' * 70)
    # print(A, B, begin, end)
    bi = partition(B, A, ai, begin, end)    # break B and return bi
    ai = partition(A, B, bi, begin, end)    # break A and return ai == bi!
    # print(A, B, bi, ai)
    sortAB(A, B, begin, ai - 1)
    sortAB(A, B, ai + 1, end)


def solve(A, B):
    sortAB(A, B, 0, len(A) - 1)
    C = zip(A, B)
    return ["{} {}".format(x[0], x[1]) for x in C]


if __name__ == "__main__":
    f = sys.stdout

    if False:
        nuts_count = int(input())

        nuts = []

        for _ in range(nuts_count):
            nuts_item = int(input())
            nuts.append(nuts_item)

        bolts_count = int(input())

        bolts = []

        for _ in range(bolts_count):
            bolts_item = int(input())
            bolts.append(bolts_item)

    nuts = [4, 32, 5, 7]
    bolts = [32, 7, 5, 4]
    res = solve(nuts, bolts)


f.write('\n'.join(res))
f.write('\n')

f.close()
