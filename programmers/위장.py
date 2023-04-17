# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 0
    hash_table = {}
    case = 1
    
    for i in clothes:
        if hash_table.get(i[1]):
            hash_table[i[1]] +=1
        else:
            hash_table[i[1]] = 1
    
            
    for v in hash_table.values():
        case = case + (case * v)
        
    answer = case - 1
    
    return answer