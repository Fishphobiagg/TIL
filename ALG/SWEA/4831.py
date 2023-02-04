# N 종점 정류장(인덱스) 한 번 충전으로 이동할 수 있는 정류장 수 : K, M : 충전소 개수

T = int(input())

for test_num in range(1, T + 1):
    K, N, M = map(int, input().split())
    charge_count = 0
    driving_distance = 0
    battery = K
    charge_index = list(map(int, input().split()))
    while driving_distance < N:
        charge_list = [i for i in charge_index if i > driving_distance and driving_distance + K >= i]
        if charge_list:
            driving_distance = max(charge_list)
            charge_count +=1
            if driving_distance + K >= N:
                break
        else:
            charge_count = 0
            break
    print(f'#{test_num} {charge_count}')
