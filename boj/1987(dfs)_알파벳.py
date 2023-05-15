import sys

def bfs(x, y):
    global result
    q = set()
    q.add((x, y, board[x][y]))

    while q:
        xx, yy, history = q.pop()
        result = max(result, len(history))

        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            else:
                if board[nx][ny] not in history:
                    q.add((nx, ny, history + board[nx][ny]))


if __name__ == "__main__":
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    board = []
    result = 1

    R, C = map(int, sys.stdin.readline().split())
    for _ in range(R):
        board.append(list(sys.stdin.readline().rstrip()))

    bfs(0, 0)
    print(result)
