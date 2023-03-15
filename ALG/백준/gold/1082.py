# 1082 방 번호

'''
M원까지 dp를 만들고, 각 요금마다 최대의 숫자를 dp에 넣어놓으면 된다.
그 뒤는 최대의 숫자에
'''

N = int(input())
num_price = list(map(int, input().split()))
M = int(input())

dp = [0]*(M+1)
for i in range(N):
    if num_price[i] > M:
        continue
    dp[num_price[i]] = i
def room_number(x):
    for i in range(N):
        if x + num_price[i] <= M:
            if not dp[x+num_price[i]]:
                num = ''
                for k in sorted(str(dp[x]) + str(i), reverse=True):
                    num += k
                dp[x+num_price[i]] = int(num)
                room_number(x+num_price[i])
            else:
                num = ''
                for k in sorted(str(dp[x]) + str(i), reverse=True):
                    num += k
                if dp[x+num_price[i]] < int(num):
                    dp[x+num_price[i]] = int(num)
                    room_number(x+num_price[i])

for i in num_price:
    room_number(i)

print(max(dp))