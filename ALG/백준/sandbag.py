match_up = []
result = [[0]*6 for _ in range(4)]

for i in range(4):
    season = list(map(int,input().split()))
    for j in range(0, 6):
        result[i][j] = season[j*3]*3 + season[j*3+1]

print(result)
print(3**15)