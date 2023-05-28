import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    point = []
    result = 0
    
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        point.append((x, y))
    point.sort(key = lambda t: t[0])
    
    start = point[0][0]
    end = point[0][1]
    
    for s, e in point:
        if s > end:
            result += end - start
            start = s
            end = e
            
        elif e > end:
            end = e
    result += end - start
    print(result)