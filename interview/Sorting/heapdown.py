def heap_down(x, i):
    # check with children
    # find the smaller one
    # if you are greater than the smaller one
    # swap with it
    lenx = len(x)
    left = 2*i + 1
    right = 2*i + 2
    if left < lenx and right < lenx:
        if x[left] < x[right]:
            xmin, xi = x[left], left
        else:
            xmin, xi = x[right], right
        if x[i] > xmin:
            x[i], x[xi] = x[xi], x[i]
            heap_down(x, xi)
        else:
            pass
    elif left < lenx:
        if x[i] > x[left]:
            x[i], x[left] = x[left], x[i]
            heap_down(x, left)
        else:
            pass
    else:
        pass


def print_heap(x, i=0, sp=0):
    left = 2*i + 1
    right = 2*i + 2
    lenx = len(x)
    print("{}{}".format(" "*sp, x[i]))
    if (sp < 3):
        if left < lenx:
            print_heap(x, i=left, sp=sp+1)
        if right < lenx:
            print_heap(x, i=right, sp=sp+1)


def heapify(x):
    h = len(x)//2
    for i in range(h, -1, -1):
        heap_down(x, i)


a = [10, 9, 8, 7, 6, 5, 4, 3, 1]
heapify(a)
print_heap(a)
