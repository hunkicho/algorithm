import sys

n, m = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

result = (a+b)
result.sort()
print(*result)


# 투포인터
import sys

n, m = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

ap, bp = 0, 0
result = []
while ap != n or bp != m:
    if ap == n:
        result.append(b[bp])
        bp += 1
    elif bp == m:
        result.append(a[ap])
        ap += 1
    else:
        if a[ap] < b[bp]:
            result.append(a[ap])
            ap += 1
        elif b[bp] < a[ap]:
            result.append(b[bp])
            bp += 1

print(*result)