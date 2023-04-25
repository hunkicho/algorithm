#https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    lost_copy = lost.copy()
    reserve_copy = reserve.copy()
    check = []
    away = []
    
    for w in lost:
        if w in reserve:
            lost_copy.remove(w)
            reserve_copy.remove(w)
            
    answer = n - len(lost_copy)
            
    lost_copy.sort()
    reserve_copy.sort()
    
    
    for i in reserve_copy:
        for j in lost_copy:
            if (i - 1 == j or i + 1 == j) and j not in check and i not in away:
                answer += 1
                check.append(j)
                away.append(i)
                break
    return answer