# 동물원

'''
N = 우리의 크기
'''

N = int(input())
if N == 1:
    print(3)
    exit()
dp = [0]*(N+1)
dp[0] = 1
dp[1] = 3

for i in range(2, N+1):
    dp[i] = (dp[i-2]+dp[i-1]*2)%9901

print(dp[-1])