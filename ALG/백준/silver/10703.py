R, S = map(int, input().split())

aurelion_Sol = [list(input()) for _ in range(R)]
# 차이 구하기
dif = R
last_star = 0
first_star = R
for i in range(S): # 별이랑 샵 개수 세기
    low_star = -1
    for j in range(R):
        if aurelion_Sol[j][i] == 'X' and j > last_star:
            last_star = j
        if aurelion_Sol[j][i] == 'X' and j < first_star:
            first_star = j
        if aurelion_Sol[j][i] == 'X' and low_star < j :
            low_star = j
        if aurelion_Sol[j][i] == '#':
            now_dif = j - low_star
            if low_star != -1 and now_dif < dif:
                dif = now_dif
            break
dif -= 1
for i in range(last_star, first_star-1, -1):
    for j in range(S):
        if aurelion_Sol[i][j] =='X':
            aurelion_Sol[i][j] = '.'
            aurelion_Sol[i+dif][j] ='X'

for i in aurelion_Sol:
    print(''.join(i))