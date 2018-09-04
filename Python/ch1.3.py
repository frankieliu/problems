def removeDuplicates(s):
    track = [False] * 256;
    new = ''
    for i in range(0, len(s)):
        loc = ord(s[i])-ord('a')
        if track[loc] == False:
            print("Adding {}".format(s[i]))
            new += s[i]
            track[loc] = True
    return new

print(removeDuplicates('abcd'))
print(removeDuplicates('aaaa'))
print(removeDuplicates(''))
print(removeDuplicates('abbbccccdddeee'))
print(removeDuplicates('abbbccccbbbeee'))
