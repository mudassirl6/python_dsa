prices = [7,1,5,3,6,4]

buy_price = float('inf')

max_profit = 0
total_profit = 0

for price in prices:
    if buy_price < price:
        max_profit = max(max_profit, price - buy_price)
    else:
        buy_price = price
        
print(max_profit)
        
        
