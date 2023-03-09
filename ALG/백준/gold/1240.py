# 노드사이의 거리

'''
N = 노드 개수
M = 노드 사이의 거리
start, end = 시작점, 끝점
dfs를 하면서, 거리를 더해가면 된다.
'''

N, M = map(int, input().split())
tree = [[] for i in range(N+1)]
for _ in range(N-1):
    a, b, dist = map(int, input().split())
    tree[a].append((b, dist))
    tree[b].append((a, dist))
def dfs(x):
    for node, dist in tree[x]:
        if not distance[node]:
            distance[node] += distance[x]+dist
            dfs(node)

for i in range(M):
    start, end = map(int, input().split())
    distance = [0]*(N+1)
    distance[start] = 1
    dfs(start)
    print(distance[end]-1)