# Stock Buy and Sell – Multiple Transaction Allowed


def stockBuySell(arr):
    profit = 0
    for i in range(len(arr) - 1):
        if prices[i + 1] > prices[i]:
            profit += prices[i + 1] - prices[i]
    return profit


prices = [7, 1, 5, 3, 6, 4]
print(stockBuySell(prices))
# 80+80+50+495+200
#
