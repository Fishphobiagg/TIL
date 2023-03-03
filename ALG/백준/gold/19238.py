# 스타트 택시
from collections import deque
'''
M = 승객 수
Fuel = 연료
0은 빈칸, 1은 벽

연료 충전 - 목적지에 도착하면 이동한 거리만큼 충전, (단, 이동은 무조건 최단거리로)

못가는 경우는 2가지

1. 연료가 바닥나서 못가는 경우
2. 벽으로 가로막혀 있어서 못가는 경우

택시는 이동거리가 가장 짧은 고객부터 간다. 만약 그런 고객이 여러명이라면,
행 인덱스가 작은 애들부터, 그 다음은 열 인덱스가 작은 애들부터 먼저 간다
'''
N, M, Fuel = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
taxi_x, taxi_y = map(int, input().split())
c_start = []
c_dest = []
for i in range(M):
    a = list(map(int, input().split()))
    c_start.append((a[0], a[1]))
    c_dest.append(([a[2], a[3]]))
