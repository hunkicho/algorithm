import sys
from collections import deque

n = int(sys.stdin.readline())
dx = [-2, - 1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(n):
    line = int(sys.stdin.readline())
    graph = [[0 for _ in range(line)] for _ in range(line)]
    sx, sy = map(int, sys.stdin.readline().split())
    ex, ey = map(int, sys.stdin.readline().split())
    q = deque()
    q.append((sx, sy))
    graph[sx][sy] = 1

    while q:
        tmp = q.popleft()
        if tmp[0] == ex and tmp[1] == ey:
            break
        for i in range(8):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]

            if 0 <= nx < line and 0 <= ny < line and graph[nx][ny] == 0:
                graph[nx][ny] = graph[tmp[0]][tmp[1]] + 1
                q.append((nx, ny))
    print(graph[ex][ey] - 1)
