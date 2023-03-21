# 고층 건물

'''
한 점에서 다른 한점을 잇는 선분의 기울기를 저장ㅈ
자신보다 큰 빌딩이 나올 경우, 그거보다 작은 빌딩은 더이상 보이지 않음
자신보다 작은 빌딩은 그 전 작은 빌딩 기울기의 가장 큰 값과 비교, 우측일 경우 더 가파르면,
좌측일 경우 더 완만하면 보임 즉 최소값보단 크고 최대값보단 작아야함
'''

N = int(input())
buildings = list(map(int, input().split()))
ans = 0 # 정답 출력용
for i in range(N): # 기준 빌딩 정하기
    signiel = 0 # 해당 빌딩에서 보이는 개수
    incline = [0]*N #기울기 저장할 리스트
    for j in range(N):
        if i == j: #자기 자신 스킵
            continue
        incline[j] = buildings[i] - buildings[j] / (i - j)
    # 오른쪽
    max_right = 
    for j in range(i, N):
    # 왼쪽
    # 바로 옆이 큰 경우
    # 바로 옆이 작은 경우
    for j in range(i, -1, -1):
        
    
print(ans)