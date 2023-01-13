T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = []
    if len(A) > len(B):
        c = len(A)-len(B)
        for __ in range(c):
            B.insert(0, 0)
        for i in range(0, c+1):
            sum = 0
            for a,b in zip(A, B):
                sum += a*b
            result.append(sum)
            del B[0]
            B.append(0)
    elif len(B) > len(A):
        c = len(B)-len(A)
        for __ in range(c):
            A.insert(0, 0)
        for i in range(0, c+1):
            sum = 0
            for a,b in zip(A, B):
                sum += a*b
            result.append(sum)
            del A[0]
            A.append(0)
    else:
        sum = 0
        for a,b in A, B:
            sum += a*b
        result.append(sum)
    print(f'#{_+1} {max(result)}')