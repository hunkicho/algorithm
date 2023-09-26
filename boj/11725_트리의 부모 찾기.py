import sys
sys.setrecursionlimit(10 ** 6)

def dfs(node):
    for i in tree[node]:
        if visit[i] == 0:
            visit[i] = node
            dfs(i)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    tree = [[] for _ in range(N+1)]
    visit = [0] * (N + 1)

    for _ in range(N-1):
        start, end = map(int, sys.stdin.readline().split())
        tree[start].append(end)
        tree[end].append(start)
        
    dfs(1)
        
    for x in range(2, N+1):
        print(visit[x])