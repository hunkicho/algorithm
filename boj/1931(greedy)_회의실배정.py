import sys

if __name__ == "__main__":
    meet = []
    n = int(sys.stdin.readline())
    for _ in range(n):
        meet.append(tuple(map(int, sys.stdin.readline().split())))
    meet.sort(key = lambda x : (x[1],x[0]))

    end = meet[0][1]
    cnt = 1

    for i in range(1,n):
        if meet[i][0] >= end:
            end = meet[i][1]
            cnt += 1
    print(cnt)