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









from collections import defaultdict, deque




def solution(tickets):

    answer = ["ICN"]
    start = ""
    stack = deque()
    stack.append("ICN")
    check = 0


    dic_ticket = defaultdict(list)
    for way in tickets:

        if way[0] in dic_ticket:
            if dic_ticket[way[0]][-1][0] < way[1]:
                tmp = dic_ticket[way[0]].pop()
                dic_ticket[way[0]].append(way[1])
                dic_ticket[way[0]].append(tmp)
            else:
                dic_ticket[way[0]].append(way[1])
        else:
            check +=1
            dic_ticket[way[0]].append(way[1])
    print(dic_ticket)

    def dfs(node):
        sum = 0
        for i in dic_ticket:
            sum += len(dic_ticket[i])
        print("-------------",sum,answer)
        if sum == 0:
            #print("asdasdas")
            return answer
        else:
            dic_ticket[node].sort(reverse=True)
            for _ in range(len(dic_ticket[node])):
                tmp = dic_ticket[node].pop()
                answer.append(tmp)
                dfs(tmp)
                answer.pop()
                dic_ticket[node].append(tmp)

    return answer



















