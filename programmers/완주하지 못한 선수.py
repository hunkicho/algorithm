# https://school.programmers.co.kr/learn/courses/30/lessons/42576?language=python3

# 다른 사람이 입력한 답 봄

def solution(participant, completion):
    dic = {}
    
    for i in participant:
        if dic.get(i):
            dic[i] += 1
        else:
            dic[i] = 1
    
        
    for i in completion:
        if dic.get(i):
            dic[i] -= 1
            if dic[i] == 0:
                del dic[i]
        
    return list(dic)[0]