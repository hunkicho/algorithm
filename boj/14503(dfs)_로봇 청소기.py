import sys

# 0: 북
# 1: 동
# 2: 남
# 3: 서

# 0: 청소안함
# 1: 벽

def dfs(r, c, s):
    global cnt
    status = True

    if room[r][c] == 0:
        room[r][c] = 2
        cnt += 1

    for i in base[s]:
        rn = r + rd[i]
        cn = c + cd[i]

        if 0 <= rn <= n - 1 and 0 <= cn <= m - 1 and room[rn][cn] == 0:
            dfs(rn, cn, i)
            status = False

    if status:
        rn = r - rd[s]
        cn = c - cd[s]

        if 0 <= rn <= n - 1 and 0 <= cn <= m - 1 and room[rn][cn] == 2:
            dfs(rn, cn, s)
        else:
            print(rn, cn)
            print(cnt)



if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    r, c, d = map(int, sys.stdin.readline().split())
    room = []
    cnt = 0
    base = [[3,2,1,0], [0,3,2,1], [1,0,3,2], [2,1,0,3]]
    rd = [1, 0, -1, 0]
    cd = [0, 1, 0, -1]

    for _ in range(n):
        room.append(list(map(int, sys.stdin.readline().split())))
    dfs(r-1, c-1, d)