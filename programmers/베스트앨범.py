# https://school.programmers.co.kr/learn/courses/30/lessons/42579

# def solution(genres, plays):
#     answer = []
#     length = len(genres)
#     dic = dict()
#     dic2 = dict()
#     gen = []
    
            
    
#     for i in range(length):
#         if dic.get(genres[i]):
#             dic2[genres[i]] += plays[i]
#             dic[genres[i]].append([i, plays[i]])
#         else:
#             dic2[genres[i]] = plays[i]
#             dic[genres[i]] = [[i, plays[i]]]
                                                  
#     hap = sorted(dic2.items(), key = lambda x: x[1], reverse=True)
#     for j in hap:
#         gen.append(j[0])
    
#     for k in gen:
#         get_data = sorted(dic[k], key = lambda x: (-x[1],x[0]))
#         for y in range(len(get_data)):
#             answer.append(get_data[y][0])
#             if y == 1:
#                 break
                                       
#     return answer




from collections import defaultdict

def solution(genres, plays):
    answer = []
    total_play = defaultdict(int)
    play_times = defaultdict(list)
    
    # 딕셔너리에 장르별로 재생횟수들을 순서와 함께 저장
    # 총 횟수 제일 많은거 2개 뽑기
    # 재생횟수 리스트 람다로 정렬
    
    length = len(genres)
    
    for i in range(length):
        total_play[genres[i]] += plays[i]
        play_times[genres[i]].append([plays[i], i])
        
    total_play = sorted(total_play.items(), key=lambda x: x[1], reverse=True)
    print(total_play)
    
    for j in range(len(total_play)):
        genre = total_play[j][0]
        play_times[genre].sort(key=lambda x: (-x[0], x[1]))

        for k in range(len(play_times[genre])):
            if k > 1:
                break
            answer.append(play_times[genre][k][1])

            
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]	))