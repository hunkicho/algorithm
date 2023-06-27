import sys


def change(num):
    if num == 0:
        return 1
    else:
        return 0


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    first = list(map(int, str(sys.stdin.readline().rstrip())))
    last = list(map(int, str(sys.stdin.readline().rstrip())))

    board = {
        "111": [1, "none"],
        "110": [1, "left"],
        "100": [2, "right"],
        "101": [2, "both"],
        "001": [2, "left"],
        "011": [1, "right"],
        "010": [3, "both"],
        "000": [0, "none"]
    }

    count = 0
    start = 0

    while True:
        if start + 2 >= n:
            start -= (start + 2) - (n - 1)
        key = ""
        for i in range(start, start + 3):
            if first[i] != last[i]:
                key += str(1)
            else:
                key += str(0)
        check = board[key]
        count += check[0]
        if check[1] == "both":
            if i - 1 >= 0:
                first[i - 1] = change(first[i - 1])
            if i + 1 < n:
                first[i+1] = change(first[i + 1])
        elif check[1] == "left":
            if i - 1 >= 0:
                first[i - 1] = change(first[i - 1])
        elif check[1] == "right":
            if i + 1 < n:
                first[i+1] = change(first[i + 1])

        if start + 3 == n:
            # for i in range(start, start + 3):
            #     if first[i] != last[i]:
            #         key += str(last[i])
            #     else:
            #         key += str(first[i])
            # check = board[key]
            if check[1] == "left":
                print(-1)
                break
            else:
                print(count)
                break
        else:
            for i in range(start, start + 3):
                first[i] = last[i]
        print(first)
        start += 3

