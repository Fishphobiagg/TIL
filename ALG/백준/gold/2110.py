# 플레이스테이션 설치
import sys
input = sys.stdin.readline

'''
설치 기준 거리보다 전에 설치했던 집과의 거리가 클 경우 설치
'''
N, C = map(int, input().split())
home = [int(input()) for _ in range(N)]
home.sort()
start, end = 1, home[-1] - home[0]
result = 0
if C == 2:
    print(home[-1]-home[0])
else:
    while start < end:
        mid = (start+end)//2 # 집 설치 간격
        last = home[0] # 전에 설치했던 집
        cnt = 1 #설치 개수를 저장하기 위한 변수
        for i in range(1, N):
            if mid <= home[i]-last:
                cnt += 1
                last = home[i]
        if cnt >= C: # 설치를 너무 많이 한 경우 - 간격 늘리기
            start = mid+1
            result = mid
        elif cnt < C: # 너무 적게 설치한 경우 - 간격 좁히기
            end = mid
    print(result)