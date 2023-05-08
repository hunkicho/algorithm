import sys

def dfs(x,y,hap):
    graph[x][y] = 2
    

    for k in range(4):
        gx = x + dx[k]
        gy = y + dy[k]

        if gx < 0 or gx >= n or gy < 0 or gy >= n:
            continue
        else:
            if graph[gx][gy] == 1:
                check = dfs(gx,gy,hap+1)
                hap = check if check > hap else 0
    return hap


n = int(sys.stdin.readline())
graph = []
cnt = 0

dx = [0,0,-1,1]
dy = [1,-1,0,0]

result = []

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(dfs(i,j,1))
            cnt += 1

print(cnt)
result.sort()
for num in result:
    print(num)