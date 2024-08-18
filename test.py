def maxprofit(stocks):
    if len(stocks) == 0 or len(stocks) == 1:
        return 0
    min_ = stocks[0]
    max_ = 0
    # print(min_)
    # print(max_)
    for i in range(1, len(stocks)):
        if stocks[i] < min_:
            min_ = stocks[i]
            # print(min_)
        if stocks[i] > max_:
            max_ = stocks[i]
            # print(max_)
    difference = max_ - min_

    if difference > 0:
        return difference
    else:
        return 0


price = [7, 6, 4, 3, 1]
print(maxprofit(price))
