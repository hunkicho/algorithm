# https://www.acmicpc.net/problem/1260

import sys
from collections import deque

def dfs(node):
    print(node, end=' ')
    visit[node] = 1

    for i in board[node]:
        if visit[i] == 0:
            dfs(i)

def bfs(start):
    visit[start] = 1
    
    while q:
        next = q.popleft()
        print(next, end=' ')
        
        for i in board[next]:
            if visit[i] == 0:
                visit[i] = 1
                q.append(i)

n, m ,v = map(int, sys.stdin.readline().split())
board = [[] for _ in range(n+1)]
visit = [0] * (n + 1)

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    board[start].append(end)
    board[end].append(start)

for j in board:
    j.sort()

dfs(v)
print()

visit = [0] * (n+1)
q = deque()
q.append(v)

bfs(v)
print()
