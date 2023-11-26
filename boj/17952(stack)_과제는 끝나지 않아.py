# stack

import sys

n = int(sys.stdin.readline())
stack = []
score = 0

for _ in range(n):
    info = list(map(int, sys.stdin.readline().split()))

    if info[0] > 0:
        if info[2] == 1:
            score += info[1]
        else:
            stack.append([info[1], info[2]-1])
    elif stack:
            stack[-1][1] = stack[-1][1] - 1
            if stack[-1][1] == 0:
                work = stack.pop()
                score += work[0]
print(score)