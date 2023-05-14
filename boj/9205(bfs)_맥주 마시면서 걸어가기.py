import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    location = []
    for i in range(n+2):
        location.append(list(map(int, sys.stdin.readline().split())))

    start = location[0]
    end = location[-1]
    store = [location[1]]
    finish = True

    # 편의점 위치 담기 및 정렬
    for j in range(2, len(location) - 1):
        if abs(location[j][0] + location[j][1]) > abs(store[-1][0] + store[-1][1]):
            store.append(location[j])
        else:
            tmp = store.pop()
            store.append(location[j])
            store.append(tmp)

    # 도착 위치가 20병 안에 가면
    if (abs(start[0] - end[0]) + abs(end[1] - end[1])) // 50 <= 20:
        print("happy")
    else:
        check = True
        for j in store:
            if (abs(start[0] - end[0]) + abs(start[1] - end[1])) // 50 <= 20:
                break
            # 제일 가까운 편의점이 20병 안에 못가면
            if (abs(start[0] - j[0]) + abs(start[1] - j[1])) // 50 > 20:
                check = False
                break
            else:
                start = [j[0], j[1]]

        if check:
            print("happy")
        else:
            print("sad")

