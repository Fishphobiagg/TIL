T = int(input())
k = int(input())

money, a = sorted([tuple(map(int,input().split())) for _ in range(k)], reverse=True), 0

for i in range(k):
    a += money[i][0]*money[i][1]

dp = [0]*(T+1)
dp[0] = 1 # dp 초항 설정
for i in range(k):
    std = [0]*(T+1)
    for j in range(T+1):
        if dp[j]:
            for y in range(1, money[i][1]+1):
                if j+money[i][0]*y > T:
                    continue
                std[j+money[i][0]*y] += dp[j]
    dp = [std[i]+dp[i] for i in range(T+1)]
print(dp[T])