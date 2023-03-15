# 고층 건물

'''
두 빌딩을 잇는 기울기 < 그 전까지 있는 빌딩들의 기울기
바로 옆 건물은 볼 수 있음
'''

N = int(input())
buildings = list(map(int, input().split()))

if N == 1:
    print(0)
    exit()
if N == 2:
    print(1)
    exit()

cnt = [0]*N

for i in range(N): #기준 빌딩
    incline = [0]*N
    cnt = 0
    # 왼쪽 건물 확인
    for j in range(i-1, -1, -1):
        if j == i+1:
            cnt += 1
    # 오른쪽 건물 확인
    for j in range(i+1, N):
        if j == i+1:
            cnt += 1
            incline[j] = (buildings[i]-buildings[j])/(i-j)
            continue
        incline[j] = (buildings[i]-buildings[j])/(i-j)
        if incline[j]
print(max(cnt))