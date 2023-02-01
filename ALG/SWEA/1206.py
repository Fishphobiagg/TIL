#View

for case_num in range(10):
    N = int(input())
    buildings = list(map(int,input().split())) # 건물의 높이를 입력 받을 리스트
    right_view = 0 # 조망권 세대 수를 저장할 변수
    around_index = [-2 ,-1, 1, 2]
    for idx, building in enumerate(buildings[2:-2]):
        around = [buildings[idx+2+i] for i in around_index] # 양옆 2칸 건물들의 높이
        if building > max(around): # 기준 건물이 양옆 2칸 건물들보다 클 경우
            right_view += building - max(around) # 양옆 2칸 건물들 중 가장 큰 건물과 높이 차이가 조망권 세대 수
    print(f'#{case_num+1} {right_view}')