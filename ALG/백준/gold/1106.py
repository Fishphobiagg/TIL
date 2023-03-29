# 호텔
'''
C = 목표 인수
dp에 비용을 저장
'''


C, N = map(int,input().split())
dp = [1e7]*(C+100)
data = [tuple(map(int,input().split())) for _ in range(N)]
dp[0] = 0
for cost, cust in data:
    for i in range(C+100):
        dp[i] = min(dp[i-cust]+cost, dp[i])

print(min(dp[C:]))