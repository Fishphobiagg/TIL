# 치킨 배달
'''
도시의 치킨 거리 최소화
모든 집에서 치킨 거리 합산 -> 최소값 구하기
M = 살릴 치킨 집 개수
'''
N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

min_dist = 10000000
chicken_set = []
def select_chicken(i=0, a=[]):
    if i == len(chicken):
        if not len(a):
            return
        if len(a) <= M:
            chicken_set.append(a)
            return
        return
    select_chicken(i+1, a+[(chicken[i][0], chicken[i][1])])
    select_chicken(i+1, a)

select_chicken()
for a in chicken_set:
    total = 0
    for h_x, h_y in house:
        min_chick = 100000
        for x, y in a:
            min_chick = min(abs(h_x-x)+abs(h_y-y), min_chick)
        total += min_chick

    min_dist = min(total, min_dist)

print(min_dist)
