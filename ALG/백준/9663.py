# N_Queen
N = int(input())

# 기울기가 같을 경우, 놓은 열이 같을 경우 다시 back
# 0, 1, 2, 3, 4, 5, 6, 7 각각 한개씩 할당, |행인덱스 - 열|이 다 달라야함
# 대각선을 오른족만 고려하면 된다.
# 이 문제의 경우, visited가 아니라 대각선 여부로 판단해서 재귀함수를 탈출하면 된다.
queen = [0 for i in range(N+1)]
count = 0
visited = [0 for i in range(N)]
queen[1] = 1
def dfs(x):
    for i in range(1, N+1):
        if not visited[i] and :
            visited[i] = 1
            queen[x] == i
            dfs(x+1)
            break