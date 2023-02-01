T = int(input())

for Test_num in range(T):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    max_sum = 0 
    min_sum = sum(num_list[:M])
    for idx in range(0, N-M+1):
        arr_sum = sum([num_list[idx+i] for i in range(0,M)])
        if max_sum < arr_sum:
            max_sum = arr_sum
        if min_sum > arr_sum:
            min_sum = arr_sum
    
    print(f'#{Test_num+1} {max_sum - min_sum}')