import sys
from collections import deque
# 총 F층
# 목적지 G
# 현위치 S
# U 위로 u
# D 아래로 d

def bfs():
    while q:
        p, cnt = q.popleft()

        if p == G:
            return cnt

        for i in (U, D):
            np = p + i
            if 0 < np <= F and visit[np] == 0:
                q.append((np, cnt + 1))
                visit[np] = 1
    return -1


if __name__ == "__main__":
    F, S, G, U, D = map(int, sys.stdin.readline().split())
    visit = [0 for _ in range(F+1)]
    q = deque()
    q.append((S, 0))
    visit[S] = 1
    check = bfs()
    if check == -1:
        print("use the stairs")
    else:
        print(check)
