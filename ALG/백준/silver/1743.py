# 음식물 피하기

import sys
sys.setrecursionlimit(100000)

N, M, K = map(int, input().split())
trash_map = [[0]*M for i in range(N)]

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(x,y):
    global count
    for i in range(4):
        nx = x + move[i][0]
        ny = y + move[i][1]
        if nx < 0 or ny < 0 or ny >= M or nx >= N:
            continue
        if not trash_map[nx][ny]:
            continue
        if not visited[nx][ny]:
            count += 1
            visited[nx][ny] =1
            dfs(nx, ny)

for i in range(K):
    A, B = map(int, input().split())
    trash_map[A-1][B-1] = 1
area_list = []
for i in range(N):
    for j in range(M):
        if not trash_map[i][j]:
            continue
        visited = [[0]*M for _ in range(N)]
        visited[i][j] = 1
        count = 1
        dfs(i, j)
        area_list.append(count)
if not area_list:
    print(0)
else:
    print(max(area_list))



