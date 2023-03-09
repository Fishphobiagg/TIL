# 어떻게 사람 이름이 항승

N, L = map(int, input().split())

w = list(map(int,input().split()))
waterbomb = [1 if i in w else 0 for i in range(max(w)+1)]
cnt = 0
i = 0
for i in range(max(w)+1):
    if waterbomb[i]:
        for j in range(i,i+L):
            if j >= max(w)+1:
                break
            waterbomb[j] = 0
        cnt+=1
    if not sum(waterbomb):
        break
print(cnt)