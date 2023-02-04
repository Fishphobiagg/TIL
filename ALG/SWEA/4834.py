T = int(input())

for test_num in range(1, T+1):
    N = int(input())
    num_list = [int(number) for number in input()]
    set_num = set(num_list)
    max_counted_num = 0
    max_count = 0
    for check_num in set_num:
        if num_list.count(check_num) > max_count:
            max_count = num_list.count(check_num)
            max_counted_num = check_num
        elif num_list.count(check_num) == max_count and max_counted_num < check_num:
            max_counted_num = check_num
    
    print(f'#{test_num} {max_count}')