import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
dy = [0] * n
dy[0] = a[0]
res = a[0]

for i in range(1,n):
    check = 0
    for j in range(i-1,-1,-1):
        if a[j] < a[i] and dy[j] > check:
            check = dy[j]
    dy[i] = check + a[i]
    if dy[i] > res:
        res = dy[i]

print(res)