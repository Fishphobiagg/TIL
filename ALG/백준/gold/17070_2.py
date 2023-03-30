# 파이크 옮기기 1 version 2

pipe = [list(map(int,input().split())) for _ in range(int(input()))]
N = len(pipe)

start, end = (0,0), (0,1)

move = [(1,1),(0,1),(1,0)]
d = 1
cnt = 0
def pipe_dp(s, e, direction):
    global cnt
    # dp에 축적
    x_1, y_1 = s
    x_2, y_2 = e
    if e == (N-1, N-1):
        cnt +=1
        return
    for i in range(3):
        if (direction == 1 and i ==2) or (direction == 2 and i ==1):
            continue
        nx,ny = x_2 + move[i][0], y_2 + move[i][1]
        if nx == N or ny == N:
            continue
        if not sum([pipe[k][j] for j in range(y_2, ny+1) for k in range(x_2, nx+1)]):
            if nx == N-1 and ny == N-1:
                pipe_dp(e, (nx, ny), i)
                continue
            if (i==2 and nx == N-1) or (i == 1 and ny == N-1):
                continue
            pipe_dp(e, (nx, ny), i)
pipe_dp(start, end,d)
print(cnt)