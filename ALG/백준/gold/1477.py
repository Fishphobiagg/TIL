# 휴게소 세우기
from collections import deque

'''
휴게소 사이 거리 최소화
딱 가운데에 세우기
휴게소가 없는 구간
'''
N, M, L = map(int, input().split())
a = list(map(int,input().split()))+[0,L]
a.sort()

# 구간의 중간값 구하기

mid = [a[i+1] - a[i] for i in range(len(a)-1)]

for idx, i in enumerate(mid):
    
    # 왼쪽 구간 세우기
    
    # 오른쪽 구간 세우기