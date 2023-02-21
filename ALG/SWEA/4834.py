T = int(input())

for test_num in range(1, T+1):
    N = int(input()) # 카드 장수 입력
    num_list = [int(number) for number in input()] # 입력받은 N개의 숫자 ai를 1개씩 리스트에 저장
    set_num = set(num_list) # 각 숫자를 세기 위해 set
    max_counted_num = 0 # 가장 많이 나온 숫자를 저장하기 위한 변수
    max_count = 0 # 가장 많이 나온 횟수를 저장하기 위한 변수
    for check_num in set_num: # 각 숫자의 개수를 세기 위한 반복문
        if num_list.count(check_num) > max_count: # 만약 check_num이 기존 최대 개수보다 많을 경우
            max_count = num_list.count(check_num) # 가장 많이 나온 숫자, 가장 많이 나온 횟수 업데이트
            max_counted_num = check_num
        elif num_list.count(check_num) == max_count and max_counted_num < check_num: # 카드 장수가 가장 많으면서 같고, 숫자는 현재 체크하는 숫자가 더 클 경우
            max_counted_num = check_num # 가장 많은 카드에 적힌 숫자 업데이트
    
    print(f'#{test_num} {max_count}')