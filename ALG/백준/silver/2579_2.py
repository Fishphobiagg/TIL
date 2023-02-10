# 계단 오르기
'''
결승점을 밟아야하고, 최대값을 구해야된다
'''
N = int(input())

stairs = [0 for i in range(301)]
for i in range(1,N+1):
    stairs[i] = int(input())
steps = [0 for i in range(301)]
steps[1] = stairs[1]
steps[2] = stairs[2]+stairs[1]

if N == 1:
    print(steps[1])
elif N == 2:
    print(steps[2])
else:
    for i in range(3, N+1):
        steps[i] = stairs[i] + max(stairs[i-1] + steps[i-3], steps[i-2])
    print(steps[N])
        