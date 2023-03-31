from collections import deque
# 연구소 2
'''
1이 벽
2가 놓을 수 있는 곳
'''
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
start = []

for i in range(N): # 시작 지점 리스트에 넣기
    for j in range(N):
        if lab[i][j] == 2:
            start.append((i,j))

def combination(x, use=[]): # 시작 점 조합 만드는 함수
    if len(use) == M:
        c_set.append(use)
        return
    if x == len(start):
        return
    combination(x+1, use)
    combination(x+1, use+[start[x]])

c_set = []
combination(0)
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
ans = []
for virus in c_set: # 각 조합에 대해서 bfs
    Q = deque(virus)
    visited=[[0]*N for i in range(N)]
    for x, y in virus: # 모든 바이러스 투하 지점 visited = 1
        visited[x][y] = 1
    while Q: # bfs 시작
        x, y = Q.popleft()
        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]
            if nx == N or nx < 0 or ny == N or ny < 0:
                continue
            if lab[nx][ny] == 1 or visited[nx][ny]:
                continue
            visited[nx][ny] = visited[x][y] + 1
            Q.append((nx, ny))
    infested = True
    sec = 0
    for i in range(N): # 몇 초 걸렸는지 알아내기 위한 포문
        for j in range(N):
            sec = max(visited[i][j], sec)
            if not lab[i][j] + visited[i][j]: # 만약 감염안된 방 있을 경우
                infested = False
                break
        if not infested:
            break
    if infested: # 모두 감염됐을 때
        ans.append(sec-1)
if ans:
    print(min(ans))
else: # 감염 성공 사례 0일 경우 -1 출력
    print(-1)