import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    point = []
    result = 0
    
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        point.append((x, y))
    point.sort()
    
    start = point[0][0]
    end = point[0][1]
    
    for i in range(1, len(point)):
        if point[i][0] > start and point[i][0] > end:
            result += end - start
            start = point[i][0]
            
        if point[i][1] > end:
            end = point[i][1]
    result += end - start
    print(result)