# https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 0
    routes.sort(key = lambda x : (x[0], x[1]))
    start = -30001
    end = routes[0][1]
    
    for s, e in routes:
        if start <= s <= end:
            start = s
            if e < end:
                end = e
        else:
            start = s
            end = e
            answer += 1
    
    return answer + 1