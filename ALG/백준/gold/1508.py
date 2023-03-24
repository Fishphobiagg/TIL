# 레이스 대회
'''
M : 심판 배치 수
K : 위치
N : 트랙의 길이
'''

N, M, K = map(int, input().split())
ref = list(map(int, input().split()))

start, end = 0, 1000000
ans = []
if M == K:
    print('1'*K)
    exit()
while start <= end:
    last = 0
    result = '1'
    mid = (start+end)//2
    for i in range(1, K):
        if ref[i]-ref[last] >= mid:
            result += '1'
            last = i
        else:
            result +='0'
    if result.count('1') > M:
        new_result = ''
        for i in result:
            if new_result.count('1') == M:
                new_result += '0'*(K-len(new_result))
                break
            new_result += i
        ans.append((mid, new_result))
    if result.count('1') == M:
        ans.append((mid, result))
        start = mid+1
    elif result.count('1') < M: # 적게 배치한 경우
        end = mid-1
    else:
        start = mid+1

ans.sort()
print(ans[-1][1])