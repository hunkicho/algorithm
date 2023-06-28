import sys

if __name__ == "__main__":
    while True:
        n = int(sys.stdin.readline())
        # 미로의 방 수가 0일 경우 입력 종료
        if n == 0:
            break

        for _ in range(n):
            variable = list(map(int, sys.stdin.readline().split()))
            base = len(variable) - 1
            alpha = variable[0]
            price = variable[1]
            room = variable[2:base]

