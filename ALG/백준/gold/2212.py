# 센서
'''
K : 세울 수 있는 최대 집중국의 개수
N : 센서의 개수
K개의 조로 나누기
칸막이
'''
N = int(input())
K = int(input())
sensor = sorted(list(map(int,input().split())))
sub = []

for i in range(1, N):
    sub.append(sensor[i]-sensor[i-1])
sub.sort(reverse=True)
print(sum(sub[K-1:]))