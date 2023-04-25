# 잠시만 안녕

'''
T초가 지나고 방에 남아있는 먼지의 양
확산 되는 양 = A//5

확산 -> 작동 순 `
'''

R, C, T = map(int, input().split())
room = [list(map(int,input().split())) for _ in range(R)]

move = [(0, 1), (1, 0), (-1, 0), (0, -1)]

for i in range(R):
    if room[i][0]:
        purifier = (i, i+1)

def diffusion():
    dif_list = []
    unit = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if room[i][j]:
                dif_list.append((i,j))
    for x, y in dif_list: # 확산
        dif_amount = room[x][y]//5
        for i in range(4):
            nx, ny = x+ move[i][0], y+move[i][1]
            if nx < 0 or ny < 0 or nx == R or ny == C:
                continue
            if (nx, ny) == (purifier[0],0) or (nx,ny) == (purifier[1],0):
                continue
            unit[nx][ny] += dif_amount
            unit[x][y] -= dif_amount
    # 확산값 적용
    for i in range(R):
        for j in range(C):
            room[i][j] += unit[i][j]

def yunakim():
    unit = room[:]
    unit[purifier[0]][0], unit[purifier[1]][0] = -1, -1
    # 오른쪽으로 이동할 구간 - 청정기의 오른쪽
    for i in range(1, C-1):
        unit[purifier[0]][i+1] = room[purifier[0]][i]
        unit[purifier[0]][i+1] = room[purifier[1]][i]
    # 위 아래
    for i in range(purifier[0]):
        if i+1 == purifier[0]:
            continue
        unit[i+1][0] = room[i][0]
    for i in range(R-1, purifier[1], -1):
        if i-1 == purifier[1]:
            continue
        unit[i-1][0] = room[i][0]
    # 왼쪽으로 이동할 구간
    for i in range(1, C-1):
        unit[0][i] = room[0][i+1]
        unit[R-1][i] = room[R-1][i+1]
    # 반대편 끝쪽 구간
    for i in range(purifier[1], R-1):
        unit[i+1][C-1] = room[i][C-1]
    for i in range(purifier[0], 0, -1):
        unit[i-1][C-1] = room[i][C-1]
    for i in range(R):
        for j in range(C):
            room[i][j] = unit[i][j]

for k in range(T):
    print(room)
    diffusion()
    yunakim()
    print(room)
total = 2
for i in range(R):
    total += sum(room[i])

print(total)