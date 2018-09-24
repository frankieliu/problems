# Towers of Hanoi
# in stack 1: 5 4 3 2 1 -> move to stack 3

def move(n, fr, to, stacks):
    if to == 0:
        if fr == 1:
            mid = 2
        else:
            mid = 1
    elif to == 1:
        if fr == 0:
            mid = 2
        else:
            mid = 0
    elif to == 2:
        if fr == 1:
            mid = 0
        else:
            mid = 1
    # print(fr, to, mid)
    if n == 1:
        a = stacks[fr].pop()
        stacks[to].append(a)
        stacksPrint(stacks)
    else:
        move(n-1, fr, mid, stacks)
        move(1, fr, to, stacks)
        move(n-1, mid, to, stacks)

def stacksPrint(stacks):
        print(''.join(str(stacks[0])),
              ''.join(str(stacks[1])),
              ''.join(str(stacks[2])))

s1 = []
s2 = []
s3 = []
[s1.append(i) for i in range(5,0,-1)]
move(5, 0, 2, [s1, s2, s3])
# stacksPrint([s1, s2, s3])
