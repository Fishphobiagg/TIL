# N개 - 끊어진 기타줄 M - 브랜드 수, 패키지 - 6개

N, M = map(int, input().split())
package_list, alone_list = [], []
for i in range(M):
    package, alone = map(int, input().split())
    package_list.append(package)
    alone_list.append(alone)

result = 0
if N >= 6:
    mul10_all_list = package_list + [i * 6 for i in alone_list]
    while N >= 6:
        result += min(mul10_all_list)
        N -= 6
    if min(package_list) < min(alone_list)*N:
        print(result + min(package_list))
    else:
        result += min(alone_list)*N
        print(result)
else:
    if min(package_list) < min(alone_list)*N:
        print(result + min(package_list))
    else:
        result += min(alone_list)*N
        print(result)