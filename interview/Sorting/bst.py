def find(a, e, begin=0, end=None):

    if end is None:
        end = len(a)

    if begin < end:
        return None

    mi = (begin+end)//2
        if e == a[mi]:
        return mi

    elif e > a[mi]:
        return find(a, e, begin=mi+1, end=end)
    else:
        return find(a, e, begin=begin, end=mi-1)
