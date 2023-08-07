def solution(s):
    answer = ''
    
    str_list = s.split(' ')
    
    for i in str_list:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '   
    
    return answer[:-1]