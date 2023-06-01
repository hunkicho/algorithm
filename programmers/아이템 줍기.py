def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    map = [[0] * 10 for _ in range(10)]
    cnt = 1


    for rec in rectangle:
        x1 = rec[0]
        y1 = 9-rec[1]
        x2 = rec[2]
        y2 = 9-rec[3]

        for i in range(x1, x2+1): #가로 선 긋기
            map[y1][i] = 1
            map[y2][i] = 1
        print(y2,y1)
        for j in range(y2, y1+1): # 세로 선 긋기
            if map[j][x1] == 1:
                for t in range(x1-1,-1,-1):
                    if map[j][t] == 1:
                        for k in range(x1+1, x2):
                            map[j][k] = 0
                        break
            map[j][x1] = 1

            if map[j][x2] == 1:
                for b in range(x2+1,10):
                    if map[j][b]:
                        for n in range(x2+1, x1,-1):
                            map[j][n] = 0
            map[j][x2] = 1
        for q in map:
            print(q)
        print("0000000000000000000000000000000000000000000000000000000000000")
        cnt += 1

    return answer

solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]],1,3,7,8)