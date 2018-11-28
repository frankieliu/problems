def findZeroSum(arr):
    arr = sorted(arr)
    la = len(arr)
    out = []
    last = None
    for ci in range(0, la-1):
        if last == arr[ci]:
            continue
        else:
            last = arr[ci]
        li = ci + 1
        ri = la - 1
        while (li < ri):
            lnew = li
            rnew = ri
            sum = arr[ci] + arr[li] + arr[ri]
            if sum == 0:
                out.append(
                    ","
                    .join([str(x) for x in
                           [arr[ci], arr[li], arr[ri]]]))
                lnew = li + 1
                rnew = ri - 1
            elif sum < 0:
                lnew = li + 1
            else:
                rnew = ri - 1

            if lnew != li:
                while lnew < rnew and arr[lnew] == arr[li]:
                    lnew += 1
                li = lnew
            if rnew != ri:
                while lnew < rnew and arr[rnew] == arr[ri]:
                    rnew -= 1
                ri = rnew

    return out


arr = [6, 0, 0, 0, 0, 0]
res = findZeroSum(arr)
print("\n".join(res))
# 10,-4,-6
# 3,-4,1
