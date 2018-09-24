# str rotation

# assume you have isSubstring which checks if one word is a
# substring of another

# given two strings s1 and s2:
#  check if s2 is a rotation of s1 using one call to isSubstring

# abbba
# baaab  <- this is a rotation

def checkRotation(s1, s2):
    s = s1 + s1
    return s2 in s

print(checkRotation("hello", "elloh"))
