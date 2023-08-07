def solution(s, n):
    answer = ''
    
    str_to_list = list(s)
    for i in str_to_list:
        if i == ' ':
            answer += ' '
        else:
            corr = ord('A') if i.isupper() else ord('a')
            answer += chr((ord(i) - corr + n) % 26 + corr)
    
    return answer

print(solution("AB",1))