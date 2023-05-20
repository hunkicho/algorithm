import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.insert(0, 0)
dl = [0] * (n+1)
dl[1] = 1
res = 1

for i in range(2, n+1):
    tmp = 0
    for j in range(i-1, 0, -1):
        if a[j] < a[i] and dl[j] > tmp:
            tmp = dl[j]
    dl[i] = tmp + 1
    if dl[i] > res:
        res = dl[i]
print(res)
