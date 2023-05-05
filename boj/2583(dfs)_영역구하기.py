# https://www.acmicpc.net/problem/2583

import sys
sys.setrecursionlimit(10**9)

def dfs(x,y,hap):
    graph[x][y] = 1
    
    for q in range(4):
        gx = x + dx[q]
        gy = y + dy[q]

        if gx < 0 or gx >= m or gy < 0 or gy >= n:
            continue
        else:
            if graph[gx][gy] == 0:
                check = dfs(gx, gy, hap + 1)
                hap = check if check > hap else 0
    return hap
    

m, n, k = map(int, sys.stdin.readline().split())
graph = [[0 for col in range(n)] for row in range(m) ]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

cnt = 0
result = []

for _ in range(k):
    rect = list(map(int, sys.stdin.readline().split()))
    for i in range(m-rect[3], m-rect[1]):
        for j in range(rect[0], rect[2]):
            graph[i][j] = 1

for v in range(0, m):
    for b in range(0,n):
        if graph[v][b] == 0:
            result.append(dfs(v,b,1))
            cnt += 1
print(cnt)

result.sort()
for p in result:
    print(p, end=" ")