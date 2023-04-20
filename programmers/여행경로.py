# from collections import deque

# def solution(tickets):
#     answer = []
#     graph = {}
#     visit = len(tickets)
    
#     for i in tickets:
#         if graph.get(i[0]):
#             graph[i[0]].append(i[1])
#         else:
#             graph[i[0]] = [i[1]]
#     print(graph)
    
#     q = deque(["ICN"])

#     while q:
#         n = q.popleft()
#         answer.append(n)

#         if n in graph:
#             graph[n].sort()
#             if len(graph[n]) > 1:
#                 graph[n].sort
#                 for k in range(len(graph[n])):
#                     if graph[n][k] in graph:
#                         if len(graph[graph[n][k]]) > 1 or visit == 0:
#                             q.append(graph[n][k])
#                             graph[n].pop(k)
#                             visit -= 1
#                             break
#                         elif len(graph[graph[n][k]]) > 0 :
#                             if graph[graph[n][k]][0] in graph:
#                                 q.append(graph[n][k])
#                                 graph[n].pop(k)
#                                 visit -= 1
#                                 break
#             elif len(graph[n]) == 1:
#                 if len(graph[n][0]) > 0 or visit == 0:
#                     q.append(graph[n][0])
#                     graph[n].pop(0)
#                     visit -= 1
#             print(graph)
    
#     return answer

# 다른사람거 봄

from collections import defaultdict
def solution(tickets):
    r = defaultdict(list)
    for i,j in tickets:
        r[i].append(j)
    for i in r.keys():
        r[i].sort()

    s = ["ICN"]
    p = []
    while s:
        q = s[-1]
        if r[q] != []:
            s.append(r[q].pop(0))
        else:
            p.append(s.pop())
    return p[::-1]
