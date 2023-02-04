# Flatten

def dump(num, arr):
    arr = sorted(arr, reverse=True)
    avr = sum(arr) / len(arr)
    big = [i for i in arr if i > avr] # 평균보다 높은 층들 배열
    small = [i for i in arr if i < avr] # 평균보다 낮은 층들 배열
    can_dump = sum(big) - ((avr)*len(big)) # 밑으로 갈 수 있는 개수
    need_dump = (avr*len(small)) - sum(small) # 필요한 개수
    
    if can_dump > need_dump: # 나를 수 있는 블록의 수가 필요한 수보다 많을 경우
        if need_dump <= num: # 덤프 할 수 있는 횟수가 필요한 덤프 수보다 많을 경우
            return 1
        else: # 필요한 덤프 횟수가 할당된 덤프 횟수보다 많을 경우
            dump_count = 0
            while dump_count < num:
                big[0] = big[0] - 1
                small[-1] = small[-1] +1
                big.sort()
                small.sort()
                count += 1
            return max(big) - min(small)
    elif can_dump == need_dump and need_dump <= num: # 필요한 덤프 횟수 와 덤프할 수 있는 횟수가 같으면서, 할당된 덤프 횟수가 이보다 같거나 많은 경우
        return 0

T = 10

for test_num in range(1,T+1):
    dump_number = int(input())
    boxes = list(map(int, input().split()))    
    print(dump(dump_number, boxes))