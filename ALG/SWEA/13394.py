# A번 - B번까지 감, A,B는 반드시 정차
# 1 : 일반버스 2 : 급행 3: 광역 급행
# 일반버스 : A~B사이 모든 정류장 정차
# 급행 : A가 짝수인 경우 A와 B사이 모든 짝수 번호 정류장에 정차,
# 홀수인 경우 A와 B 사이 홀수 번호 정류장에 정차
# 광역급행 : A가 짝수인 경우 A와 B 사이 모든 4의 배수 번호 정류장에
# A가 홀수인 경우 A와 B사이 3의 배수이면서 10의 배수가 아닌 정류장에

T = int(input())

for _ in range(T):
    N = int(input())
    bus_list = [list(map(int, input().split())) for i in range(N)]
    end = 0
    for i in bus_list:
       if i[2] > end:
           end = i[2]
    count_list = [0 for i in range(end)]
    for bus in bus_list:
        if bus[0] == 1:

            for i in range(bus[1], bus[2]):
                count_list[i-1] += 1
        elif bus[0] == 2:
            if bus[1] % 2 == 0:
                for i in range(bus[1], bus[2]):
                    if i % 2 == 0:
                        count_list[i-1] += 1
            else:
                for i in range(bus[1], bus[2]):
                    if i % 2 == 1:
                        count_list[i-1] += 1
        else:
            if bus[1] % 2 == 0:
                for i in range(bus[1], bus[2]):
                    if i % 4 == 0:
                        count_list[i-1] += 1
            else:
                for i in range(bus[1], bus[2]):
                    if i % 3 == 0 and i % 10 != 0:
                        count_list[i-1] += 1
    print(f'#{_+1} {max(count_list)}')