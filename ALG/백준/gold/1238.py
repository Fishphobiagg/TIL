# 파티
import sys
input = sys.stdin.readline
'''
N = 학생 수(마을 수)
M = 연결 개수
X = 목적지

'''
N, M, X = map(int, input().split())
node = [[]for _ in range(N+1)]
for i in range(M):
    A, B, dist = map(int, input().split())
    node[A].append((B, dist))
    node[B].append((A, dist))

def dijkstra(x):
    for i in node[x]:
        if not dist[i[0]]:
            dist[i[0]] = dist[x] + i[1]
            dijkstra(i[0])
        elif dist[i[0]] > dist[x] + i[1]:
            dist[i[0]] = dist[x] + i[1]
ans = [0]*(N+1)
for i in range(N):
    visited = [0]*(N+1)
    dist = [0]*(N+1)
    if N == X:
        continue
    visited[i] = 1
    dijkstra(i)
    ans[i] = dist[X]
    print(dist)
print(max(ans))