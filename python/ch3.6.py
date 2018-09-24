import random

a = []
[a.append(random.randint(1,10)) for i in range(0,10)]
a = [5,4,3,2,1]
print(a)

b = []
while a:
    topa = a.pop()
    if not b:
        b.append(topa)
    else:
        topb = b.pop()
        if topb >= topa:
            b.append(topb)
            b.append(topa)
        else:
            a.append(topb)
            while b:
                topb = b.pop()
                if topb < topa:
                    a.append(topb)
                else:
                    exit
            b.append(topa)

print(b)
