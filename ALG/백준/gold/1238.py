# 파리온어위캔드 들어가기 싫어 너가 없는 우리 집에
import sys
import heapq
input = sys.stdin.readline

'''
N : 학생의 수
M : 간선의 수
X : 목표 마을

가는 거 따로
오는 거 따로

'''
N, M, X = map(int, input().split())
road = [[]for _ in range(N+1)]

dist_go = [0]*(N+1)
dist_X = [1e7]*(N+1)
for _ in range(M):
    A, B, T = map(int,input().split())
    road[A].append((B, T))

dist_X[X] = 0
Q = []
heapq.heappush(Q, (0, X))


# 돌아오는 비행기편
while Q:
    d, x = heapq.heappop(Q)
    if dist_X[x] < d:
        continue
    for i in road[x]:
        if d + i[1] < dist_X[i[0]]:
            dist_X[i[0]] = d+i[1]
            heapq.heappush(Q, (dist_X[i[0]], i[0]))

# 가는 비행기
for i in range(1, N+1):
    dist = [1e7]*(N+1)
    if i == X:
        continue
    dist[i] = 0
    Q = []
    heapq.heappush(Q, (0, i))
    while Q:
        d, x = heapq.heappop(Q)
        if dist[x] < d:
            continue
        for k in road[x]:
            if d + k[1] < dist[k[0]]:
                dist[k[0]] = d+k[1]
                heapq.heappush(Q, (dist[k[0]], k[0]))
    dist_go[i] = dist[X]
print(max(([dist_X[i] + dist_go[i] for i in range(1, N+1)])))