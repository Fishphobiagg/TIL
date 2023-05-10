# 경쟁적 전염
from collections import deque
N, K = map(int, input().split())

지도 = [list(map(int,input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

virus=[]
for i in range(N):
    for j in range(N):
        if 지도[i][j]:
            virus.append((지도[i][j], i, j))
virus.sort()
Q = deque(virus)
sec = 0

while Q:
    if sec == S:
        break
    for _ in range(len(Q)):
        level, x, y = Q.popleft()
        for i in range(4):
            nx, ny = x + move[i][0], y + move[i][1]
            if nx < 0 or ny < 0 or nx == N or ny == N:
                continue
            if not 지도[nx][ny]:
                지도[nx][ny] = level
                Q.append((level, nx, ny))
    sec += 1

print(지도[X-1][Y-1])
