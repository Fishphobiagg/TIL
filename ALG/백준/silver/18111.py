# 마인크래프트
N, M, B = map(int, input().split())
land = []
ans_height = 0
time = 100000000000
for i in range(N):
    a = list(map(int, input().split()))
    land.append(a)
for i in range(257): # 모든 높이에 대해서 검사
    need = 0
    abs = 0
    for j in range(N):
        for k in range(M):
            if land[j][k] > i:
                abs += land[j][k] - i
            else:
                need += i - land[j][k]
    if need > abs + B:
        continue
    if need + abs*2 <= time:
        ans_height = i
        time = need + abs*2
print(time, ans_height)
