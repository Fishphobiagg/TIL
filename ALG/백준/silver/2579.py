# 계단 오르기 (재귀함수)

N = int(input())

stairs = [int(input()) for i in range(N)]


def up(x):
    if x == 0:
        return stairs[0]
    if x == 1:
        return stairs[1] + stairs[0]
    elif x>= 3:
        stairs[x] = stairs[x] + max(stairs[x-1]+up(x-3), up(x-2))
    return stairs[x]
    
print(up(N-1))