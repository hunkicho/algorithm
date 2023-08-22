# 내가 푼거(stack 이용)
def solution(progresses, speeds):
    answer = []
    stack = []
    
    length = len(progresses)
    check = 0
    
    for i in range(length):
        percent = 100 - progresses[i]
        speed = speeds[i]
        remain = percent // speed if percent % speed == 0 else percent // speed + 1
        
        if stack:
            if remain <= check:
                stack.append(remain)
            else:
                answer.append(len(stack))
                stack = [remain]
                check = remain
        else:
            stack.append(remain)
            check = remain
            
    
    if len(stack) > 0:
        answer.append(len(stack))
    
    return answer

# 책에서 푼 내용(queue 이용)
def solution(progresses, speeds):
    answer = []    

    while progresses:        
        for i in range(len(progresses)):
            progresses[i] += speeds[i]            

        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1

        if cnt > 0: answer.append(cnt)
            
    return answer

print(solution([93, 30, 55], [1, 30, 5]))


