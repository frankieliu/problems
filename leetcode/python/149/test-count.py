from collections import Counter

L = [1,2,45,55,5,4,4,4,4,4,4,5456,56,6,7,67]
L = {1:2,
     2:3,
     3:4}
print(L.values())
print(Counter(L).most_common(1))
