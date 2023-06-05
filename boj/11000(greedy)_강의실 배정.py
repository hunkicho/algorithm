import sys

if __name__ == "__main__":
    lec = []
    n = int(sys.stdin.readline())
    start = []
    end = []
    cnt = 0
    for _ in range(n):
        #lec.append(tuple(map(int, sys.stdin.readline().split())))
        s, e = map(int, sys.stdin.readline().split())
        if s not in end:
            cnt += 1
        end.append(e)

    print(cnt)
