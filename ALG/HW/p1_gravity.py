
T = int(input())

for test_num in range(T):
    L = int(input())
    length_list = list(map(int, input().split())) # 블록의 길이를 입력 받을 리스트
    distance_list = [] # 낙차들을 저장할 리스트
    for idx, length in enumerate(length_list): # 낙차를 계산할 블록 층의 인덱스와 해당 층의 길이
        distance = 0
        for length_2 in length_list[idx::]: # length_2 낙차를 계산할 층부터 밑에 있는 층들의 길이
            if length > length_2: # 자신보다 짧은 층이 있을 경우 낙차 +1
                distance += 1 
        distance_list.append(distance) # 낙차 리스트에 저장
    print(f'#{test_num+1} {max(distance_list)}')