# 외계인 침공

TC = int(input())
for i in range(3):

    n, k = map(int, input().split())
    planet = list(map(int, input().split()))
    planet = reversed(sorted(planet))
    citizen = k
    mobil_count = 0
    for j in planet:
        if k >= j:
            k -= j
            citizen += j
        elif k < j:
            if k + citizen < j:
                print(f'#{i} -1')
                continue
            else:
                k += citizen -j
                citizen += j
                mobil_count += 1
    print(f'#{i} {mobil_count}')
            