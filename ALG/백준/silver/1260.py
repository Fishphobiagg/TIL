# 1260번 DFS와 BFS
from collections import deque

N, M, V = map(int, input().split())

graph = [[] for i in range(N)]
visited_BFS = [0 for i in range(N)]
visited_DFS = [0 for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    graph[A-1].append(B)
    graph[B-1].append(A)

visited_BFS[V-1] = 1
Q = deque([V-1])
BFS_list = [V]
DFS_list = []
# BFS (넓이)

while Q:
    bfs_index = Q.popleft()
    graph[bfs_index].sort()
    for i in graph[bfs_index]:
        if visited_BFS[i-1] == 0:
            BFS_list.append(i)
            visited_BFS[i-1] = 1
            Q.append(i-1)


# DFS (깊이)

def DFS(x):
    if visited_DFS[x-1] == 0:
        visited_DFS[x-1] = 1
        DFS_list.append(x)
        graph[x-1].sort()
        for i in graph[x-1]:
            DFS(i)

DFS(V)
print(*DFS_list)
print(*BFS_list)