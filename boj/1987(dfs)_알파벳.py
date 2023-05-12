import sys


def dfs(x, y, cnt):
    global result

    if max(result) > cnt + (R * C - cnt):
        return

    result.add(cnt)

    for i in range(4):
        qx = x + dx[i]
        qy = y + dy[i]

        if qx < 0 or qx >= R or qy < 0 or qy >= C:
            continue
        else:
            if history[ord(board[qx][qy])] == 0:
                history[ord(board[qx][qy])] = 1
                dfs(qx, qy, cnt + 1)
                history[ord(board[qx][qy])] = 0


if __name__ == "__main__":
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    board = []
    history = [0 for _ in range(ord('Z') + 1)]
    result = set([1])

    R, C = map(int, sys.stdin.readline().split())
    for _ in range(R):
        board.append(list(sys.stdin.readline().rstrip()))

    history[ord(board[0][0])] = 1
    dfs(0, 0, 1)
    print(max(result))
