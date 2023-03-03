# 젤다와 링크

from itertools import combinations

'''
팀 인원수 - N/2명
-> 4c2 를 하면 된다...
거기서 또 두명씩 부분 집합... 해서 팀 능력치 더하기...
'''
start_link = [list(map(int,input().split())) for _ in range(int(input()))]
min_stats = 1000000
# 부분집합 구하기
for team in combinations(range(len(start_link)), len(start_link)//2):
    start = 0
    link = 0
    team_link = []
    for i in range(len(start_link)):
        if i not in team:
            team_link.append(i)
    for status in combinations(team, 2):
        x, y = status
        start += start_link[x][y] + start_link[y][x]
    for status in combinations(team_link, 2):
        x, y = status
        link += start_link[x][y] + start_link[y][x]
    if min_stats > abs(start-link):
        min_stats = abs(start-link)
print(min_stats)