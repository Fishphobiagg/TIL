    # 아기상어뚜루룰루뚜루
from collections import deque
'''
0 : 빈칸
1~6 : 물고기의 크기
9 : 아기상어

더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.

엄마 상어에게 요청하기 전까지의 시간
아기상어의 크기 - 자신의 크기가 n일 경우 N마리 먹으면 +1 ,시작 크기 - 2
자기보다 작거나 같은 크기의 물고기만 먹을 수 있음

visited 필요없음, 해당경로에 다른 상어가


'''

N = int(input())

fishbowl = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if fishbowl[i][j] == 9:
            start = (i, j) # 시작 지점 구하기
            fishbowl[i][j] = 0
# 방문할 수 있는 물고기의 좌표+거리+크기 반환
move = [(0,1), (1,0), (-1,0), (0,-1)]
time = 0  # 거리만큼 더해주기
stack = 0
shark = 2
while True:
    Q = deque([start])
    visited = [[0]*(N)for _ in range(N)]
    catch = 0
    while Q: #한번 사이클
        x, y = Q.popleft()
        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]
            if nx < 0 or ny < 0 or nx == N or ny == N:
                continue
            if (nx, ny) == start:
                continue
            if not visited[nx][ny]:
                if shark < fishbowl[nx][ny]:
                    continue
                if not fishbowl[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    Q.append((nx,ny))
                elif fishbowl[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    if not catch:
                        catch = (nx, ny)
                    else:
                        if visited[nx][ny] < visited[catch[0]][catch[1]]:
    if not catch:
        break
    catch.sort()
    print(catch)
    fishbowl[catch[0][1]][catch[0][2]] = 0
    time += catch[0][0]
    stack += 1
    if stack == shark:
        shark += 1
        stack = 0
    start = (catch[0][1], catch[0][2])
print(time)