length, width, height = map(int, input().split())
n = int(input())
cube = [list(map(int, input().split())) for _ in range(n)]
volume = length * width * height
ans = 0
before = 0
cube.sort(reverse=True)

for w, cnt in cube:
    print(before)
    before <<= 3
    v = 2 ** w
    print(before)
    maxCnt = (length // v) * (width // v) * (height // v) - before
    maxCnt = min(cnt, maxCnt) # 만약 넣을 수 있는 개수가 가지고 있는 개수보다 클 경우 가지고 있는 개수만 넣기
    ans += maxCnt # 넣은 개수만큼 더하기
    before += maxCnt
if before == volume:
    print(ans)
else:
    print(-1)