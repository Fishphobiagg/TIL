# 놓기 전에 X 놓고 나서 타당성 검사

N = int(input())

count = 0
chess = [0]*N

def pos(x):
    for i in range(x):
        if chess[x] == chess[i] or abs(chess[i]-chess[x]) == abs(i-x):
            return 0

    return 1

def dfs(x):
    global count
    if x == N:
        count +=1
        return
    else:
        for i in range(N):
            chess[x] = i
            if pos(x):
                dfs(x+1)

dfs(0)
print(count)