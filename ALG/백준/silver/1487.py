# 물건 팔기

N = int(input())

price_list = []
shipping_list = []

for i in range(N):
    sell_price, shipping_fee = map(int, input().split())
    price_list.append(sell_price)
    shipping_list.append(shipping_fee)

max_revenue = 0
sell_price = 0
for price in price_list: #판매할 가격
    revenue = 0
    for j,k in zip(price_list, shipping_list):
        if price-k >= 0 and j >= price:
            revenue += price - k
    if revenue > max_revenue:
        sell_price = price
        max_revenue = revenue
    elif revenue == max_revenue and price < sell_price:
        sell_price = price

print(sell_price)
