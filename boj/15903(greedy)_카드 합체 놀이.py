import sys
from heapq import heappush, heappop, heapify

if __name__ == "__main__":
    n, c = map(int, sys.stdin.readline().split())
    card = list(map(int, sys.stdin.readline().split()))
    heapify(card)

    result = 0

    for _ in range(c):
        check = 0
        for _ in range(2):
            check += heappop(card)
        for _ in range(2):
            heappush(card, check)

    print(sum(card))
