import sys
from collections import deque

if __name__ == "__main__":
    first, last = map(int, sys.stdin.readline().split())
    q = deque()
    q.append((first,0))
    line = [0] * 1000001
    line[first] == 1

    while q:
        tmp, time = q.popleft()

        if tmp == last:
            print(time)
            break

        for i in range(3):
            if i == 0:
                next = tmp - 1 if 0 <= tmp - 1 <= 100000 else -1
            elif i == 1:
                next = tmp + 1 if 0 <= tmp + 1 <= 100000 else -1 
            else:
                next = tmp * 2 if 0 <= tmp * 1 <= 100000 else -1  
            
            if next > 0 and line[next] == 0:
                line[next] = 1
                q.append((next, time + 1))
                