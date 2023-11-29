import sys
from collections import deque

# 위상정렬 순서
# 1. 진입차수가 0인 정점을 큐에 삽입
# 2. 큐에서 원소를 꺼내어 해당 원소와 연결된 간선을 모두 제거
# 3. 제거한 후에 진입차수가 0인 정점을 큐에 삽입
# 4. 2 ~ 3 반복

# 왜 위상정렬일까?
# 순서가 종속적이다(순서가 있다.), 비교 값이 일부만 있다.

# n = 학생의 수
# m = 키를 비교한 회수

n, m = map(int, sys.stdin.readline().split())
indegree = [0] * (n + 1) # 진입 차수 저장
graph = [[] for _ in range(n + 1)] # 노드 연결정보 저장


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

result = []
q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    result.append(node)

    for j in graph[node]:
        indegree[j] -= 1
        if indegree[j] == 0:
            q.append(j)

for res in result:
    print(res, end=' ')
