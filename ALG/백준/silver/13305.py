# 주유소

# 자기보다 큰 가격의 주유소가 나오는 동안은, 계속 그 주유소에서 충전해서 가기

N = int(input())

distance = list(map(int,input().split()))
oil_price = list(map(int, input().split()))
oil_price = oil_price[:-1]

total_price = distance[0] * oil_price[0]
now_price = oil_price[0]
for price, dist in zip(oil_price, distance): 
    if price < now_price:
        now_price = price
    total_price += now_price * dist

print(total_price)