import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    dy = [0] * (n+3)
    dy[1] = 1
    dy[2] = 2
    dy[3] = 4
    
    for i in range(4, n+1):
        dy[i] = dy[i-1] + dy[i-2] + dy[i-3]
    print(dy[n])
    