import sys
sys.setrecursionlimit(10**9)

def dfs(x,y,limit):
    visit[x][y] = 1
    
    for q in range(4):
        gx = x + dx[q]
        gy = y + dy[q]

        if gx < 0 or gx >= n or gy < 0 or gy >= n or area[gx][gy] <= limit:
            continue
        else:
            if visit[gx][gy] == 0:
                dfs(gx,gy,limit)

n = int(sys.stdin.readline())
area = []

dx = [0,0,-1,1]
dy = [1,-1,0,0]

visit = [[0 for _ in range(n)] for _ in range(n) ]

result = 0
check = 0

for _ in range(n):
    input = list(map(int, sys.stdin.readline().split()))
    area.append(input)
    check = max(max(input), check)

            
for i in range(check):
    cnt = 0
    visit = [[0 for _ in range(n)] for _ in range(n) ]
    for j in range(n):
        for k in range(n):
            if area[j][k] > i and visit[j][k] == 0:
                dfs(j,k,i)
                cnt += 1
    if cnt > result:
        result = cnt

print(result)