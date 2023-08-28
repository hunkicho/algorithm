from collections import deque
def solution(n, edge):
    answer = 0
    
    route = [0] * (n+1)
    graph = [[] for i in range(n+1)]
    
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    
    q = deque()
    q.append(1)
    route[1] = 1
    
    while q:
        now = q.popleft()
        for g in graph[now]:
            if route[g] == 0:
                q.append(g)
                route[g] = route[now] + 1
    
    max_route = max(route)
    
    for j in route:
        if j == max_route:
            answer += 1
    
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))