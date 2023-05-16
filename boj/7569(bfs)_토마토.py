import sys
from collections import deque


def bfs():
    global day
    while q:
        tmp = q.popleft()

        day = max(day, tmp[3])

        for p in range(6):
            nz = tmp[0] + dz[p]
            nx = tmp[1] + dx[p]
            ny = tmp[2] + dy[p]

            if 0<=nz<z and 0<=nx<x and 0<=ny<y and contain[nz][nx][ny] == 0:
                contain[nz][nx][ny] = 1
                q.append((nz, nx, ny, tmp[3] + 1))


if __name__ == "__main__":
    y, x, z = map(int, sys.stdin.readline().split())

    dx = [0, 0, -1, 1, 0, 0]
    dy = [1, -1, 0, 0, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    q = deque()
    day = 0
    box = []
    contain = []
    for _ in range(z):
        for _ in range(x):
            box.append(list(map(int, sys.stdin.readline().split())))
        contain.append(box)
        box = []

    for i in range(z):
        for j in range(x):
            for k in range(y):
                if contain[i][j][k] == 1:
                    q.append((i, j, k, 0))

    if len(q) == z * x * y:
        print(0)
    else:
        bfs()
        for i in range(z):
            for j in range(x):
                for k in range(y):
                    if contain[i][j][k] == 0:
                        print(-1)
                        sys.exit(0)
        print(day)
