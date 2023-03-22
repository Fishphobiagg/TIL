# 플레이스테이션 설치
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
home = [int(input()) for _ in range(N)]
home.sort()
result = 0
start, end = 1, home[-1] - home[0]
if C == 2:
    print(home[1]-home[0])
    exit()

while start < end:
    now = (start+end)//2
    cnt = 1
    last = 0
    for i in range(1, N):
        if home[i]-home[last] >= now:
            cnt += 1
            last = i
    if cnt >= C:
        result = now
        start = now+ 1
    elif cnt < C:
        end = now
print(result)