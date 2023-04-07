# 롤드컵
'''
승,패의 개수 일치
무승부의
'''

match_up = []
case = []
max_win = [0]*6
max_drow = [0]*6
max_lose = [0]*6
season = [list(map(int, input().split())) for _ in range(4)]
for i in range(4):
    for j in range(0, 6):
        max_win[j] = max(max_win[j], season[i][j*3])
        max_drow[j] = max(max_drow[j], season[i][j*3+1])
        max_lose[j] = max(max_lose[j], season[i][j*3+2])
def match(x, a=[]):
    if len(a) == 2:
        match_up.append(a)
        return
    if x == 6:
        return
    match(x+1, a+[x])
    match(x+1, a)
match(0)
print(max_win, max_lose, max_drow)
def epl(x, arr=[0]*18):
    if x == 15:
        a = arr[:]
        if a in season:
            case.append(a)
        return
    home, away = match_up[x][0], match_up[x][1]
    # 홈 승
    arr[home*3]+=1
    arr[away*3+2]+=1
    if max_win[home] >= arr[home*3] and max_lose[away]>=arr[away*3+2]:
        epl(x+1, arr)
    arr[home*3]-=1
    arr[away*3+2]-=1
    # 무승부
    arr[home*3+1]+=1
    arr[away*3+1]+=1
    if max_drow[home] >= arr[home*3+1] and max_drow[away] >= arr[away*3+1]:
        epl(x+1, arr)
    arr[home*3+1]-=1
    arr[away*3+1]-=1
    # 홈 패
    arr[away*3] +=1
    arr[home*3+2] +=1
    if max_win[away] >= arr[away*3+2] and max_lose[home]>=arr[home*3]:
        epl(x+1, arr)
    arr[away*3] -=1
    arr[home*3+2] -=1
epl(0)
print(case)
for i in range(4):
    if season[i] in case:
        print('1', end=' ')
    else:
        print('0', end=' ')