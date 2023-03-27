# 동전 소매치기
import sys
input = sys.stdin.readline

'''
t원을
10원, 5원, 1원짜리로 바꾸기

다 합친 값에서 빼가기?
'''

T = int(input())
k = int(input())
dp = [0]*10001

money = [tuple(map(int,input().split())) for _ in range(k)]
money.sort()
for i in range(1, money[0][1]+1):
    dp[i*money[0][0]] += 1
for idx, i in enumerate(money):
    if not idx:
        continue
    for j in range(1,i[1]+1): # 동전 개수
        num = j*i[0]
        if num > 10000:
            continue
        for k in range(0, num+1):
            if k+num > 10000:
                continue
            dp[num+k] += 1
print(dp[T])
