def maxprofit(stocks):
    if len(stocks) == 0 or len(stocks) == 1:
        return 0
    min_price = stocks[0]
    max_profit = 0
    for price in stocks:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


price = [7, 1, 5, 3, 6, 4]
print(maxprofit(price))
