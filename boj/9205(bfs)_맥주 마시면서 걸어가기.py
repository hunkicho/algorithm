import sys
from collections import deque

# 출발지에서 도착지 까지 20병으로 갈 수 있으면 더 이상 판단 필요 없음
# 아니면 편의점 거쳐야 함
# 가장 가까운 편의점 부터 검사해야 하는데 제일 가까운 편의점 20병 안에 못가면 끝
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    location = []
    visit = []
    for i in range(n+2):
        point = list(map(int, sys.stdin.readline().split()))
        point.append(0)
        location.append(point)

    start = location[0]
    end = location[-1]
    store = []
    if len(location) > 2:
        for j in range(1, len(location) - 1):
            store.append(location[j])

    # 도착 위치가 20병 안에 가면
    if (abs(start[0] - end[0]) + abs(start[1] - end[1])) <= 50 * 20:
        print("happy")
    else:
        q = deque()
        q.append(start)
        start[2] = 1
        check = False

        while q:
            tmp = q.popleft()
            if tmp == end:
                check = True
                break
            tmp[2] = 1

            for p in location:
                if (abs(tmp[0] - p[0]) + abs(tmp[1] - p[1])) <= 50 * 20 and p[2] == 0:
                    q.append(p)

        if check:
            print("happy")
        else:
            print("sad")


