T = int(input())
for Test_num in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))

    max_num = 0
    min_num = num_list[0]
    for i in num_list:
        if max_num < i:
            max_num = i
        if min_num > i:
            min_num = i
    print(f'#{Test_num} {max_num - min_num}')
