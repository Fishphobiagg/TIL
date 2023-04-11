# 색종이 붙이기

area = [list(map(int,input().split())) for _ in range(10)]
ans = [] # 정답 리스트
can_cover = [[] for _ in range(6)]

# 5~1까지 놓을 수 있는 공간
def find(x=5): # 왼쪽 위 꼭지점 기준으로 생각
    if x==1:
        return
    for i in range(0,10-x+1):
        for j in range(0,10-x+1):
            if area[i][j]:
                if sum([area[a][b] for a in range(i, i+x) for b in range(j, j+x)]) == x**2:
                    can_cover[x].append((i,j))
    find(x-1)
find()

def cover(size, x, y, arr):
    for i in range(x, x+size):
        for j in range(y, y+size):
            arr[i][j] = 0

def uncover(size, x, y, arr):
    for i in range(x, x+size):
        for j in range(y, y+size):
            arr[i][j] = 1

def back(x=5, arr=[0]*6):
    if x == 1:
        a = sum([area[i][j] for i in range(10) for j in range(10)])
        if a > 5:
            return
        else:
            arr[1] += a
            ans.append(sum(arr))
            return
    if arr[x] == 5:
        back(x-1, arr)

    else:
        for i in can_cover[x]: # 놓을 수 있는 경우 놓고 백트랙
            a = sum([area[c][d] for c in range(i[0], i[0]+x) for d in range(i[0], i[0]+x)])
            if a == x**2: # 만약 놓을 수 있는 곳인 경우
                cover(x, i[0], i[1], area)
                arr[x] += 1
                back(x, arr)
                uncover(x, i[0], i[1], area)
                arr[x] -= 1
back()
print(ans)

print(min(ans))