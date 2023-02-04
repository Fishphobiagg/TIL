#가장 긴 증가하는 부분 수열

N = int(input())
num_list = list(map(int, input().split()))

max_count = 0

for idx, j in enumerate(num_list):
    count = 1
    standard = j
    for i in num_list[idx:]:
        if i > standard:
            count+=1
            standard = i
    if max_count < count:
        max_count = count

print(max_count)