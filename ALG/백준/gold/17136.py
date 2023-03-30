# 색종이 붙이기
'''
색종이를 크기가 10×10인 종이 위에 붙이려고 한다.
종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 0 또는 1이 적혀 있다.
1이 적힌 칸은 모두 색종이로 덮여져야 한다.
색종이를 붙일 때는 종이의 경계 밖으로 나가서는 안되고, 겹쳐도 안 된다.
또, 칸의 경계와 일치하게 붙여야 한다. 0이 적힌 칸에는 색종이가 있으면 안 된다.

1의 개수 - 넓이
1의 개수 = 색종이 넓이
1부터 5까지 색종이의 개수 리스트 [0 0 0 0 0]

백트래킹은 어디서? -> 정사각형의 크기 판단하는데에 사용? ㄴㄴ
4*4, 5*5 색종이는 최대 4장까지 사용 가능,


색종이 개수의 조합을 가지치기하는 것이다.

'''
p_map = [list(map(int, input().split())) for _ in range(10)]
# area = 0
# # 총 넓이 구하기
# for i in range(10):
#     for j in range(10):
#         if p_map[i][j]:
#             area += 1

# 모든 면이 칠해져 있을 경우
# if area == 100:
#     print(4)
#     exit()
#
# arr = [0]*6
# ans = []
#
# def back(x):
#     global ans
#     if x == 0:
#         a = sum([(i**2)*arr[i] for i in range(1,6)])
#         if a == area:
#             print(arr)
#             ans.append(arr[:])
#         return
#     for i in range(5,-1,-1):
#         arr[x] = i
#         if sum([arr[i] * (i ** 2) for i in range(1, 6)]) <= area:
#             back(x-1)

# back(5)

# 사각형 개수 구하기
ractangular = [0]*6
for k in range(5,0,-1):
    # 짝수/홀수
    if k%2:
        for i in range(k//2,10-k//2):
            for j in range(k//2, 10-k//2):
                if k == 1:
                    if p_map[i][j] == 1:
                        ractangular[1] +=1
                        p_map[i][j] = 0
                if sum([p_map[q][p] for q in range(i-k//2, i+k//2+1) for p in range(j-k//2, j+k//2+1)]) == k**2:
                    ractangular[k] += 1
                    for q in range(i-2, i+3):
                        for p in range(j-2, j+3):
                            p_map[q][p] = 0
    elif k == 2: # 우측 하단으로만 검사
        for i in range(9):
            for j in range(9):
                if sum([p_map[q][p] for q in range(i, i+2) for p in range(j, j+2)]) == 4:
                    ractangular[2] +=1
                    for q in range(i, i+2):
                        for p in range(j, j+2):
                            p_map[q][p] = 0
    elif k == 4:
        for i in range(7):
            for j in range(7):
                if sum([p_map[q][p] for q in range(i, i+4) for p in range(j, j+4)]) == 16:
                    ractangular[2] += 1
                    for q in range(i, i+4):
                        for p in range(j, j+4):
                            p_map[q][p] = 0
    print(p_map)
print(ractangular)