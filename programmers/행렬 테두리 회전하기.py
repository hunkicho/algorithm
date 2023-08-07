def solution(rows, columns, queries):
    answer = []
    
    board = [[0]*columns for _ in range(rows)]
    
    num = 1
    for i in range(rows):
        for j in range(columns):
            board[i][j] = num
            num += 1
    
    
    for k in queries:
        fx = k[0] - 1
        fy = k[1] - 1
        lx = k[2] - 1
        ly = k[3] - 1

        print(fx, fy, lx, ly)
        
        first = board[fx][fy]
        min_value = first

        for q in range(fx, lx):
            board[q][fy] = board[q+1][fy]
            min_value = min(min_value, board[q+1][fy])
        
        for q in range(fy, ly):
            board[lx][q] = board[lx][q+1]
            min_value = min(min_value, board[lx][q+1])
        
        for q in range(lx, fx, -1):
            board[q][ly] = board[q-1][ly]
            min_value = min(min_value, board[q-1][ly])

        for q in range(ly, fy + 1, -1):
            board[fx][q] = board[fx][q-1]
            min_value = min(min_value, board[fx][q-1])

        board[fx][fy+1] = first

        answer.append(min_value)
    
    print(board)
    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))