import sys
from collections import deque

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    board = [list(map(int, str(sys.stdin.readline().strip()))) for _ in range(n)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    q = deque()
    q.append((0, 0, 1))
    
    while q:
        y, x, count = q.popleft()

        if y == n -1 and x == m - 1:
            print(count)
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if board[ny][nx] == 1:
                board[ny][nx] = 0
                q.append((ny, nx, count + 1))
