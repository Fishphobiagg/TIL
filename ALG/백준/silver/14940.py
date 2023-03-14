# easy fast
from collections import deque

N, M = map(int, input().split())
kakao_map = [list(map(int, input().split())) for _ in range(N)]

start = False
for i in range(N):
    for j in range(M):
        if kakao_map[i][j] == 2:
            start = (i, j)
            break
    if start:
        break
visited =[[0]*M for _ in range(N)]
dist = [[0]*M for _ in range(N)]
dist[start[0]][start[1]] = 0
Q = deque([start])
visited[start[0]][start[1]] = 1

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while Q:
    x, y = Q.popleft()
    for i in range(4):
        nx = x + move[i][0]
        ny = y + move[i][1]
        if nx < 0 or ny < 0 or nx == N or ny == M:
            continue
        if not visited[nx][ny] and kakao_map[nx][ny]:
            visited[nx][ny] = 1
            if not dist[nx][ny]:
                dist[nx][ny] = dist[x][y] + 1
            elif dist[nx][ny] > dist[x][y] + 1:
                dist[nx][ny] = dist[x][y] + 1
            Q.append((nx, ny))

for i in range(N):
    for j in range(M):
        if not visited[i][j] and kakao_map[i][j]:
            dist[i][j] = -1

for i in dist:
    print(*i)