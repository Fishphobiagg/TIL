# 효율적인 해킹
from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

trust = [[] for i in range(N + 1)]
ans = [0 for _ in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    trust[B].append(A)

def bfs(x):
    count = 0
    Q = deque([x])
    visited = [0] *(N+1)
    visited[x] = 1
    while Q:
        count += 1
        c = Q.popleft()
        for j in trust[c]:
            if not visited[j]:
                Q.append(j)
                visited[j] = 1
    return count

for i in range(1, N+1):
    ans[i] = bfs(i)
for i in range(1, N+1):
    if max(ans) == ans[i]:
        print(i, end=' ')