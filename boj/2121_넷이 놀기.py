import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    A, B = map(int, sys.stdin.readline().split())
    location = dict()

    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        location[(x, y)] = True
    
    count = 0

    for (x, y) in location.keys():
        if location.get((x+A, y),False) and location.get((x, y+B),False) and location.get((x+A, y+B),False):
            count += 1

    print(count)
