# https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    length = len(genres)
    dic = dict()
    dic2 = dict()
    gen = []
    
            
    
    for i in range(length):
        if dic.get(genres[i]):
            dic2[genres[i]] += plays[i]
            dic[genres[i]].append([i, plays[i]])
        else:
            dic2[genres[i]] = plays[i]
            dic[genres[i]] = [[i, plays[i]]]
                                                  
    hap = sorted(dic2.items(), key = lambda x: x[1], reverse=True)
    for j in hap:
        gen.append(j[0])
    
    for k in gen:
        get_data = sorted(dic[k], key = lambda x: (-x[1],x[0]))
        for y in range(len(get_data)):
            answer.append(get_data[y][0])
            if y == 1:
                break
                                       
    return answer