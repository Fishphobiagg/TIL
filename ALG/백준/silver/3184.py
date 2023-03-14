# sheep
from collections import deque


'''
. - 빈 필드
# 울타리
o - 양
v - 늑대
'''
R, C = map(int, input().split())

farm = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
result_wolf = 0
result_sheep = 0
for i in range(R):
    for j in range(C):
        sheep = 0
        wolf = 0
        if not visited[i][j] and farm[i][j] != '#':
            Q = deque([(i, j)])
            visited[i][j] = 1
            while Q:
                x, y = Q.popleft()
                if farm[x][y] == 'o':
                    sheep += 1
                if farm[x][y] == 'v':
                    wolf += 1
                for k in range(4):
                    nx = x + move[k][0]
                    ny = y + move[k][1]
                    if nx < 0 or ny < 0 or nx == R or ny == C:
                        continue
                    if not visited[nx][ny] and farm[nx][ny] != '#':
                        visited[nx][ny] = 1
                        Q.append((nx, ny))
            if wolf < sheep:
                result_sheep += sheep
            else:
                result_wolf += wolf
print(result_sheep, result_wolf)