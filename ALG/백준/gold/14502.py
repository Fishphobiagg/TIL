# 연구소
from collections import deque
import copy
from itertools import combinations
'''
0 - 빈칸
1 - 벽
2 - 바이러스
세울 수 있는 벽 - 3개
'''
N, M = map(int, input().split())

지도 = [list(map(int,input().split())) for _ in range(N)]
zero_base = []
virus = []
move = [(1,0), (0,1), (-1,0), (0,-1)]


for i in range(N):
    for j in range(M):
        if not 지도[i][j]:
            zero_base.append((i, j))
        elif 지도[i][j] == 2:
            virus.append((i, j))

candidate_set = list(combinations(zero_base, 3))
max_area = 0

for i in candidate_set:
    new_map = copy.deepcopy(지도)
    Q = deque(virus)
    new_map[i[0][0]][i[0][1]], new_map[i[1][0]][i[1][1]], new_map[i[2][0]][i[2][1]] = 1, 1, 1
    cnt = 0
    while Q:
        x, y = Q.popleft()
        for j in range(4):
            nx = x + move[j][0]
            ny = y + move[j][1]
            if nx < 0 or ny < 0 or nx == N or ny == M:
                continue
            if not new_map[nx][ny]:
                new_map[nx][ny] = 2
                Q.append((nx, ny))
    for k in range(N):
        for p in range(M):
            if not new_map[k][p]:
                cnt +=1
    max_area = max(max_area, cnt)
print(max_area)