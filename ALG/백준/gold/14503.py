#로봇 청소기

'''
회전 -> 방향 -1

0은 청소되지않은 칸
1은 벽
'''
N, M = map(int,input().split())
robot_x, robot_y, direction = map(int,input().split())
room = [list(map(int, input().split())) for _ in range(N)]

move = [(-1,0), (0,1), (1,0), (0,-1)] # 북, 동, 남, 서

def turn(): # 반시계 회전
    global direction
    if not direction:
        direction = 3
    else:
        direction -= 1

def check_around(x, y): # 주변 확인하는 함수
    if not room[x][y+1] or not room[x+1][y] or not room[x-1][y] or not room[x][y-1]:
        return True
    else:
        return False

nx = robot_x
ny = robot_y
clean = 0
while True:
    if not room[nx][ny]:
        room[nx][ny] = 2
        clean += 1
    if check_around(nx, ny): # 주변에 빈칸 있는 경우
        for i in range(4):
            turn() #반시계로 돌기
            if not room[nx+move[direction][0]][ny+move[direction][1]]: #빈칸인 경우 전진
                nx += move[direction][0]
                ny += move[direction][1]
                break
    else:
        if room[nx-move[direction][0]][ny-move[direction][1]] == 1: # 후진 대상 칸이 벽
            break # 사이클 종료
        else: # 후진 가능
            nx -= move[direction][0]
            ny -= move[direction][1]
print(clean)