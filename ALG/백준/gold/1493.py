# Box 채우기

'''
한 변의 길이 - 박스 종류 2**(박스 종류 번호)
2차원 배열로 가로세로높이 표현

같은단차인 경우에만 쌓을 수 있음
'''

l,w,h = map(int,input().split())
N = int(input())
ans = l*w*h
used = 0
cube = [0]*21
for i in range(N):
    a, b = map(int,input().split())
    cube[a] += b

for i in range(20, -1, -1):
