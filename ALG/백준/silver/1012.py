# 유기농 배추 / DFS

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    elif farm[x][y] == 1:

        farm[x][y] = 0

        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x+1, y)
        return True
    return False

T = int(input())

for test in range(T):
    M, N, K = map(int, input().split())
    farm = [[0]*M for i in range(N)]
    result = 0
    for i in range(K):
        A, B = map(int, input().split())
        farm[A][B] = 1
    for i in range(N):
        for j in range(M):
            if dfs(i, j):
                result += 1
    print(result)