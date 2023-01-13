T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = []
    if len(A) > len(B):
        c = len(A)-len(B)
        for __ in range(c):
            B.append(0)
        for i in range(0, c):
            sum = 0
            for a,b in zip(A, B):
                sum += a*b
            result.append(sum)
            B[i] = B[i-1]
    elif len(B) > len(A):
        c = len(B)-len(A)
        for __ in range(c):
            A.append(0)
        for i in range(0, c):
            sum = 0
            for a,b in zip(A, B):
                sum += a*b
            result.append(sum)
            A[c] = A[c+i]
    else:
        sum = 0
        for a,b in A, B:
            sum += a*b
        result.append(sum)
    print(result)
    print(f'#{_+1} {max(result)}')