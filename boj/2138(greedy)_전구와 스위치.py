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

    count = 0

    while True:
        check = -1
        for i in range(n):
            if first[i] != last[i] and check != i:
                if 0 < i < n - 1:
                    first[i - 1] = change(first[i - 1])
                    first[i] = change(first[i])
                    first[i + 1] = change(first[i + 1])
                elif i == 0:
                    first[i] = change(first[i])
                    first[i + 1] = change(first[i + 1])
                elif i == n - 1:
                    first[i - 1] = change(first[i - 1])
                    first[i] = change(first[i])

                check = i
                # print("after = ", first)
                count += 1
        if first == last:
            break

    print(count)
