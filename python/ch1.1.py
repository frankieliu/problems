# remove dupplicate characters in string
def hasDuplicate(str):
    a = [False] * 256;
    for i in range(0,len(str)):
        loc = ord(str[i])-ord('a')
        if a[loc]:
            return True
        else:
            a[loc] = True

    return False

print(hasDuplicate('helo'))
print(hasDuplicate('hello'))
