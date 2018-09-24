def space(s):
    count = 0
    origLen = len(s)
    for i in range(0, origLen):
        if s[i] == ord(' '):
            count += 1

    # Add to the length
    s += bytearray([0] * (2 * count));

    # pointer to end of loc
    loc = len(s) - 1
    for i in reversed(range(0, origLen)):
        if s[i] == ord(' '):
            # adding %20
            s[loc] = ord('0')
            loc -= 1
            s[loc] = ord('2')
            loc -= 1
            s[loc] = ord('%')
            loc -= 1
        else:
            # print(s[i])
            s[loc] = s[i]
            loc -= 1

    return s

print(''.join([chr(x) for x in space(bytearray('hello world  21'.encode()))]))
