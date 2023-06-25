import sys
from heapq import heappush, heappop

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lec = []
    count = 1
    end = []
    for _ in range(n):
        s, e = map(int, sys.stdin.readline().split())
        lec.append((s, e))

    lec.sort()
    end.append(lec[0][1])
    lec_fix = lec[1:]

    for i in lec_fix:
        if i[0] < end[0]:
            heappush(end, i[1])
            count += 1
        else:
            heappop(end)
            heappush(end, i[1])
    print(count)

