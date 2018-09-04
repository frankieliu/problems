# check if two strings are anagrams
def checkAna(s1, s2):
    wc1 = [0] * 256
    wc2 = [0] * 256
    for i in range(0, len(s1)):
        loc = ord(s1[i]) - ord('a')
        wc1[loc] += 1
    for i in range(0, len(s2)):
        loc = ord(s2[i]) - ord('a')
        wc2[loc] += 1
    for i in range(0,256):
        if wc1[i] != wc2[i]:
            return False
    return True

print(checkAna('back', 'akcb'))
print(checkAna('a', 'b'))
print(checkAna('a', ''))
print(checkAna('baba', 'aabb'))
