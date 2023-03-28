# 파이크 옮기기 1
'''
시작 지점부터 끝 지점까지의 좌표 사이에 있는 칸은 모두 파이프
전 end는 다음 start가 됨
45도만 꺾기 가능
'''
pipe = [list(map(int,input().split())) for _ in range(int(input()))]
dp = [[0]*len(pipe) for _ in range(len(pipe))]

start, end = (0,0), (0,1)
dp[0][0] = 1
direction = 1
move = [(1,1), (0,1), (1,0)]
def pipe_dp(s, e, d):
    x_1, y_1 = s
    x_2, y_2 = e
    if x_1 == len(pipe) or y_1 == len(pipe) or x_2 == len(pipe) or y_2 == len(pipe):
        return
    for i in range(x_1, x_2+1):
        for j in range(y_1, y_2+1):
            if pipe[i][j]: # 벽이 있을 경우
                return
    dp[x_2][y_2] += dp[x_1][y_1]
    print(dp)
    for i in range(3): # 3방향 고고
        if d == 1 and i == 2:
            continue
        if d == 2 and i == 1:
            continue
        pipe_dp(e, (e[0]+move[i][0], e[1]+move[i][1]), i)


pipe_dp(start,end, direction)
print(dp[len(pipe)-1][len(pipe)-1])