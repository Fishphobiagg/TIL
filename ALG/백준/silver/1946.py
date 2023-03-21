for t in range(int(input())):
    N = int(input())
    doc = [0]*(N+1)
    for i in range(N):
        A, B = map(int, input().split())
        doc[A] = B
    top = doc[1]
    ans = 0
    for i in range(2, N+1):
        if top > doc[i]:
            top = doc[i]
        else:
            ans += 1
    print(N-ans)