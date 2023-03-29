'''
기본적인 컨셉
초항 : 아무 동전도 사용하지 않는 경우 - 1가지
사용하는 동전을 하나씩 늘리기, 아무것도 사용 x -> 10원 -> 10, 5원 -> 10, 5, 1원 
이전 단계에서 경우의 수가 있었던 가격 -> 이 가격부터 현재 사용하는 동전 조합 가격 더한 가격에 경우의 수 생성
'''

T = int(input())
k = int(input())

money = sorted([tuple(map(int,input().split())) for _ in range(k)], reverse=True)

dp = [0]*(T+1)
dp[0] = 1 # dp 초항 설정
for i in range(k):
    std = [0]*(T+1)
    for j in range(T+1):
        if dp[j]: 
            for y in range(1, money[i][1]+1):
                if j+money[i][0]*y > T: # 목표값을 넘는 경우
                    continue
                std[j+money[i][0]*y] += dp[j]
    dp = [std[i]+dp[i] for i in range(T+1)]
print(dp[T])