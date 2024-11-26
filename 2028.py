# Find Missing Observations
def missingRolls(rolls, mean, n):
    res = []
    m = len(rolls)
    total_sum = mean * (m + n)
    missing_sum = total_sum - sum(rolls)
    if missing_sum > 6 * n or missing_sum < n:
        return []
    dice = missing_sum // n
    remainder = missing_sum % n
    res = [dice] * n
    for i in range(remainder):
        res[i] += 1
    # while n:
    #     dice = min(6, missing_sum - n + 1)
    #     res.append(dice)
    #     missing_sum -= dice
    #     n -= 1
    return res


rolls = [3, 2, 4, 3]
mean = 4
n = 2
print(missingRolls(rolls, mean, n))
