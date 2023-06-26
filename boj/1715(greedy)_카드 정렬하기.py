import sys
from heapq import heappush, heappop

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    card = []
    result = 0
    for _ in range(n):
        card.append(int(sys.stdin.readline()))
    card.sort()
    start = card[0]
    print(card)
    for i in card[1:]:
        result += start + i
        start = result
        print(result)

    print(result)
