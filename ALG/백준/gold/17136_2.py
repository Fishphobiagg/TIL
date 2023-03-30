import copy
p_map = [list(map(int, input().split())) for _ in range(10)]
area = 0
# 총 넓이 구하기
for i in range(10):
    for j in range(10):
        if p_map[i][j]:
            area += 1

# 모든 면이 칠해져 있을 경우
if area == 100:
    print(4)
    exit()
karina = [[] for _ in range(6)]
for i in range(5, 1, -1):
    new_map = copy.deepcopy(p_map)
    num = 0
    for j in range(0, 11-i): # 후보지 등록
        for k in range(0, 11-i):
            if sum([new_map[p][q] for p in range(j, j+i) for q in range(k, k+i)]) == i**2:
                karina[i].append((j,k))

def kazuha(x): # 놓을 수 있는지 확인하는 함수
    if sum([cnt[i]*i**2 for i in range(1,6)]) > area: # 넓이
        return False
    return True
    pass
ans = [[] for _ in range(6)]

def minji(x, a_area, arr, cnt): # 놓고 순열 생성하는 함수
    if x == 1:
        if area - a_area > 5:
            return
        else:

    if karina[x]:
        for a, b in karina[x]:
            new = arr[:]
            # 순서대로 하나씩 놓아보기
            for i in range(a, a+x):
                for j in range(b,b+x):
                    new[i][j] = 0
            # 남은 후보지 몰색
            new_candidate = []
            for c, d in karina[x]:
                if sum(new[i][j] for i in range(c, c+x) for j in range(d, d+x)) == x**2:
                    new_candidate.append((c, d))
            if new_candidate:


    else:
        minji(x-1, a_area, arr)