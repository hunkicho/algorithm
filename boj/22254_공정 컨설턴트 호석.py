import sys, heapq

def check() -> bool:
    for gift in gifts:
        line = heapq.heappop(hp)
        if line + gift > X:
            return False
        heapq.heappush(hp, line + gift)
    return True

if __name__ == "__main__":
    N, X = map(int, sys.stdin.readline().split())
    gifts = list(map(int, sys.stdin.readline().split()))
    
    start = 1
    end = N
    result = 0

    while start <= end:
        mid = (start + end) // 2

        hp = []
        for _ in range(mid):
            heapq.heappush(hp, 0)
        
        if not check():
            start = mid +1
        else:
            end = mid - 1
            result = mid
            
    print(result)
            