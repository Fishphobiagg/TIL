# 점프점프

N = int(input())
A = list(map(int, input().split()))
dp = [1 if i in range(1, A[0]+1) else 1e7 for i in range(N)]
dp[0] = 0
for i in range(1,N):
    # 못 밟은 땅인 경우 여긴 skip, 뒤에 밟은 땅 있을 수도 있으니 continue
    if dp[i] != 1e7:
        for crayon_pop in range(1, A[i]+1):
            if i+crayon_pop < N:
                dp[i+crayon_pop] = min(dp[i]+1, dp[i+crayon_pop])
print(dp[-1]) if dp[-1] != 1e7 else print(-1)