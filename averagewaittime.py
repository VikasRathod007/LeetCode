def averageWaitingTime(customers):
    # wait = []
    # finish = []
    res = 0.0
    cur = 0
    for arrival, time in customers:
        if arrival > cur:
            cur = time + arrival
            res += time
        else:
            cur = cur + time
            res += cur - arrival

    return res / len(customers)


customers = [[5, 2], [5, 4], [10, 3], [20, 1]]
print(averageWaitingTime(customers))
