# 카드 스까무라
'''
P - 현재 이 카드가 2번으로 가야함, 계속해서 이 숫자를 옮겨서 정렬이 되어야함, 즉 (0, 1, 2), (0, 1, 2)의 형태가 되어야함
S - 카드를 섞는 방법, [1, 2, 0] 이면 0번쨰 위치에 있던 카드는 1번째로, 1번째는 2번째로, 2번째는 0번째로 간다
최소값이기 때문에 계속해서 시도하면서 정렬이 됐을 경우 중지,
초기값과 같은 값이 나왔을 경우 중단, 답 없음 처림
'''
N = int(input())
answer = list(range(3))*(N//3)
P = list(map(int, input().split()))
S = list(map(int, input().split()))
cards = P[:]
cnt = 0

while cards!=answer:
    new = [0]*N
    for i in range(N):
        new[S[i]] = cards[i]
    cards = new
    cnt+=1
    if cards == P:
        print(-1)
        exit()
print(cnt)