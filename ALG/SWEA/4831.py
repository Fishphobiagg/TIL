# N 종점 정류장(인덱스) 한 번 충전으로 이동할 수 있는 정류장 수 : K, M : 충전소 개수

T = int(input())

for test_num in range(1, T + 1):
    K, N, M = map(int, input().split()) # 연비, 정류장 개수, 충전소 개수
    charge_count = 0 # 충전 횟수
    driving_distance = 0 # 버스가 이동한 거리
    charge_index = list(map(int, input().split())) # 충전소 위치
    while driving_distance < N: 
        # 충전을 진행한 곳 기준으로 출발
        # 현재 위치에서 가지고 있는 연료로 갈 수 있는 충전소 리스트
        charge_list = [i for i in charge_index if i > driving_distance and driving_distance + K >= i]
        if charge_list: # 갈 수 있는 충전소가 존재할 경우
            driving_distance = max(charge_list) # 차를 가장 먼 거리의 충전소로 이동
            charge_count +=1 # 충전 횟수 +1
            if driving_distance + K >= N: # 만약 현재 배터리로 도착지를 갈 수 있을 경우 반복문 탈출
                break
        else: # 현재 연료로 갈 수 있는 충전소가 없는 경우
            charge_count = 0
            break
        
    print(f'#{test_num} {charge_count}')
