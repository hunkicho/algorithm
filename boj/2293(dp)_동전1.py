import sys

def dfs(hap):
    global cnt
    if hap > k:
        return
    if hap == k:
        cnt += 1
    else:
        for i in range(n):
            print(hap,"+",num[i])
            dfs(hap + num[i])

n, k = map(int, sys.stdin.readline().split())
dy = [0] * (k+1)
num = []
cnt = 0

for _ in range(n):
    num.append(int(sys.stdin.readline()))
for j in num:
    dfs(j)
    
print(cnt)