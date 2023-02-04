from collections import deque
N = int(input())
connection = int(input())
visited = [0 for i in range(N)]
c_list = list([] for i in range(N))
for i in range(connection):
    A,B = map(int,input().split())
    c_list[A-1].append(B)
    c_list[B-1].append(A)
visited[0] = 1
Q = deque([1])
#BFS 넓이 우선 탐색
while Q:
    c=Q.popleft()
    for nx in c_list[c-1]:
        if visited[nx-1]==0:
            Q.append(nx)
            visited[nx-1]=1

# DFS 깊이 우선 탐색 // 시간이 더 오래걸림
# def check(x):
#     visited[x-1] = 1
#     for i in c_list[x-1]:
#         if visited[i-1] == 0:
#             check(i)
# check(1)

print(sum(visited)-1)

# https://bio-info.tistory.com/152 참고