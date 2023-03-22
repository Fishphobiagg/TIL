# 휴게소 세우기
'''
휴게소 사이 거리 최소화
가운데값부터 이분탐색
기존에 있는 구간에 (구간 시작 + 구간 끝)) //현재 간격  개만큼 휴게소 설치.
그렇게 모든 구간에 휴게소를 설치했을 때 설치한 휴게소의 개수가 M보다 작거나 같다면 
그 상황에서 간격의 최대값은 result가 될 것이다.

'''
N, M, L = map(int, input().split())
a = list(map(int,input().split()))+[0,L]
a.sort()

start, end = 1, L-1

while start <= end:
    mid = (start+end)//2
    cnt = 0
    for i in range(len(a)-1):
        if a[i+1]-a[i] > mid:
            cnt += (a[i+1]-a[i]-1)//mid
    if cnt > M:
        start += 1
    else:
        end = mid-1
        result = mid
print(result)