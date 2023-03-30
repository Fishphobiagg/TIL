# 파이크 옮기기 1 dfs

'''
시작 지점부터 끝 지점까지의 좌표 사이에 있는 칸은 모두 파이프
전 end는 다음 start가 됨
45도만 꺾기 가능

벽 부딪히는 경우의 수 제외하면 DP로 해결 가능
'''
pipe = [list(map(int,input().split())) for _ in range(int(input()))]
N = len(pipe)
end = (0,1)
direction = 1 # 1 = 가로 0 = 대각 2 = 세로
cnt = 0
def dfs(e,d):
    global cnt
    if d == 0:
        if e[0]+1<N and e[1]+1<N:
            if not pipe[e[0]][e[1]]+pipe[e[0]+1][e[1]]+pipe[e[0]][e[1]+1]+pipe[e[0]+1][e[1]+1]:
                if (e[0]+1, e[1]+1) == (N-1, N-1):
                    cnt +=1
                elif e[0]+1<N and e[1]+1<N:
                    dfs((e[0]+1, e[1]+1), 0)
        if e[1]+1 < N:
            if not pipe[e[0]][e[1]] + pipe[e[0]][e[1]+1]:
                if (e[0], e[1]+1) == (N-1, N-1):
                    cnt +=1
                elif e[1]+1 < N-1:
                    dfs((e[0], e[1]+1), 1)
        if e[0]+1 < N:
            if not pipe[e[0]][e[1]] + pipe[e[0]+1][e[1]]:
                if (e[0]+1, e[1]) == (N-1, N-1):
                    cnt +=1
                elif e[0]+1 < N-1:
                    dfs((e[0]+1, e[1]), 2)
    elif d == 1:
        if e[0]+1 < N and e[1]+1<N:
            if not pipe[e[0]][e[1]]+pipe[e[0]+1][e[1]]+pipe[e[0]][e[1]+1]+pipe[e[0]+1][e[1]+1]:
                if (e[0]+1, e[1]+1) == (N-1, N-1):
                    cnt +=1
                elif e[0]+1<N and e[1]+1<N:
                    dfs((e[0]+1, e[1]+1), 0)
        if e[1]+1<N:
            if not pipe[e[0]][e[1]] + pipe[e[0]][e[1]+1]:
                if (e[0], e[1]+1) == (N-1, N-1):
                    cnt +=1
                elif e[1]+1 < N-1:
                    dfs((e[0], e[1]+1), 1)
    else:
        if e[0]+1 < N and e[1]+1<N:
            if not pipe[e[0]][e[1]]+pipe[e[0]+1][e[1]]+pipe[e[0]][e[1]+1]+pipe[e[0]+1][e[1]+1]:
                if (e[0]+1, e[1]+1) == (N-1, N-1):
                    cnt +=1
                elif e[0]+1<N and e[1]+1<N:
                    dfs((e[0]+1, e[1]+1), 0)
        if e[0]+1 <N:
            if not pipe[e[0]][e[1]] + pipe[e[0]+1][e[1]]:
                if (e[0]+1, e[1]) == (N-1, N-1):
                    cnt +=1
                elif e[0]+1 < N-1:
                    dfs((e[0]+1, e[1]), 2)

dfs(end, direction)
print(cnt)