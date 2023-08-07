def solution(s):
    answer = []
    
    step1 = s[2:-2].split("},{")
    step2 = []
    
    
    for i in step1:
        tmp = i.split(',')
        step2.append(tmp)

    step2.sort(key=len)
    
    
    for j in step2:
        for k in range(0,len(j)):
            if int(j[k]) not in answer:
                answer.append(int(j[k]))
        
    
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))