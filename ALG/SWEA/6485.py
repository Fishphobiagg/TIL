# 삼성시의 버스노선

T = int(input())

for _ in range(T):
    N = int(input())
    max_terminal = 0
    terminal_list = []
    for i in range(N):
        A, B = map(int,input().split())
        terminal_list.append([A,B])
        if B > max_terminal:
            max_terminal = B
    counter = [0 for i in range(max_terminal)]
    for terminal in terminal_list:
        for i in range(terminal[0], terminal[1]+1):
            counter[i-1] += 1
    
    P = int(input())
    print(f'#{_+1}', end=' ')
    for i in range(1, P): 
        C = int(input())
        print(f'{counter[C-1]}', end=' ')