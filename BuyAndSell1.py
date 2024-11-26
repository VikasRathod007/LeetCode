def maximumProfit(prices):
    if not prices or len(prices) < 2:
        return 0
    max_profit = 0
    stock = prices[0]
    # for i in range(len(prices) - 1):
    #     if stock < prices[i + 1]:
    #         max_profit = max(max_profit, prices[i + 1] - stock)
    #         print(max_profit)
    #     else:
    #         stock = prices[i + 1]
    #         print("stock", stock)
    # return max_profit
    for price in prices[1:]:
        if price > stock:
            max_profit = max(max_profit, price - stock)
        else:
            stock = price
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(maximumProfit(prices))
