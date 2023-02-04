N = int(input())

def sorting(num_list):
    pivot = sorted(num_list)[len(num_list)//2]
    

A = [int(input()) for i in range(N)]
max_count = 0
max_num = 0
# 산술 평균
print(round(sum(A)/N))

C =set(A)
# 중앙값
count = 0
while True:
    T = min(C)
    C.discard(min(C))
    count += 1
    if count == len(A)//2:
        print(min(C))
        break
# 최빈값
B = set(A)
for i in B:
    if A.count(i) > max_count:
        max_count = A.count(i)
        max_num = i
    elif A.count(i) == max_count:
        if max_num > i:
            max_num = i
    
# 범위
print(max(A) - min(A))
