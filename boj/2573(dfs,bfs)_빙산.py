# https://www.acmicpc.net/problem/2573

# import sys
# sys.setrecursionlimit(10**9)
#
# def year(x_start,x_end,y_start,y_end):
#     """
#     매년 빙하 높이 줄어들기
#     - 빙하가 동시에 녹아야 하기 때문에 리스트에 좌표와 줄어드는 높이를 저장한 후
#       반복문에서 차례대로 높이 조절
#     """
#     values = []
#     for i in range(x_start,x_end):
#         for j in range(m):
#             if ice[i][j] > 0:
#                 cut = 0
#                 for k in range(4):
#                     qx = i + dx[k]
#                     qy = j + dy[k]
#
#                     if qx < 0 or qx >= n or qy < 0 or qy >= m:
#                         continue
#                     else:
#                         if ice[qx][qy] == 0:
#                             cut += 1
#                 values.append([i,j,cut])
#
#     for o in values:
#         if ice[o[0]][o[1]] - o[2] > 0:
#             ice[o[0]][o[1]] -= o[2]
#         else:
#             ice[o[0]][o[1]] = 0
#
# def dfs(x,y):
#     visit[x][y] = 1
#
#     for k in range(4):
#         qx = x + dx[k]
#         qy = y + dy[k]
#
#         if qx < 0 or qx >= n or qy < 0 or qy >= m:
#             continue
#         else:
#             if ice[qx][qy] > 0 and visit[qx][qy] == 0:
#                 dfs(qx,qy)
#
# n, m = map(int, sys.stdin.readline().split())
# ice = []
#
# dx = [0,0,-1,1]
# dy = [1,-1,0,0]
#
# count = 0
# x_start = 0
# x_end = n
# y_start = 0
# y_end = m
#
# for _ in range(n):
#     ice.append(list(map(int, sys.stdin.readline().split())))
#
# while True:
#     visit =  [[0 for _ in range(m)] for _ in range(n)]
#     check = 0
#     check2 = 0
#
#     temp_x_start = n
#     temp_x_end = 0
#     temp_y_start = m
#     temp_y_end = 0
#
#     for x in range(x_start,x_end):
#         for c in range(y_start,y_end):
#             if ice[x][c] > 0:
#                 check = 1
#                 # 매번 처음부터 탐색을 할 수 없기 때문에 탐색 시작과 끝점을 설정
#                 # 좌표마다 비교하며 저장한다.
#                 temp_x_start = x if temp_x_start > x else temp_x_start
#                 temp_x_end = x if temp_x_end < x else temp_x_end
#                 temp_y_start = c if temp_y_start > c else temp_y_start
#                 temp_y_end = c if temp_y_end < c else temp_y_end
#
#                 if visit[x][c] == 0:
#                         dfs(x,c)
#                         check2 += 1
#
#     if check == 0:
#         print(0)
#         break
#     elif check2 > 1:
#         print(count)
#         break
#
#     x_start = temp_x_start
#     x_end = temp_x_end + 1
#     y_start = temp_y_start
#     y_end = temp_y_end + 1
#
#     year(x_start,x_end,y_start,y_end)
#     count += 1


import sys
from collections import deque


def year(x_start, x_end):
    """
    매년 빙하 높이 줄어들기
    - 빙하가 동시에 녹아야 하기 때문에 리스트에 좌표와 줄어드는 높이를 저장한 후
      반복문에서 차례대로 높이 조절
    """
    values = []
    check = False
    for i in range(x_start, x_end):
        for j in range(m):
            if ice[i][j] > 0:
                cut = 0
                for k in range(4):
                    qx = i + dx[k]
                    qy = j + dy[k]

                    if qx < 0 or qx >= n or qy < 0 or qy >= m:
                        continue
                    else:
                        if ice[qx][qy] == 0:
                            cut += 1
                values.append([i, j, cut])

    for o in values:
        if ice[o[0]][o[1]] - o[2] > 0:
            ice[o[0]][o[1]] -= o[2]
        else:
            ice[o[0]][o[1]] = 0
    if len(values) > 0:
        check = True

    return check


def find_point():
    count = 0
    for i in range(n):
        for j in range(m):
            if ice[i][j] > 0 and visit[i][j] == 0:
                q.append((i, j))
                visit[x][y] = 1
                BFS()
                count += 1
    return count


def BFS():
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            else:
                if visit[nx][ny] == 0 and ice[nx][ny] > 0:
                    visit[nx][ny] = 1
                    q.append((nx, ny))


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    ice = []
    for _ in range(n):
        ice.append(list(map(int, sys.stdin.readline().split())))


    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    x = 0
    y = 0
    cnt = 0

    q = deque()

    while True:
        #for u in ice:
            #print(u)
        visit = [[0 for _ in range(m)] for _ in range(n)]
        point = find_point()
        #print("point = ", point)
        #print("==================")

        if point >= 2:
            print(cnt)
            break

        is_finish = year(0, n)
        if not is_finish:
            print(0)
            break
        cnt += 1
